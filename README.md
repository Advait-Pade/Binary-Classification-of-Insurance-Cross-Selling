# Experiment Repository

This repository contains Jupyter notebooks and associated resources for implementing and logging machine learning workflows, as well as their integration into a Flask application. Below is an overview of the experiments conducted, along with visual representations of logged models and downloadable artifacts.

---

## Table of Contents
- [Implementation Steps](IMPLEMENTATION_STEPS.md)
- [First Experiment](#first-experiment)
- [Second Experiment](#second-experiment)
- [Promoting a Model in MLflow](#promoting-a-model-in-mlflow)
  - [Flask Application](#flask-application)

---

## First Experiment
**Notebook**: `First Experiment.ipynb`  
This experiment demonstrates a basic machine learning workflow using three different classifiers:

- **Logistic Regression**  
- **Random Forest Classifier**  
- **XGBoost Classifier**  

### Logged Models
The models trained and logged during this experiment are visualized below:  
![First Experiment Logged Models](images/First%20Experiment/Logged%20Models.png)

---

## Second Experiment
**Notebook**: `Second Experiment.ipynb`  
This experiment focuses on storing and logging valuable resources, including:

- The dataset used in the experiment  
- Confusion matrix for model evaluation  
- AUC (Area Under the Curve) metric for performance analysis  
- Model file (saved in `.pkl` format)  

### Logged Models
The models logged during this experiment are visualized below:  
![Second Experiment Logged Models](images/Second%20Experiment/Logged%20Models.png)

### Downloadable Artifacts
Below is a snapshot of the downloadable artifacts stored during this experiment:  
![Downloadable Artifacts](images/Second%20Experiment/Downloadable%20Artifacts.png)

---

## Promoting a Model in MLflow
Promoting a model in MLflow is a critical step to transition a model from `Staging` to `Production`. Below are the steps:

1. Open the MLflow UI and navigate to the "Models" section.
2. Select the model you want to promote and choose the specific version.
3. Click on the "Stage" dropdown and select **Promote to Production**.
4. Add relevant comments for the promotion (optional) and confirm the action.

### Supporting Screenshots
- Screenshot 1: Navigating to the model version
- Screenshot 2: Selecting "Promote to Production" in the MLflow UI

---

## Flask Application
The Flask application provides a user interface to interact with the trained models. You can find the detailed steps for setting up and running the Flask application in the [Implementation Steps](IMPLEMENTATION_STEPS.md).

---

Feel free to explore the notebooks and resources in this repository for detailed insights into the experiments.
