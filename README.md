
# Email/SMS Spam Classifier

This project is an Email/SMS Spam Classifier built using **Natural Language Processing (NLP)** and **Streamlit**. The model classifies input email or SMS messages as either "Spam" or "Not Spam." It uses text preprocessing, vectorization, and a machine learning model to predict the category of the message.

## Features

- **Text Preprocessing**: The application processes input text by converting it to lowercase, tokenizing, removing punctuation, and filtering out stopwords. The text is then stemmed using the **Porter Stemmer** algorithm.
- **Model**: The classifier uses a **Multinomial Naive Bayes** model, trained on a dataset of labeled emails/SMS messages to predict whether a message is spam or not.
- **Streamlit Interface**: The app provides a simple web interface where users can input a message, click a button to get the prediction, and see the result instantly.

## Libraries & Technologies Used

- **Python**: The main programming language.
- **Streamlit**: For creating the web interface.
- **Scikit-learn**: Used for machine learning and vectorization.
- **NLTK**: For text processing, including tokenization, stopword removal, and stemming.
- **Pickle**: For loading the pre-trained model and vectorizer.

## Requirements

To run this application locally, you need to install the required dependencies. You can install them using the following command:

```bash
pip install -r requirements.txt
```

Here’s the content of the `requirements.txt` file:

```
streamlit
nltk
scikit-learn
pandas
numpy
```

## How to Use

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/your-username/spam-classifier
   cd spam-classifier
   ```

2. Download the necessary NLTK resources:
   ```python
   import nltk
   nltk.download('stopwords')
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. The app will open in your browser. Enter an email or SMS in the input box and click **"Predict"** to see if the message is spam or not.

## How It Works

1. **Text Preprocessing**: When a user inputs a message, the text is preprocessed by converting it to lowercase, tokenizing the text, removing punctuation, eliminating stopwords, and stemming the words.
2. **Vectorization**: The processed text is then vectorized using a `TF-IDF` vectorizer to convert the text into a numerical format that the model can understand.
3. **Prediction**: The vectorized input is passed to the pre-trained **Multinomial Naive Bayes** model, which predicts whether the input text is spam or not.
4. **Result Display**: Based on the model's prediction, the result is displayed as either **Spam** or **Not Spam** on the interface.

## Model and Vectorizer Files

The model and vectorizer used in this app are saved as `mnb.pkl` (model) and `vectorizer.pkl` (vectorizer). These files are loaded using **pickle** and are required for the app to function properly.

## Example

- Input: "Congratulations! You've won a free gift. Claim it now!"
- Output: **Spam**

- Input: "Hey, are we meeting tomorrow?"
- Output: **Not Spam**
