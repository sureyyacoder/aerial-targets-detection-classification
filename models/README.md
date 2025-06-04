# Trained Models

This folder contains all trained YOLOv8 model files (`.pt`) for the AirAi Vision project. Each model corresponds to a specific dataset version used during development or final training.

---

## Model Descriptions

| Model File | Description |
|------------|-------------|
| `uav_best.pt` | Trained on the single-class UAV dataset |
| `airplane_passenger_v1_best.pt` | Trained on passenger aircraft (Airbus vs Boeing, v1 version) |
| `airplane_passenger_v2_best.pt` | Single class version of v1 |
| `airplane_military_best.pt` | Trained on multi-class military aircraft dataset |
| `helicopter_civil_best.pt` | Trained on the civil helicopter dataset (single class) |
| `helicopter_military_v1_best.pt` | Trained on v1 of the military helicopter dataset |
| `helicopter_military_v2_best.pt` | Cleaned version of v1 with low-performance classes removed |
| `final_dataset_best.pt` | Trained on the unified final dataset (UAV, airplane, helicopter) with global class IDs |

> Note: `v2` versions indicate datasets that were cleaned or refined after initial experiments.

---

## 🔗 Download Link

All model files can be accessed here:

- [Trained Models - Google Drive Folder](https://drive.google.com/drive/folders/1in1ieIROunwgQVFI0O20fdV0nR64N-Xk?usp=drive_link)

---

##  How to Use (YOLOv8)

You can use any of these models with the [Ultralytics YOLOv8](https://docs.ultralytics.com) toolkit. Example inference command:

```bash
yolo task=detect mode=predict model=final_dataset_best.pt source=your_image.jpg
