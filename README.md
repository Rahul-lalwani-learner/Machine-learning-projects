# Machine Learning Projects Repository 🚀

Welcome to my comprehensive collection of machine learning and computer vision projects! This repository showcases a diverse range of projects from data science and machine learning to computer vision applications using YOLO and deep learning frameworks.

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [Machine Learning Projects](#machine-learning-projects)
  - [Computer Vision Projects](#computer-vision-projects)
  - [Competition Projects](#competition-projects)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## 🔍 Overview

This repository contains 9 different projects covering various aspects of machine learning, deep learning, and computer vision. Each project demonstrates different techniques, from traditional machine learning algorithms to state-of-the-art deep learning models and real-time object detection systems.

## 🎯 Projects

### Machine Learning Projects

#### 1. 🚜 Bulldozer Price Prediction
**Location:** `Bulldozer-price-prediction/`

A comprehensive end-to-end machine learning project that predicts the sale price of bulldozers using regression techniques.

- **Problem:** Predict future sale prices of bulldozers based on their characteristics and historical data
- **Dataset:** Kaggle Bluebook for Bulldozers competition data
- **Evaluation Metric:** RMSLE (Root Mean Squared Log Error)
- **Features:** Multiple bulldozer characteristics and specifications
- **Key Files:**
  - `end-to-end-Bulldozer-price-regression.ipynb` - Main analysis notebook
  - `Final_predictions.csv` - Model predictions
  - `environment.yml` - Conda environment configuration
  - `dataset/` - Training, validation, and test datasets

#### 2. ❤️ Heart Disease Classification
**Location:** `Heart-disease-project/`

A binary classification project to predict heart disease presence based on clinical parameters.

- **Problem:** Predict whether a patient has heart disease based on medical attributes
- **Dataset:** Cleveland data from UCI Machine Learning Repository
- **Target Accuracy:** 95% for proof of concept
- **Features:** Age, sex, chest pain type, blood pressure, cholesterol, ECG results, etc.
- **Key Files:**
  - `end-to-end-heart-disease-classification.ipynb` - Complete analysis
  - `GridSearchCV_LogisticRegresion.pkl` - Trained model
  - `environment.yml` - Dependencies
  - `data/heart-disease.csv` - Dataset

#### 3. 🐕 Dog Breed Prediction
**Location:** `Dog-breed-prediction/`

A multi-class image classification project using deep learning to identify dog breeds.

- **Problem:** Classify dog breeds from images using computer vision
- **Model:** MobileNetV2 with transfer learning
- **Framework:** TensorFlow/Keras
- **Key Files:**
  - `end_to_end_dog_vision.ipynb` - Main notebook
  - `models/` - Trained model files (.h5 format)
  - `logs/` - Training logs and TensorBoard data
  - `custom-data/` - Custom test images
  - `full_model_predictions_submission_1_mobilenetV2.csv` - Predictions

#### 4. 🖐️ Palmprint Detection
**Location:** `Palmprint-detection-project/`

A specialized computer vision project for palmprint detection and analysis.

- **Research Paper:** Included (`9939-Article Text-17682-1-10-20210714.pdf`)
- **Key Files:**
  - `end_to_end_palmprint_detection.ipynb` - Implementation notebook
  - `custom-images/` - Test palmprint images
  - `environment.yml` - Environment setup

### Computer Vision Projects

#### 5. 🚗 Car Counter (Project 1)
**Location:** `Project 1 - Car Counter/`

Real-time vehicle counting system using YOLO object detection and SORT tracking.

- **Technology:** YOLOv8, OpenCV, SORT tracking algorithm
- **Features:** Real-time detection, vehicle tracking, counting across a line
- **Key Files:**
  - `Car-Counter.py` - Main application
  - `sort.py` - SORT tracking implementation
  - `mask.png` - Region of interest mask
  - `graphics.png` - UI graphics

#### 6. 👥 People Counter (Project 2)
**Location:** `Project 2 - People Counter/`

Similar to the car counter but optimized for counting people in video streams.

- **Technology:** YOLO, OpenCV, tracking algorithms
- **Application:** Crowd monitoring, occupancy counting
- **Key Files:**
  - `People-Counter.py` - Main application
  - `sort.py` - Tracking algorithm
  - `mask.png`, `graphics.png` - UI components

#### 7. 🦺 PPE Detection (Project 3)
**Location:** `Project 3 - PPE Detection/`

Personal Protective Equipment detection system for workplace safety monitoring.

- **Purpose:** Detect safety equipment like hardhats, masks, safety vests
- **Classes:** 25 different classes including safety equipment and vehicles
- **Key Files:**
  - `PPEDetection.py` - Main detection script
  - `best.pt` - Trained YOLO model weights

**Detected Classes:**
- Safety Equipment: Hardhat, Mask, Safety Vest, Gloves
- Violations: NO-Hardhat, NO-Mask, NO-Safety Vest
- Vehicles: Excavator, SUV, truck, bus, etc.
- Other: Person, Safety Cone, Ladder, etc.

#### 8. 🃏 Poker Card Detection (Project 4)
**Location:** `Project 4 - Poker Card Detection/`

Advanced computer vision system for detecting and recognizing poker cards and hands.

- **Features:** Card detection, hand recognition, poker hand classification
- **Key Files:**
  - `Poker-Hand-Detector.py` - Main detector
  - `PokerHandFunction.py` - Hand evaluation logic
  - `best.pt`, `last.pt` - Model weights
  - `Training_results/` - Training metrics and validation images

### Competition Projects

#### 9. 🌍 Smartathon HackerEarth - Pollutant Classification
**Location:** `Smartathon-Hackerearth/`

A machine learning competition project for environmental data analysis.

- **Competition:** HackerEarth Smartathon
- **Problem:** Pollutant classification from environmental data
- **Duration:** 10-day learning and implementation project
- **Key Files:**
  - `Pollutant_classification.ipynb` - Complete solution
  - `readme.md` - Project-specific documentation
- **Dataset:** Available via Google Drive link in project readme

## 🛠️ Technologies Used

### Machine Learning & Data Science
- **Python Libraries:** pandas, numpy, scikit-learn, matplotlib, seaborn
- **Machine Learning:** Random Forest, Logistic Regression, GridSearchCV
- **Deep Learning:** TensorFlow, Keras, MobileNetV2
- **Environment Management:** Conda, pip

### Computer Vision
- **Frameworks:** OpenCV, Ultralytics YOLO (YOLOv8)
- **Object Detection:** YOLO models, custom trained weights
- **Tracking:** SORT (Simple Online and Realtime Tracking)
- **Image Processing:** cvzone, cv2

### Development Tools
- **Notebooks:** Jupyter Notebook (.ipynb)
- **Version Control:** Git
- **Model Formats:** .h5 (Keras), .pt (PyTorch/YOLO), .pkl (scikit-learn)

## 🚀 Setup Instructions

### General Requirements
```bash
# Clone the repository
git clone https://github.com/Rahul-lalwani-learner/Machine-learning-projects.git
cd Machine-learning-projects
```

### For Machine Learning Projects
```bash
# Navigate to specific project directory
cd Heart-disease-project  # or Bulldozer-price-prediction, etc.

# Create conda environment
conda env create -f environment.yml
conda activate [environment-name]

# Launch Jupyter Notebook
jupyter notebook
```

### For Computer Vision Projects
```bash
# Install required packages
pip install ultralytics opencv-python cvzone

# For YOLO projects, ensure you have the model weights
# Some projects include pre-trained weights (best.pt)
# Others may require downloading YOLOv8 weights

# Run the application
python Car-Counter.py  # or respective project file
```

### Video Files and Weights
- Video files are referenced from `../Videos/` directory
- YOLO weights from `../Yolo-Weights/` for some projects
- Some projects include custom trained weights (best.pt, last.pt)

## 📁 Project Structure

```
Machine-learning-projects/
├── README.md (this file)
├── Bulldozer-price-prediction/
│   ├── end-to-end-Bulldozer-price-regression.ipynb
│   ├── environment.yml
│   ├── Final_predictions.csv
│   └── dataset/ (training data)
├── Dog-breed-prediction/
│   ├── end_to_end_dog_vision.ipynb
│   ├── models/ (trained models)
│   ├── logs/ (training logs)
│   └── custom-data/ (test images)
├── Heart-disease-project/
│   ├── end-to-end-heart-disease-classification.ipynb
│   ├── GridSearchCV_LogisticRegresion.pkl
│   └── data/heart-disease.csv
├── Palmprint-detection-project/
│   ├── end_to_end_palmprint_detection.ipynb
│   └── custom-images/
├── Project 1 - Car Counter/
│   ├── Car-Counter.py
│   └── sort.py
├── Project 2 - People Counter/
│   ├── People-Counter.py
│   └── sort.py
├── Project 3 - PPE Detection/
│   ├── PPEDetection.py
│   └── best.pt
├── Project 4 - Poker Card Detection/
│   ├── Poker-Hand-Detector.py
│   ├── PokerHandFunction.py
│   ├── best.pt
│   └── Training_results/
└── Smartathon-Hackerearth/
    ├── Pollutant_classification.ipynb
    └── readme.md
```

## 🎯 Key Features

### Machine Learning Projects
- **End-to-end workflows** from data preprocessing to model deployment
- **Multiple evaluation metrics** and model comparison
- **Feature engineering** and data visualization
- **Model persistence** with pickle and joblib
- **Environment reproducibility** with conda/pip requirements

### Computer Vision Projects
- **Real-time processing** capabilities
- **Object tracking** across video frames
- **Custom trained models** for specific use cases
- **Multi-class detection** with confidence scoring
- **Visual feedback** with bounding boxes and labels

## 📊 Results and Performance

### Machine Learning
- **Bulldozer Price Prediction:** RMSLE optimization for auction price prediction
- **Heart Disease Classification:** Target 95% accuracy achieved
- **Dog Breed Prediction:** Multi-class classification with MobileNetV2
- **Palmprint Detection:** Specialized biometric recognition

### Computer Vision
- **Car/People Counting:** Real-time tracking and counting
- **PPE Detection:** 25-class safety equipment detection
- **Poker Card Detection:** Complex card and hand recognition

## 🤝 Contributing

Feel free to contribute to any of these projects by:
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

## 📝 Notes

- Some projects require additional dataset downloads (links provided in respective project folders)
- Video files and some model weights may need to be downloaded separately
- Environment files are provided for reproducible setups
- Each project includes detailed notebooks with step-by-step explanations

## 📧 Contact

For questions, suggestions, or collaboration opportunities, please feel free to reach out!

---

**Happy Learning and Coding! 🚀**
