# Mini Answer Evaluator

A simple AI-powered answer evaluation system using rubric retrieval + Llama 2 via Ollama.

## Objective
Build a system that:
- Accepts a question
- Accepts a student answer
- Retrieves a relevant rubric
- Uses Llama 2 to evaluate the answer
- Returns marks, feedback, and justification in JSON format

## Project Structure
mini-answer-evaluator/
- app.py
- rubric.py
- utils.py
- evaluator.py
- requirements.txt
- prompt_used.txt
- README.md

## Setup

### 1. Install Ollama
Download from https://ollama.com

Run:
ollama run llama2

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run project
python app.py

## Features
- Local LLM (no API key needed)
- Rubric-based grading
- Structured JSON output
- Simple CLI workflow

## Future Improvements
- Streamlit UI
- Embeddings-based rubric retrieval
- Evaluation history
