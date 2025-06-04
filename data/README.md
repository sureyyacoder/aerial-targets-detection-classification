# Datasets

This project includes multiple datasets, starting from raw formats, processed experimental subsets, and finally a cleaned, unified dataset for final training. You can access each dataset and its details below.

---

## 1. Processed Experimental Datasets (`processed/`)

This section contains datasets that were preprocessed from raw sources for individual model training and evaluation. These datasets were used to analyze performance across different vehicle types and subcategories.

> All experimental datasets follow a **70-20-10 split** structure (train/valid/test).

For example, the helicopter dataset has multiple versions:
- **v1:** The original dataset
- **v2:** A cleaned version with low-performing classes and noisy images removed

**General Folder Structure:**

```bash
processed/
├── images/
│   ├── train/
│   │   ├── airplane/
│   │   │   ├── military/
│   │   │   ├── passenger/
│   │   │   └── passenger_one_class/
│   │   ├── helicopter/
│   │   │   ├── civil/
│   │   │   ├── military/
│   │   │   └── military_v2/
│   │   └── UAV/
│
├── valid/
│   └── (same structure as train)
│
├── test/
│   └── (same structure as train)
│
├── labels/
│   ├── train/
│   ├── valid/
│   └── test/
```


**Access Links:**

You can browse and download the experimental datasets directly using the links below:

- [Processed Images Folder (train/valid/test)](https://drive.google.com/drive/folders/1-O72NqQivIU2VrZQLdEWxMpHistCFas1?usp=drive_link)
- [Processed Labels Folder (train/valid/test)](https://drive.google.com/drive/folders/1-Kk2WBaq5_80v3mZ6LNB2JOuLSpUzgDY?usp=drive_link)

---

## 2. Final Unified Dataset (`final_dataset/`)

After evaluating the experimental datasets and model results, a final unified dataset was created. This dataset includes all major vehicle types and subcategories with cleaned annotations and globally unique class IDs.

- **Classes Included:** UAV, Airplane Passenger (one-class), Military Aircraft (cleaned), Helicopter Civil, Helicopter Military (v2)
- **Label Definitions:** Listed in `final_dataset_config.yaml` 

**Access Links:**

- [Final Dataset - Train](https://drive.google.com/drive/folders/16XYlC5a72ifbu0jhrmIgbMb8rAFIsAJh?usp=drive_link)
- [Final Dataset - Valid](https://drive.google.com/drive/folders/1hEhtY8jYgyjszIuGei9w26yYCK48Z44T?usp=drive_link)
- [Final Dataset - Test ](https://drive.google.com/drive/folders/1eV72SKz9-gsq0sxD_n8wbBG92521n9V8?usp=drive_link)

**Format:** YOLOv8 directory structure  
**Split Ratio:** 80% training, 10% validation, 10% testing

---

## 3. Raw Data Sources (`raw/`)

These are the original datasets collected and downloaded from Roboflow in YOLOv8 format. Each is shared as a zipped archive and includes labels, images, and a data.yaml file.

**Datasets Included:**
- UAV (single class)
- Airplane Passenger (single class and multi-class)
- Airplane Military (multi-class, v1 & v2)
- Helicopter Civil (single class)
- Helicopter Military (multi-class, v1 & v2)

- [Raw Dataset Folder (Zipped)](https://drive.google.com/drive/folders/1chD6wc1-BE-_WIe0WGkAsy48y1FBqojU?usp=drive_link)

---
## Dataset Configuration Files (data_configs/)

This folder contains all data.yaml configuration files used during training for both experimental and final datasets.
Each YAML file defines class names, number of classes, and directory paths used by YOLOv8.
Useful for reproducing training results or modifying dataset splits.

 [YAML files](https://drive.google.com/drive/folders/1qq0EVDEitYIEXA-zqkCPMXgW6yHEp8WC?usp=drive_link)

 ---

##  Annotation Format (YOLOv8)

All datasets follow the [YOLOv8 format](https://docs.ultralytics.com/datasets/):

Each image has a corresponding `.txt` label file with the following format:

<class_id> <x_center> <y_center> <width> <height>

