# Model Training Experiments

This folder contains all experimental training results for the AirAi Vision project. Each subfolder corresponds to a model trained on a specific dataset variant.

Results include validation predictions, performance curves (Precision, Recall, F1), confusion matrices, and other metrics.

---

## Experiment Overview

| Dataset | Subfolder | Description |
|---------|-----------|-------------|
| UAV | `uav/` | Single-class UAV detection experiment with 15 epoch |
| Airplane (Passenger) | `airplane/passenger_v1/` | Airbus vs Boeing classification (v1) with 20 epoch |
| Airplane (Passenger) | `airplane/passenger_v2/` | Sigle class version with 30 epoch |
| Airplane (Military) | `airplane/military/` | Multi-class military aircraft detection with 75 epoch |
| Helicopter (Civil) | `helicopter/civil/` | Single-class civil helicopter detection with 30 epoch|
| Helicopter (Military) | `helicopter/military_v1/` | Original multi-class military helicopter dataset with 50 epoch|
| Helicopter (Military) | `helicopter/military_v2/` | Cleaned version of v1 with noisy classes removed with 50 epoch|

---

Each subfolder includes:
- 🔲 Precision / Recall / F1 Curve
- 🔲 Confusion Matrix
- 🔲 Validation Predictions
- 🔲 CSV with metrics 

To dive into results, navigate to the desired subfolder.

---

For final dataset performance results, see:  
➡️ `results/` folder (used for the unified final model training).
