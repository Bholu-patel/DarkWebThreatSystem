import pandas as pd
import re
import pickle
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# -------------------------
# Load dataset
# -------------------------

dataset_path = "dataset/labeled_threat_dataset.csv"

if os.path.exists(dataset_path):
    data = pd.read_csv(dataset_path)
else:
    data = pd.read_csv("dataset/darkweb_threat_dataset_1000_rows_unlabeled.csv")


    # -------------------------
    # Clean Text
    # -------------------------

    def clean_text(text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text


    data["clean_text"] = data["text"].apply(clean_text)


    # -------------------------
    # Create Labels
    # -------------------------

    def assign_label(text):

        high_words = ["password", "database", "credit", "card", "dump", "credentials"]
        medium_words = ["hack", "exploit", "vulnerability", "ransomware"]

        for word in high_words:
            if word in text:
                return "High"

        for word in medium_words:
            if word in text:
                return "Medium"

        return "Low"


    data["label"] = data["clean_text"].apply(assign_label)


    # Save labeled dataset
    data.to_csv(dataset_path, index=False)

    print("Labeled dataset saved successfully!")


# -------------------------
# Feature Extraction (TF-IDF)
# -------------------------

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(data["clean_text"])

y = data["label"]


# -------------------------
# Train Test Split
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# -------------------------
# Train Machine Learning Model
# -------------------------

model = MultinomialNB()

model.fit(X_train, y_train)


# -------------------------
# Evaluate Model
# -------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)


# -------------------------
# Save Model & Vectorizer
# -------------------------

pickle.dump(model, open("ml_model/model.pkl", "wb"))
pickle.dump(vectorizer, open("ml_model/vectorizer.pkl", "wb"))

print("Model and vectorizer saved successfully!")


# -------------------------
# Test the Model
# -------------------------

sample = ["selling 10000 bank passwords"]

sample_vector = vectorizer.transform(sample)

prediction = model.predict(sample_vector)

print("Sample Input:", sample)
print("Predicted Threat Level:", prediction)