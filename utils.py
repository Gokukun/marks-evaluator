from rubric import rubrics, fallback_rubric

def get_rubric(question):
    question = question.lower()

    for subject in rubrics:
        for keyword in rubrics[subject]["keywords"]:
            if keyword in question:
                return rubrics[subject]["rubric"]

    return fallback_rubric