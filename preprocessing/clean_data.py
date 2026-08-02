import pandas as pd
import re

# Load dataset
data = pd.read_csv("dataset/darkweb_threat_dataset_1000_rows_unlabeled.csv")

# Function to clean text
def clean_text(text):

    text = text.lower()  # convert to lowercase

    text = re.sub(r'[^a-zA-Z\s]', '', text)  # remove numbers and symbols

    return text

# Apply cleaning
data["clean_text"] = data["text"].apply(clean_text)


# -----------------------------
# Keyword Detection Step
# -----------------------------

# List of threat keywords
keywords = [
    "password",
    "database",
    "leak",
    "hack",
    "ransomware",
    "dump",
    "exploit",
    "credentials",
    "credit",
    "card"
]

# Function to detect suspicious keywords
def keyword_detection(text):

    for word in keywords:

        if word in text:
            return "suspicious"

    return "normal"


# Apply keyword detection
data["keyword_flag"] = data["clean_text"].apply(keyword_detection)


# Show output
print(data.head())