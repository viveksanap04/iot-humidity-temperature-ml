# 🌡️ Temperature & Humidity Prediction Using Machine Learning

**An IoT + Machine Learning project exploring how historical environmental data duration influences temperature and humidity prediction performance.**

## 📌 Project Overview

This project focuses on collecting real-time temperature and humidity data using an **ESP32 microcontroller and DHT22 sensor**, storing sensor readings in **Firebase Realtime Database**, and applying Machine Learning techniques to predict future environmental conditions.

The project follows a three-phase experimental approach based on different durations of historical data:

1. **Phase 1:** 1-Day Dataset
2. **Phase 2:** 7-Day Dataset
3. **Phase 3:** 30-Day Dataset

The primary goal is to investigate whether increasing the duration of historical data improves prediction accuracy and how changing environmental conditions affect model performance.

---

## 🎯 Project Objectives

- Collect real-time temperature and humidity readings using IoT hardware.
- Store sensor data with timestamps in Firebase.
- Perform Data Analytics and Exploratory Data Analysis (EDA).
- Apply traditional Machine Learning regression algorithms.
- Compare model performance across different dataset durations.
- Understand the impact of changing environmental conditions on predictions.
- Evaluate model performance using MAE, MSE, RMSE and R².
- Identify the limitations of traditional regression models for environmental prediction.

---

## 🛠️ Technology Stack

| Category           | Technologies                            |
| ------------------ | --------------------------------------- |
| Hardware           | ESP32, DHT22 Sensor                     |
| Programming        | Python                                  |
| Database           | Firebase Realtime Database              |
| Data Processing    | Pandas, NumPy                           |
| Data Visualization | Matplotlib, Seaborn                     |
| Machine Learning   | Scikit-learn                            |
| Development        | Jupyter Notebook, Google Colab, VS Code |
| Version Control    | Git, GitHub                             |

---

## 📊 Three-Phase Experimental Approach

### Phase 1 — 1-Day Dataset

\<details> \<summary>\<strong>Data Collection Details\</strong>\</summary>

- Location: Kharghar, Sector 3, Navi Mumbai, Maharashtra, India
- Collection point: Outdoor environment outside my flat
- Start: 1 November 2026, 00:09:28
- End: 2 November 2026, 02:22:41
- Dataset size: Approximately 45,000 records
- Status: Data collection completed

\</details>

**Current Work: Data Analytics & Machine Learning**

- Data cleaning and preprocessing.
- Exploratory Data Analysis.
- Understanding temperature and humidity distributions.
- Identifying patterns and trends.
- Experimenting with traditional regression algorithms.
- Evaluating prediction performance.

### Phase 2 — 7-Day Dataset

\<details> \<summary>\<strong>Data Collection Details\</strong>\</summary>

- Collection started: 16 November 2026
- Expected completion: 24 November 2026
- Duration: Approximately 7–8 calendar days, depending on the exact collection cutoff.
- Status: Data collection in progress

\</details>

**Planned Work:**

- Continue continuous real-time sensor data collection.
- Build a larger historical dataset.
- Perform Data Analytics and EDA.
- Train and evaluate regression models.
- Compare results with Phase 1.
- Investigate daily environmental variations.

### Phase 3 — 30-Day Dataset

\<details> \<summary>\<strong>Data Collection Details\</strong>\</summary>

- Start: Continuation of Phase 2 data collection.
- Target duration: Approximately 30 days.
- Status: Planned.

\</details>

**Planned Work:**

- Continue collecting data until approximately one month of historical readings is available.
- Perform comprehensive Data Analytics.
- Train regression models using the larger dataset.
- Investigate longer-term environmental patterns.
- Compare prediction performance across all three phases.
- Study how additional historical data influences model generalization.

---

## 🤖 Machine Learning Approach

The initial experiments will focus on traditional regression algorithms.

Potential algorithms:

- Linear Regression
- Polynomial Regression
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors Regressor
- Support Vector Regression

**Evaluation Metrics:**

| Metric   | Purpose                               |
| -------- | ------------------------------------- |
| MAE      | Average absolute prediction error     |
| MSE      | Average squared prediction error      |
| RMSE     | Prediction error in the original unit |
| R² Score | Explained variance in the target      |

The models will be evaluated separately for temperature and humidity prediction.

---

## 📈 Experimental Comparison

The final experiment will compare the three dataset durations.

| Parameter        | Phase 1     | Phase 2          | Phase 3          |
| ---------------- | ----------- | ---------------- | ---------------- |
| Historical data  | 1 day       | 7 days           | 30 days          |
| Records          | \~45,000    | To be determined | To be determined |
| Data Analytics   | In progress | Planned          | Planned          |
| ML Training      | In progress | Planned          | Planned          |
| Model Evaluation | Pending     | Pending          | Pending          |
| Comparison       | Baseline    | Pending          | Pending          |

The final objective is to determine how well models trained on different historical data durations perform on unseen future sensor readings.

---

## 🔍 Key Research Questions

1. Does increasing the historical dataset duration improve prediction accuracy?
2. How do temperature and humidity patterns change throughout different days?
3. Which regression algorithm performs best for temperature prediction?
4. Which regression algorithm performs best for humidity prediction?
5. Can models trained on short-duration data generalize to future environmental conditions?
6. Does a larger dataset always lead to better predictions?

---

## 📂 Project Structure
-----

## 🚧 Current Project Status

**Currently working on Phase 1 Data Analytics and Machine Learning experiments while continuously collecting data for Phase 2.**

This is an ongoing project. Results, visualizations, model comparisons, and observations will be updated as each phase progresses.

---

## 👨‍💻 Author

**Vivek Sanap**

PGCP-AI | C-DAC Mumbai

Interested in Machine Learning, Artificial Intelligence, IoT, and Data Science.

---

⭐ If you find this project interesting, feel free to explore the repository and follow its progress.
