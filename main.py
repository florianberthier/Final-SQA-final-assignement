from statistics import stdev

def GetSurveyStatistics(survey):
    result = dict()
    total = 0
    size = 0
    minVal = 10
    maxVal = 0
    scores = []

    for response in survey.responses:
        score = 0
        for answer in response.answer:
            score = score + answer
        if score > maxVal:
            maxVal = score
        if score < minVal:
            minVal = score
        total = total + score
        size = size + 1
        scores.append(score)

    if len(scores) > 1:
        result["stand_dev"] = stdev(scores)
    if size > 0:
        result["average"] = total / size
        result["min"] = minVal
        result["max"] = maxVal
    return result

def GetSurveyQuestionStatistics(survey, position):
    result = dict()
    total = 0
    size = 0
    minVal = 10
    maxVal = 0
    scores = []

    for response in survey.responses:
        questionPos = 0
        score = 0
        for answer in response.answer:
            if questionPos == position:
                score = answer
                break
            questionPos = questionPos + 1
        if score == 0:
            continue
        if score > maxVal:
            maxVal = score
        if score < minVal:
            minVal = score
        total = total + score
        size = size + 1
        scores.append(score)

    if len(scores) > 1:
        result["stand_dev"] = stdev(scores)
    if size > 0:
        result["average"] = total / size
        result["min"] = minVal
        result["max"] = maxVal
    return result

class SurveyResponse:
    def __init__(self, user):
        self.user = user
        self.answer = []
    
    def AddAnswer(self, answer, nbQuestions):
        if isinstance(answer, int) == False:
            return "Invalid answer"
        if answer < 1 or answer > 5:
            return "Invalid answer"
        if len(self.answer) + 1 > nbQuestions:
            return "No question for this answer"
        self.answer.append(answer)

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
    
    def GetResponses(self):
        result = []
        for response in self.responses:
            result.append(response.answer)
        return result

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

    def GetSurveyResponses(self, surveyName):
        for survey in self.surveyList:
            if survey.name == surveyName:
                return survey.GetResponses()
        return "Survey not found"

    def GetSurveyStat(self, surveyName):
        for survey in self.surveyList:
            if survey.name == surveyName:
                return GetSurveyStatistics(survey)
        return "Survey not found"

    def GetSurveyQuestionStat(self, surveyName, question):
        position = 0

        for survey in self.surveyList:
            if survey.name == surveyName:
                for surveyQuestion in survey.questions:
                    if surveyQuestion == question:
                        return GetSurveyQuestionStatistics(survey, position)
                    position = position + 1
                return "Survey Question not found"
        return "Survey not found"
