# ECG-Based Photo Lock HCI Project


## Overview
-----------
This project implements a Human-Computer Interaction (HCI) system using ECG signals for authentication. The application allows users to unlock a system using specific ECG electrode configurations and signal processing techniques.

## Interface Description
------------------------
The graphical interface is designed using Tkinter in Python, providing a user-friendly environment for interacting with the ECG-based authentication system.

### Interface Components
- **Welcome Message**: Displays a welcome message at the top of the window.
- **File Path Entry**: Allows users to input the file path of the ECG signal for processing.
- **Electrode Buttons**: Buttons for selecting different ECG electrode configurations (i, ii, iii, avr, avf, avl, v1-v6, vx, vy, vz).
- **Feature Extraction**: Options for feature extraction methods like AC/DCT and Wavelet-Coefficients.
- **Classifier Selection**: Options for choosing classifiers such as SVM, Random Forest, and Sequential Model.
- **Proceed Button**: Button to initiate the processing and authentication.

## Preprocessing Algorithm
---------------------------
The preprocessing algorithm includes several steps to enhance and prepare the ECG signals for feature extraction and classification.

### Steps:
- **Baseline Removal**: Removes baseline wander using a bandpass filter.
- **Normalization**: Normalizes the signal to zero mean and unit variance.
- **Denoising**: Applies Savitzky-Golay filter for noise reduction.

## Feature Extraction
----------------------
Two main methods are implemented for feature extraction:

### AC/DCT Features
- Calculates Autocorrelation Function (ACF) and applies Discrete Cosine Transform (DCT) to extract features.

### Wavelet-Coefficients
- Computes wavelet coefficients using the specified wavelet function and level.

## Classification
-------------------
Three classifiers are available for ECG signal classification:

- **Support Vector Machine (SVM)**
- **Random Forest**
- **Sequential Model**

## Usage
---------
To run the application:

1. Ensure Python and necessary libraries are installed.
2. Execute the main script `main.py`.
3. Follow the interface instructions to load an ECG file, select electrodes, extract features, choose a classifier, and proceed with authentication.

## Dependencies
-----------------
Ensure the following Python libraries are installed:

- Tkinter
- Matplotlib
- Numpy
- Scipy
- PyWavelets
- Statsmodels
- Scikit-learn
- Keras

## Author
---------
\[Mohamed Fawzy\]



 
