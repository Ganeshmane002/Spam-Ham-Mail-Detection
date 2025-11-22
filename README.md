📌 SMS Spam Detection Using Machine Learning

- This project detects whether an SMS message is Spam or Ham (Not Spam) using Natural Language Processing (NLP) and Multinomial Naive Bayes.


🔹 Project Workflow

- Loaded dataset (5572 messages)

- Preprocessed & cleaned text

- Converted text to numerical form using CountVectorizer

- Trained Multinomial Naive Bayes model

- Saved model and vectorizer using joblib

- Built a simple Streamlit web app for prediction


🧪 How to Run the Web App

- pip install -r requirements.txt

- streamlit run app.py


📂 Files Included

- app.py --> Streamlit web interface

- model.joblib --> Trained classification model

- scaled.joblib --> CountVectorizer object

- requirements.txt --> Required Python libraries

🧠 Tech Used: 

- Python, CountVectorizer, Multinomial, Naive Bayes, Streamlit, Joblib

Feel free to fork, enhance, and star the repository!
