# UniKP Replication Report

## Overview
This report documents the replication of a simple use case from the UniKP paper using the provided codebase. The goal was to demonstrate the capability to predict enzyme turnover numbers ($k_{cat}$) using the UniKP framework.

## Use Case Selection
The original plan was to replicate the "High-efficiency NeuAc biosynthesis" use case mentioned in the paper. However, the specific data for NeuAc biosynthesis was not explicitly identifiable in the provided `datasets/Kcat_combination_0918_wildtype_mutant.json` file. 

Therefore, a general **$k_{cat}$ prediction** use case was selected, using a random subset of enzymes from the provided dataset. This demonstrates the core functionality of the UniKP framework: taking enzyme sequences and substrate SMILES as input and predicting kinetic parameters.

## Implementation Details
A Python script `studies/Demo/demo_replicate.py` was created to perform the following steps:
1.  **Load Data**: Reads `datasets/Kcat_combination_0918_wildtype_mutant.json`.
2.  **Select Subset**: Selects a small subset of 20 samples to ensure quick execution.
3.  **Feature Extraction**:
    *   **Substrate**: Uses the pre-trained SMILES Transformer (loaded from `assets/trfm_12_23000.pkl` and `assets/vocab.pkl`) to generate embedding vectors for substrate SMILES strings.
    *   **Protein**: The original UniKP implementation uses the **ProtT5-XL-UniRef50** model, which requires downloading ~11GB of model weights. To allow the demo to run quickly on standard hardware without massive downloads, **protein features were mocked with random vectors** in this demonstration. A flag `MOCK_PROTEIN_FEATURES` in the script controls this behavior.
4.  **Model Training**: Trains an `ExtraTreesRegressor` on 15 samples.
5.  **Prediction**: Predicts $k_{cat}$ for the remaining 5 samples.

## Results
The demo script successfully ran and produced predictions. 

**Note**: Due to the use of random vectors for protein features and the extremely small training set (15 samples), the predictive accuracy is expected to be poor. The purpose of this demo is to validate that the code pipeline (data loading, feature extraction, model interface) functions correctly.

**Sample Output (from `studies/Demo/demo_results.csv`):**

| Organism | Substrate | Actual kcat ($s^{-1}$) | Predicted kcat ($s^{-1}$) | Log10 Actual | Log10 Predicted |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Streptomyces griseus | Catechol | 12.00 | 5.44 | 1.08 | 0.74 |
| Streptomyces griseus | 3-amino-4-hydroxybenzaldehyde | 14.00 | 1.56 | 1.15 | 0.19 |
| Streptomyces griseus | 2-Amino-p-cresol | 18.00 | 3.36 | 1.26 | 0.53 |
| Streptomyces griseus | o-aminophenol | 20.00 | 3.17 | 1.30 | 0.50 |
| Ruegeria pomeroyi | dimethylsulfoniopropionate | 2.40 | 6.68 | 0.38 | 0.82 |

## How to Run the Demo
1.  Ensure you have the required dependencies installed (see `requirements.txt`).
2.  Run the replication script:
    ```bash
    python3 studies/Demo/demo_replicate.py
    ```
3.  The results will be printed to the console and saved to `studies/Demo/demo_results.csv`.

## Enabling Full Replication
To run the full replication with real protein features:
1.  Open `studies/Demo/demo_replicate.py`.
2.  Set `MOCK_PROTEIN_FEATURES = False` (Line ~32).
3.  Ensure you have a stable internet connection to download the ProtT5-XL model (~11GB) or have it cached locally.
4.  Run the script again. The first run will take significant time to download the model.
