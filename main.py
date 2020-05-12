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

    def CreateSurvey(self, surveyName):
        self.surveyList.append(Survey(surveyName))
        return None

    def GetSurvey(self, surveyName):
        for survey in self.surveyList:
            if survey.name == surveyName:
                return survey
        return "Survey not found"

    def GetSurveys(self):
        return self.surveyList
