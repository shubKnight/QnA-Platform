import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#testing dataset
dataset = [
    {"user": "Alice", "question": "Why is my neural network not converging?", "domain": "AI/ML",
     "answer": "Check your learning rate, initialization, and data normalization."},
    {"user": "Bob", "question": "How to deploy a React app with Flask backend?", "domain": "Web",
     "answer": "You can serve the React build folder as static files in Flask or use a reverse proxy like Nginx."},
    {"user": "Charlie", "question": "What is backpropagation in neural networks?", "domain": "AI/ML",
     "answer": "Backpropagation is the process of computing gradients to update weights during training."},
    {"user": "Dave", "question": "How can I connect Arduino to a motor driver?", "domain": "Electronics",
     "answer": "Use the motor driver inputs connected to Arduino PWM pins and power supply properly."},
    {"user": "Eve", "question": "How does dropout prevent overfitting in neural networks?", "domain": "AI/ML",
     "answer": "Dropout randomly drops units during training, preventing co-adaptation and improving generalization."},
    {"user": "Frank", "question": "How do I style a button in CSS?", "domain": "Web",
     "answer": "You can use the CSS :hover pseudo-class and properties like background-color, border, and padding."},
    {"user": "Grace", "question": "What is gradient descent?", "domain": "AI/ML",
     "answer": "Gradient descent is an optimization algorithm that updates parameters to minimize loss."},
    {"user": "Heidi", "question": "How to handle user authentication in a Django app?", "domain": "Web",
     "answer": "Use Django’s built-in authentication system with User model and sessions."},
]


df = pd.DataFrame(dataset)
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['question'])

def get_similar_questions(new_question, top_k=3):
    new_vec = vectorizer.transform([new_question])
    similarities = cosine_similarity(new_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[::-1][:top_k]
    results = df.iloc[top_indices].copy()
    results['similarity'] = similarities[top_indices]
    return results


query = "Why is my CNN not learning properly?"
print(get_similar_questions(query, top_k=3))
