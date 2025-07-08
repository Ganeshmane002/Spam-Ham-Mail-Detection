import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("model.joblib")          # Naive Bayes Model
vectorizer = joblib.load("scaled.joblib")    # Tfidf or CountVectorizer

# App Title
st.title("📨 NB MailGuard - Spam Detection App")
st.markdown("Using **Naive Bayes** to classify messages as **Spam** or **Ham** (Not Spam)")

# User input
message = st.text_area("📬 Enter the message:")

# Predict on click
if st.button("Predict"):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        # Preprocess and predict
        transformed = vectorizer.transform([message])
        result = model.predict(transformed)[0]

        if result == "spam":
            st.error("🚫 This message is SPAM.")
        else:
            st.success("✅ This message is HAM (not spam).")
