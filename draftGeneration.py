import google.generativeai as genai
import os


genai.configure(api_key="YOUR_API_KEY") 


new_question = "My machine learning model's accuracy is not improving. Why?"

retrieved_context = [
    {
        "question": "My model's loss is stuck and not decreasing. What should I do?",
        "answer": "A stagnant loss could mean your learning rate is too low or the model lacks complexity. Try a different optimizer like Adam."
    },
    {
        "question": "Why is my neural network not converging?",
        "answer": "Check your learning rate. If it's too high, the loss might oscillate or diverge. Also, verify your data normalization."
    }
]


def build_rag_prompt(question, context):
    """Builds a prompt for the Gemini model with retrieved context."""
    
    prompt_header = """
    ROLE: You are an expert AI/ML assistant for the Zine Q&A platform.
    TASK: Based ONLY on the context from similar past questions provided below, generate a helpful draft answer for the new student question.
    - Combine the key ideas from the existing answers.
    - Address the student directly with actionable steps.
    - Do not use any information outside of the provided context.
    ---
    """
    
    context_section = "CONTEXT FROM PREVIOUS SIMILAR QUESTIONS:\n"
    for i, item in enumerate(context):
        context_section += f"\n[Similar Question {i+1}]: {item['question']}\n"
        context_section += f"[Existing Answer {i+1}]: {item['answer']}\n"
        
    question_section = f"""
    ---
    NEW QUESTION TO ANSWER:
    "{question}"
    
    DRAFT ANSWER:
    """
    
    return prompt_header + context_section + question_section


final_prompt = build_rag_prompt(new_question, retrieved_context)


print("Prompt Sent to gemingini")
print(final_prompt)

try:
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(final_prompt)
    draft_answer = response.text

    print("\n---  AI-Generated Draft Answer ---")
    print(draft_answer)

except Exception as e:
    print(f"\n---  An error occurred ---")
    print(f"Error: {e}")
    print("Please ensure your API key is configured correctly.")
