# Rainfall-Prediction

A project on predicting whether it will rain tomorrow or not by using the Rainfall in Australia dataset This project is tested over lot of ml models like catboost, xgboost, random forest, support vector classifier, etc.. Out of these models catboost performed very well giving an AUC score around 0.86 and ROC score of 89 far better than others.

## Download Dataset

* [Dataset link](https://github.com/mon28/Datasets/raw/main/rainfall-australia-data.zip)

## How to run?

#### STEP 01: Clone the repo and create a conda environment

```bash
git clone https://github.com/mon28/Rainfall-Prediction.git
cd Rainfall-Prediction
conda create -n rainfall python=3.8 -y
conda activate rainfall
```

#### STEP 02: Install requirements

```bash
pip install -r requirements.txt
```

#### STEP 03: Run the Streamlit app

```bash
python main.py
```