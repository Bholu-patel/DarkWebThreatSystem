# 🛡️ Dark Web Threat Intelligence System

## Overview

The Dark Web Threat Intelligence System is a Machine Learning-based web application that analyzes text related to dark web activities and predicts the threat level. It uses Natural Language Processing (NLP) and a trained machine learning model to classify potentially malicious content.

---

## Features

- Machine Learning-based threat detection
- Text preprocessing and cleaning
- Threat level prediction
- Flask REST API
- Interactive web interface
- Trained ML model using Scikit-learn

---

## Technologies Used

- Python
- Flask
- Flask-CORS
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- JavaScript

---

## Project Structure

```
DarkWebThreatSystem/
│
├── backend/
│   └── app.py
│
├── dataset/
│   ├── darkweb_threat_dataset.csv
│   └── labeled_threat_dataset.csv
│
├── frontend/
│   └── index.html
│
├── ml_model/
│   ├── train_model.py
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── preprocessing/
│   └── clean_data.py
│
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Bholu-patel/DarkWebThreatSystem.git
```

Install dependencies

```bash
pip install flask flask-cors pandas numpy scikit-learn
```

Run the backend

```bash
cd backend
python app.py
```

Open the frontend by opening `frontend/index.html` in your browser.

---

## Future Improvements

- Deep Learning Models
- BERT-based NLP
- Real-time Threat Monitoring
- Dashboard Analytics
- Database Integration
- User Authentication

---

## Author

Bhavya Jivani

---

## License

This project is intended for educational and research purposes.
