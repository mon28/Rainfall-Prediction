from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    REQUIRED_FILES: list
    STATUS_FILE: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_filepath: Path
    train_data_filename: Path
    eval_data_filename: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    model_name: Path
    data_filepath: Path
    max_iterations: int
    eval_metric: str

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_filepath: Path
    model_path: Path
    model_name: Path
    metric_file_name: Path