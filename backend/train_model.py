import pandas as pd
import nltk
import string
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Download necessary NLTK resources
nltk.download('stopwords')
from nltk.corpus import stopwords

# Load dataset
df = pd.read_csv(r"C:\Users\ashwa\IMDB\IMDB Dataset.csv")

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    return text

# Apply preprocessing
df['review'] = df['review'].apply(preprocess_text)
df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})

# Convert text into numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['review'])
y = df['sentiment']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save Model and Vectorizer
joblib.dump(model, r"C:\Users\ashwa\text-classification\model\text_classifier.pkl")
joblib.dump(vectorizer, r"C:\Users\ashwa\text-classification\model\vectorizer.pkl")

print("Model trained and saved successfully!")
