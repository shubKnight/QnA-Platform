
from sentence_transformers import SentenceTransformer, util
import numpy as np


embedding_model = SentenceTransformer('all-MiniLM-L6-v2')


def get_all_questions_from_db(db_connection):

    return [
        {
            "id": 1,
            "question_text": "Why is my neural network not converging?",
            "answer_text": "Check your learning rate. If it's too high, the loss might oscillate or diverge.",
            "embedding": embedding_model.encode("Why is my neural network not converging?")
        },
        {
            "id": 2,
            "question_text": "How do I fix a 'CORS policy' error in my React app?",
            "answer_text": "You need to configure your backend server to include the correct 'Access-Control-Allow-Origin' header.",
            "embedding": embedding_model.encode("How do I fix a 'CORS policy' error in my React app?")
        },
        {
            "id": 3,
            "question_text": "My model's loss is stuck. What should I do?",
            "answer_text": "A stagnant loss could mean your model is too simple or the learning rate is too low. Try increasing model complexity or the learning rate.",
            "embedding": embedding_model.encode("My model's loss is stuck. What should I do?")
        }
    ]


def find_similar_qa_for_rag(new_question: str, db_connection, top_k=3):
    """
    Finds similar question-answer pairs from the database to use as context for RAG.
    """

    all_questions = get_all_questions_from_db(db_connection)
    existing_embeddings = np.array([q["embedding"] for q in all_questions])


    new_question_embedding = embedding_model.encode(new_question)


    cosine_scores = util.cos_sim(new_question_embedding, existing_embeddings)[0]


    top_results_indices = np.argpartition(cosine_scores, -top_k)[-top_k:]
    

    similar_qa_pairs = []
    for idx in top_results_indices:
        if cosine_scores[idx] > 0.6: 
            similar_qa_pairs.append({
                "question": all_questions[idx]["question_text"],
                "answer": all_questions[idx]["answer_text"],
                "score": cosine_scores[idx].item()
            })


    similar_qa_pairs.sort(key=lambda x: x["score"], reverse=True)
    
    return similar_qa_pairs

new_student_question = "My neural network loss is not decreasing. What is wrong?"


db_conn = "your_database_connection_object" 


context_for_rag = find_similar_qa_for_rag(new_student_question, db_conn)


print(f"New Question: {new_student_question}\n")
print("--- Found Similar Questions for RAG Context ---")
for item in context_for_rag:
    print(f"Similarity Score: {item['score']:.2f}")
    print(f"Similar Question: {item['question']}")
    print(f"Similar Answer: {item['answer']}\n")
