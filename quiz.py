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
    for question in question_json[chosen_level]:
        question_input = Question(
            id=question['id'],
            type=question['type'],
            question=question['question'],
            answer=question['answer'],
            explanation=question['explanation']
            )
        questions_list.append(question_input)
    print("Questions have been loaded for {0} level".format(chosen_level))
    return questions_list


def ask_question(current_question):
    """Function to get question in appropriate format
    Args:
        current_question: an instance of question object
    Returns:
        formatted numbered question
    """

    return """
    Question No. {0}:
{1}
    """.format(current_question.id, current_question.question)


def checking_answer(question, ans_input):
    """Function to check if the user's answer is matched to the model answer
    Args:
        question: an instance of question object
        ans_input: a string of the answer entered by user
    Returns:
        boolean whether user's answer matched the model answer
    """

    if question.answer.lower() == ans_input.lower():
        question.solved = True
    return question.solved


def get_explanation(q_list):
    """Function to get explanations of wrongly answered questions
    Args:
        q_list: a list of question instances which is displayed to user
    Returns:
        explanations of incorrectly solved questions
    """

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

    another_question = True
    for question in q_list:
        # in case user wants to continue the quiz when guesses correctly
        if not another_question:
            break
        answer = raw_input(ask_question(question))
        retry = True
        while retry:
            retry = False
            if checking_answer(question, answer):
                # asks user if he wants to get to the next question
                another_question = raw_input("Correct answer, Type 'Y' If you want the next question\n") == 'Y'
            else:
                # asks the user he wants to try again the current question
                retry = raw_input("Wrong Answer, Type 'Y' If you want to try again.\n") == 'Y'

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
