# Notebooks - AirAi Vision

This folder contains all Jupyter notebooks used throughout the project for data preparation, model training, and utility tasks.

---

## Notebook Overview

| Notebook | Description |
|----------|-------------|
| `converting_classIDs_for_final_dataset.ipynb` | Remaps class IDs to a unified format for the final dataset |
| `final_dataset_splits.ipynb` | Splits the unified dataset into train/valid/test sets (80/10/10) |
| `unzipping_and_moving_datasets.ipynb` | Unzips raw datasets and organizes them under `processed/` folder |
| `train_uav_yolov8s.ipynb` | Trains YOLOv8s model on single-class UAV dataset |
| `train_airplane_passenger_yolov8s.ipynb` | Trains model on airplane passenger dataset (2-class or 1-class) |
| `train_airplane_military_yolov8m.ipynb` | Trains model on multi-class military aircraft dataset |
| `train_helicopter_civil_yolov8.ipynb` | Trains model on civil helicopter dataset |
| `train_helicopter_military_yolov8m.ipynb` | Trains model on military helicopter dataset (v1 and v2) |
| `train_final_dataset.ipynb` | Trains the final unified model using all categories and cleaned data |

---

> 📌 All notebooks are written for Google Colab and assume dataset paths under `/content/drive/`.

