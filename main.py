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

    def AddQuestion(self, question):
        if len(self.questions) >= 10:
            return "Limit of 10 questions reached"
        for myQuestion in self.questions:
            if myQuestion == question:
                return "Question already exist if this survey"
        self.questions.append(question)

    def AddResponse(self, answer, user):
        for response in self.responses:
            if response.user == user:
                return response.AddAnswer(answer, len(self.questions))
        response = SurveyResponse(user)
        self.responses.append(response)
        return response.AddAnswer(answer, len(self.questions))

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

    def AddQuestion(self, surveyName, question):
        for survey in self.surveyList:
            if survey.name == surveyName:
                return survey.AddQuestion(question)
        return "Survey not found"

    def AddResponse(self, surveyName, response, user):
        for survey in self.surveyList:
            if survey.name == surveyName:
                return survey.AddResponse(response, user)
        return "Survey not found"
