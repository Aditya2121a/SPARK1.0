import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from Head.Mouth import speak

with open(r'C:\Programmes\SPARK 1.0\Data\brain_data\dta.json') as file:
    data = json.load(file)

training_data = []
for intent in data.get('intents', []):
    if 'patterns' in intent:
        for pattern in intent['patterns']:
            training_data.append((pattern, intent['tag']))
    else:
        print(f"Warning: 'patterns' key is missing in intent: {intent}")


if not training_data:
    print("Error: No training data found.")
else:
    X,y = zip(*training_data)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X)
    classifier = MultinomialNB()
    classifier.fit(X, y)

    def get_response(user_input):
        user_input_vectorized = vectorizer.transform([user_input])
        predicted_intent = classifier.predict(user_input_vectorized)[0]
        for intent in data.get('intents', []):
            if intent.get('tag') == predicted_intent:
                responses = intent.get('responses', [])
                if responses:
                    return random.choice(responses)
                else:
                    return "I'm sorry, I don't have a response for that."

