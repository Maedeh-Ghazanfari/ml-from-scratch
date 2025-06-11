# Logistic Regression from Scratch

This project implements **Logistic Regression** from scratch in Python using **NumPy**, without relying on high-level libraries like scikit-learn (except for data preprocessing and evaluation). 

## 📁 Project Structure

- `Logistic Regression.ipynb`: Main Jupyter notebook containing:
  - Data loading
  - Data preprocessing 
  - Model implementation from scratch
  - Gradient descent updates
  - Loss plotting
  - Model evaluation

## 🚀 What’s Implemented

- Manual implementation of:
  - Sigmoid function
  - Log loss (cross-entropy loss)
  - Gradient descent (parameter updates)
- Training loop with weight and bias updates
- Loss visualization over training epochs
- Evaluation with classification report and confusion matrix

## 📊 Evaluation Metrics

Model performance is evaluated using:
- **Accuracy**
- **Precision**
- **Recall (Sensitivity)**
- **Specificity**
- **F1-Score**

These metrics help assess the model's robustness, especially on imbalanced datasets.

## ⚠️ Common Issues and Fixes

- **Numerical instability**: Applied `np.clip()` to avoid log(0) issues in log loss.
- **All-zero predictions**: May happen if the model underfits or due to extremely small gradients.
- **Evaluation warnings**: Use `zero_division=0` to handle undefined precision when no samples are predicted for a class.

## 📈 Loss Plot

The notebook includes a line plot of the loss decreasing over time during training. This helps confirm whether gradient descent is working as expected.

## ✅ Requirements

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- scikit-learn

Install dependencies:
```bash
pip install numpy pandas matplotlib scikit-learn

