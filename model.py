import json

class Question(object):
    """This is the structure of any question in quiz"""

    # Instance variables
    id = None
    type = None
    question = None
    answer = None
    explanation = None
    solved = False

    def __init__(self, id, type, question, answer, explanation):
        """Initializing instance variables by passing each of them"""
        self.id = id
        self.type = type
        self.question = question
        self.answer = answer
        self.explanation = explanation
