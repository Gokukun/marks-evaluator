from utils import get_rubric
from evaluator import evaluate_answer

def main():
    question = input("Enter Question: ")
    answer = input("Enter Student Answer: ")

    rubric = get_rubric(question)

    print("\n Retrieved Rubric:\n", rubric)

    result = evaluate_answer(question, answer, rubric)

    print("Evaluation Result:")
    print(result)

if __name__ == "__main__":
    main()