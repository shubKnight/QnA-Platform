import numpy as np
from sentence_transformers import SentenceTransformer, util

#loading pretrained model for semantic searching.
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded successfully!")

#testing dataset
qa_dataset = [
    {
        "question": "Why is my neural network not converging?",
        "answer": "Check your learning rate. If it's too high, the loss might oscillate or diverge. Also, verify your data normalization.",
        "domain": "AI/ML"
    },
    {
        "question": "How do I fix a 'CORS policy' error in my React app?",
        "answer": "You need to configure your backend server to include the correct 'Access-Control-Allow-Origin' header.",
        "domain": "Web Development"
    },
    {
        "question": "My model's loss is stuck and not decreasing. What should I do?",
        "answer": "A stagnant loss could mean your learning rate is too low or the model lacks complexity. Try a different optimizer like Adam.",
        "domain": "AI/ML"
    },
    {
        "question": "What is the best way to manage state in a large React application?",
        "answer": "For large applications, consider using a state management library like Redux Toolkit or Zustand for centralized and predictable state.",
        "domain": "Web Development"
    },
    {
        "question": "How can I prevent my training from overfitting?",
        "answer": "Techniques to prevent overfitting include regularization (L1/L2), dropout, and using more training data or data augmentation.",
        "domain": "AI/ML"
    }
]

#fix to be implemented further: needed to be done once and store it for the furtherrr use....
print("\nGenerating embeddings for the dataset...")
corpus_questions = [item['question'] for item in qa_dataset]
corpus_embeddings = model.encode(corpus_questions, convert_to_tensor=True)
print("Embeddings generated.")


def find_semantic_matches(new_question: str, top_k=3):
    """
    Finds the most semantically similar questions from the dataset.
    """
    print(f"\nSearching for questions similar to: '{new_question}'")
    

    new_question_embedding = model.encode(new_question, convert_to_tensor=True)
    

    cosine_scores = util.cos_sim(new_question_embedding, corpus_embeddings)[0]
    
    top_results = np.argpartition(-cosine_scores, range(top_k))[0:top_k]

    print(f"\nTop {top_k} most similar questions found:\n")
    

    for idx in top_results:
        score = cosine_scores[idx].item()
        matched_question = qa_dataset[idx]['question']
        matched_answer = qa_dataset[idx]['answer']
        
        print(f"   Match Found (Score: {score:.4f})")
        print(f"   Similar Question: {matched_question}")
        print(f"   Existing Answer: {matched_answer}\n")



if __name__ == "__main__":

    student_question = "guide me about website backend training"
    
    find_semantic_matches(student_question)
