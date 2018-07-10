import json
from model import Question


def initialize_quiz(chosen_level):
    """Function to return list of questions of a specific level
    Args:
        chosen_level: String containing selected level (easy, intermediate, hard)
    Returns:
        list of objects
    """

    # parsing questions from a .json file
    with open('numerical_reasoning.json') as f_json:
        question_json = json.load(f_json)

    # appending questions in a list
    questions_list = []
    for q in question_json[chosen_level]:
        question_input = Question(
            id=q['id'],
            type=q['type'],
            question=q['question'],
            answer=q['answer'],
            explanation=q['explanation']
            )
        questions_list.append(question_input)
    print("Questions have been loaded for {0} level".format(chosen_level))
    return questions_list


def ask_question(current_question):
    """Function to get question in appropriate format"""

    return """
    Question No. {0}:
{1}
    """.format(current_question.id, current_question.question)


def checking_answer(question, ans_input):
    """Function to check if the user's answer is matched to the model answer"""

    if question.answer.lower() == ans_input.lower():
        question.solved = True
    return question.solved


def get_explanation(q_list):
    """Function to get explanations of wrongly answered questions"""

    explanation_text = []
    for question in q_list:
        if not question.solved:
            explanation_text.append("""
            Question No. {0} Explanation:
            =============================
{1}
            """.format(question.id, question.explanation))

    return explanation_text


def start_quiz():
    """Function for quiz simulation"""
    difficulty = raw_input("""
    Select your difficulty level:
    (1) Beginner
    (2) Intermediate
    (3) Advanced
    
    Please type the level number.
    
    """)

    # conditional expression for assigning level name instead of a number
    difficulty = "beginner" if difficulty == "1" \
        else "intermediate" if difficulty == "2" \
        else "advanced" if difficulty == "3" \
        else None

    # in case user entered a wrong input
    if not difficulty:
        print("Error! You've entered an invalid input.")

        # restarting quiz
        start_quiz()

        # breaking execution of that wrong input
        return

    print("You have chosen {0} level..".format(difficulty))

    # assigning questions based on level
    q_list = initialize_quiz(difficulty)

    for question in q_list:
        answer = raw_input(ask_question(question))
        if checking_answer(question, answer):
            print("Correct answer")
        else:
            print("Wrong answer")

    explanation_result = get_explanation(q_list)

    num_wrong = len(explanation_result)
    num_correct = len(q_list) - num_wrong
    score = num_correct / len(q_list) * 100

    print("""
    Quiz has been ended...
    
    Results
    =======
    Correct Answers: {0}
    Wrong Answers: {1}
    Score: {2}
    """.format(num_correct, num_wrong, score))

    show_explanation = raw_input("Do you want to show explanations of wrong answered questions? (Y/N)")
    if show_explanation == 'Y':
        for explanation in explanation_result:
            print(explanation)


if __name__ == '__main__':
    start_quiz()