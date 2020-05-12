from statistics import stdev 

class SurveyResponse:
    def __init__(self, user):
        self.user = user
        self.answer = []

class Survey:
    def __init__(self, name):
        self.name = name
        self.questions = []
        self.responses = []

class Controller:
    def __init__(self):
        self.surveyList = []
