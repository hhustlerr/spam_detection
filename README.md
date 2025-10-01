# 📩 Spam SMS Detection

A machine learning project that detects whether a given SMS/text message is **Spam** or **Ham (Not Spam)**.  
The project uses Natural Language Processing (NLP) techniques for preprocessing and classification, and is deployed using **Flask**.

---

## 🚀 Features
- Text preprocessing (tokenization, stopword removal, stemming/lemmatization using NLTK).
- TF-IDF Vectorizer for feature extraction.
- Trained ML model stored in `model.pkl`.
- Real-time predictions via a Flask web app (`app.py`).
- Jupyter Notebook (`spam SMS detection.ipynb`) for experiments and training.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x  
- **Libraries:** Scikit-learn, Pandas, NumPy, NLTK, Flask  
- **Environment:** Jupyter Notebook / Google Colab  

---

## 📂 Project Structure
├── .devcontainer/ # Dev environment config

├── app.py # Flask web app

├── model.pkl # Trained ML model

├── vectorizer.pkl # TF-IDF vectorizer

├── requirements.txt # Dependencies

├── set_up.py # Setup script

├── setup_nltk.py # Downloads NLTK resources

├── spam SMS detection.ipynb # Training & testing notebook

└── README.md # Project documentation

## 📊 Model Training

If you want to retrain the model:

- Open spam SMS detection.ipynb in Jupyter/Colab.

- Run all cells to train the model.

- This will generate new model.pkl and vectorizer.pkl files.



