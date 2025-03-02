# Liver Segmentation in Healthcare Imaging

## Overview
This project implements an AI-driven solution for the segmentation of liver images in medical imaging. It leverages PyTorch and MONAI to automate the preprocessing, segmentation, and evaluation of liver images. The aim is to enhance diagnostic efficiency and accuracy by reducing the reliance on manual segmentation.

## Features
- **Data Preparation:** Conversion of NIfTI files to DICOM, slice grouping, and image preprocessing
- **File Management:** Automated directory creation, and file organization
- **Model Training:** Utilizes a segmentation model optimized with the Dice coefficient loss function and weighted cross-entropy to handle class imbalances.
- **Evaluation:** Tools for assessing model performance and segmentation accuracy.

## Prerequisites
- Python 3.12
- PyTorch
- MONAI
- Additional Python libraries: `numpy`, `pandas`, `os`, `shutil`, `streamlit`, `sqlite3`, `bcrypt`, `time`, `PIL from Image`
- download the nifti files from : https://drive.google.com/drive/folders/1HqEgzS8BV2c7xYNrZdEAnrHk7osJJ--2

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/darth-Vader1729/MEDICO_AI.git
   cd MEDICO_AI


2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt

## Usage
1. **Data Preparation:**
Run the script to convert NIfTI files to DICOM and organize image slices:
    ```bash
    python extract_archives.py 
<!-- 2. **Model Training:**
Train the segmentation model:
    ```bash
    python train.py --data_folder path/to/organized_data --epochs 50

3. **Evaluation:**
Evaluate model performance using the Dice coefficient:
    ```bash
    python evaluate.py --model_path path/to/trained_model --test_data path/to/test_data -->


Directory Structure
```bash
MEDICO_AI/
├── TestingDATA/         # Raw and preprocessed data
├── models/              # Saved models and checkpoints
├── Medico_AI.py         # spins the website into existence
├── README.md
└── requirements.txt
