import ollama
import json
import re

def evaluate_answer(question, answer, rubric):
    prompt = f"""
You are an answer evaluator.

Question: {question}
Student Answer: {answer}

Rubric:
{rubric}

Return ONLY valid JSON:
{{
  "marks_awarded": int,
  "max_marks": 5,
  "feedback": "...",
  "justification": "..."
}}
"""

    response = ollama.chat(
        model="llama2",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response['message']['content']

    
    try:
        result = json.loads(output)
    except:
        json_text = re.search(r'\{.*\}', output, re.DOTALL).group()
        result = json.loads(json_text)

    return result