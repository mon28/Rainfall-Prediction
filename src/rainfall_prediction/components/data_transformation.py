import os
import sys
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from rainfall_prediction.logging import logger
from rainfall_prediction.app_exception.exception_handler import AppException
from rainfall_prediction.config.configuration import DataTransformationConfig


class DataTransformation(object):
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.df = None
        self.numerical_features = None
        self.target_name = "RainTomorrow"
    

    def load_data(self):
        self.df = pd.read_csv(self.config.data_filepath)
        pd.set_option("display.max_columns", None)


    def transform_data(self):
        try:
            self.load_data()

            logger.info(f"Shape of Rainfall data file: {self.df.shape}")
            
            # handling high number of null values with random imputation
            self.perform_random_sample_imputation(["Evaporation", "Sunshine"])

            # handle continuous features
            continuous_features = self.get_continuous_features()   
            self.handle_missing_features_with_median(continuous_features)
            self.handle_outliers_with_bridges(continuous_features)

            # handle discrete features
            discrete_features = self.get_discrete_features()
            self.handle_missing_features_with_mode(discrete_features)

            # handle binary features
            self.handle_binary_features(["RainToday", self.target_name])

            # handle categorical features
            self.handle_categorical_features(["WindGustDir",
                                              "WindDir9am",
                                              "WindDir3pm"])
            
            # handle Location feature
            self.handle_location_feature()

            # handle Date feature
            self.handle_date_feature()

            # export data
            self.export_transformed_data()
            logger.info(f"Exported transformed data of shape {self.df.shape}")

        except Exception as e:
            raise AppException(e, sys) from e
    
    def get_continuous_features(self):
        if not self.numerical_features:
            self.numerical_features = [feature for feature in self.df.columns 
                                       if self.df[feature].dtypes != 'O']
        continuous_features = [feature for feature in self.numerical_features 
                               if len(self.df[feature].unique()) >= 25]
        return continuous_features


    def get_discrete_features(self):
        if not self.numerical_features:
            self.numerical_features = [feature for feature in self.df.columns 
                                       if self.df[feature].dtypes != 'O']
        discrete_features = [feature for feature in self.numerical_features 
                             if len(self.df[feature].unique()) < 25 ]
        return discrete_features


    def perform_random_sample_imputation(self, features):
        for feature in features:
            random_sample = self.df[feature].dropna().sample(self.df[feature].isnull().sum(), random_state=0)
            random_sample.index = self.df[self.df[feature].isnull()].index
            self.df.loc[self.df[feature].isnull(), feature] = random_sample


    def handle_missing_features_with_median(self, features):
        for feature in features:
            if(self.df[feature].isnull().sum()*100/len(self.df)) > 0:
                self.df[feature] = self.df[feature].fillna(self.df[feature].median())


    def handle_missing_features_with_mode(self, features):
        for feature in features:
            mode = self.df[feature].value_counts().index[0]
            self.df[feature].fillna(mode, inplace=True)


    def handle_binary_features(self, features):
        for feature in features:
            self.df[feature] = pd.get_dummies(self.df[feature], drop_first=True)


    def handle_categorical_features(self, features):
        
        for feature in features:
            rank = 0
            all_ordered_values = list(self.df.groupby([feature])[self.target_name].mean()
                                    .sort_values(ascending=False).index)
            value_rank_map = {}
            for value in all_ordered_values:
                value_rank_map[value] = rank
                rank += 1

            # replaced each discrete value with corresponding rank
            self.df[feature] = self.df[feature].map(value_rank_map)

            # handle null values: fill the rank of the value that occurs the most
            self.df[feature].fillna(self.df[feature].value_counts().index[0], inplace=True)

        
    def handle_location_feature(self):
        rank = 1
        value_rank_map = {}

        df_locations_target = \
            self.df.groupby(["Location"])[self.target_name].value_counts().sort_values().unstack()
        all_ordered_values = list(df_locations_target[1].sort_values(ascending=False).index)
        for value in all_ordered_values:
                value_rank_map[value] = rank
                rank += 1

        self.df["Location"] = self.df["Location"].map(value_rank_map)

    
    def handle_date_feature(self):
        self.df["Date"] = pd.to_datetime(self.df["Date"], format="%Y-%m-%dT", errors="coerce")
        self.df["Date_month"] = self.df["Date"].dt.month
        self.df["Date_day"] = self.df["Date"].dt.day
        self.df = self.df.drop(["Date"], axis=1)

    
    def handle_outliers_with_bridges(self, features):
        for feature in features:
            IQR = self.df[feature].quantile(0.75) - self.df[feature].quantile(0.25)
            lower_bridge = self.df[feature].quantile(0.25) - (IQR * 1.5)
            upper_bridge = self.df[feature].quantile(0.75) + (IQR * 1.5)

            self.df.loc[self.df[feature] <= lower_bridge, feature] = lower_bridge
            self.df.loc[self.df[feature] >= upper_bridge, feature] = upper_bridge


    def prepare_train_test_data(self):
        try:
            X = self.df.drop(["RainTomorrow"], axis=1)
            y = self.df["RainTomorrow"]

            X_train, X_test, y_train, y_test = \
                train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)
            
            logger.info("The Class Balance before fit {}".format(Counter(y_train)))
            sm = SMOTE()
            sm = SMOTE(random_state=0)
            X_train_res, y_train_res = sm.fit_resample(X_train, y_train)
            logger.info("The Class Balance after fit {}".format(Counter(y_train_res)))

            return X_train_res, y_train_res, X_test, y_test

        except Exception as e:
            raise AppException(e, sys) from e


    def export_transformed_data(self):
        try:
            X_train, y_train, X_test, y_test = self.prepare_train_test_data()

            train_data = X_train
            train_data[self.target_name] = y_train
            train_data.to_pickle(os.path.join(self.config.root_dir, self.config.train_data_filename))
            logger.info(f"Exported Train data of shape: {train_data.shape}")

            eval_data = X_test
            eval_data[self.target_name] = y_test
            eval_data.to_pickle(os.path.join(self.config.root_dir, self.config.eval_data_filename))
            logger.info(f"Exported Eval data of shape: {eval_data.shape}")

        except Exception as e:
            raise AppException(e, sys) from e


        

        


        




    
    
    

