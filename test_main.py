from main import Controller

def test_get_survey():
    MySurveys = Controller()
    MySurveys.CreateSurvey("Survey Test")
    MySurveys.CreateSurvey("Survey Test 2")
    assert MySurveys.GetSurvey("Survey Test").name == "Survey Test"
    assert MySurveys.GetSurvey("Survey Test 2").name == "Survey Test 2"
    assert MySurveys.GetSurvey("No survey") == "Survey not found"

def test_create_survey():
    MySurveys = Controller()
    surveys = MySurveys.GetSurveys()
    assert len(surveys) == 0
    assert MySurveys.CreateSurvey("Survey Test 7") == None
    surveys = MySurveys.GetSurveys()
    assert len(surveys) == 1
    assert surveys[0].name == "Survey Test 7"
    assert MySurveys.CreateSurvey("Survey Test 8") == None
    surveys = MySurveys.GetSurveys()
    assert len(surveys) == 2
    assert surveys[1].name == "Survey Test 8"

def test_get_surveys():
    MySurveys = Controller()
    surveys = MySurveys.GetSurveys()
    assert len(surveys) == 0
    MySurveys.CreateSurvey("Survey Test 3")
    MySurveys.CreateSurvey("Survey Test 4")
    surveys = MySurveys.GetSurveys()
    assert len(surveys) == 2
    MySurveys.CreateSurvey("Survey Test 5")
    MySurveys.CreateSurvey("Survey Test 6")
    surveys = MySurveys.GetSurveys()
    assert len(surveys) == 4

def test_add_question():
    MySurveys = Controller()
    MySurveys.CreateSurvey("Survey Test 9")
    assert len(MySurveys.GetSurvey("Survey Test 9").questions) == 0
    assert MySurveys.AddQuestion("Survey Test 9", "This is a question") == None
    assert MySurveys.AddQuestion("Survey Test 9", "This is a question") == "Question already exist if this survey"
    assert len(MySurveys.GetSurvey("Survey Test 9").questions) == 1
    assert MySurveys.GetSurvey("Survey Test 9").questions[0] == "This is a question"
    assert MySurveys.AddQuestion("Survey Test 9", "This is a question 2") == None
    assert len(MySurveys.GetSurvey("Survey Test 9").questions) == 2
    assert MySurveys.GetSurvey("Survey Test 9").questions[1] == "This is a question 2"
    assert MySurveys.AddQuestion("Unknow Survey", "This is a question") == "Survey not found"
    MySurveys.CreateSurvey("Survey Test 10")
    assert MySurveys.AddQuestion("Survey Test 10", "This is a question for survey 2") == None
    assert len(MySurveys.GetSurvey("Survey Test 9").questions) == 2
    assert len(MySurveys.GetSurvey("Survey Test 10").questions) == 1
    assert MySurveys.GetSurvey("Survey Test 10").questions[0] == "This is a question for survey 2"
    assert MySurveys.AddQuestion("Survey Test 10", "This is a question 10 for survey 10") == None
    assert MySurveys.AddQuestion("Survey Test 10", "This is a question 101 for survey 10") == None
    assert MySurveys.AddQuestion("Survey Test 10", "This is a question 102 for survey 10") == None
    assert MySurveys.AddQuestion("Survey Test 10", "This is a question 103 for survey 10") == None
    assert MySurveys.AddQuestion("Survey Test 10", "This is a question 104 for survey 10") == None
    assert MySurveys.AddQuestion("Survey Test 10", "This is a question 105 for survey 10") == None
    assert MySurveys.AddQuestion("Survey Test 10", "This is a question 106 for survey 10") == None
    assert MySurveys.AddQuestion("Survey Test 10", "This is a question 107 for survey 10") == None
    assert MySurveys.AddQuestion("Survey Test 10", "This is a question 108 for survey 10") == None
    assert MySurveys.AddQuestion("Survey Test 10", "This is a question 109 for survey 10") == "Limit of 10 questions reached"

def test_add_response():
    firstUser = 1
    secondUser = 2
    MySurveys = Controller()
    MySurveys.CreateSurvey("Survey Test 11")
    assert len(MySurveys.GetSurvey("Survey Test 11").responses) == 0
    assert MySurveys.AddResponse("Survey Test 11", 2, firstUser) == "No question for this answer"
    assert MySurveys.AddResponse("Survey Test 11", "invalid response", firstUser) == "Invalid answer"
    assert MySurveys.AddResponse("Survey Test 11", 10, firstUser) == "Invalid answer"
    assert MySurveys.AddResponse("Survey Test 11", 0, firstUser) == "Invalid answer"
    assert MySurveys.AddQuestion("Survey Test 11", "This is a question for survey 1") == None
    assert len(MySurveys.GetSurvey("Survey Test 11").questions) == 1

    assert MySurveys.AddResponse("Unknow Survey 2", 4, firstUser) == "Survey not found"
    assert MySurveys.AddResponse("Survey Test 11", 4, firstUser) == None
    assert len(MySurveys.GetSurvey("Survey Test 11").responses) == 1
    assert MySurveys.GetSurvey("Survey Test 11").responses[0].answer[0] == 4
    assert MySurveys.AddResponse("Survey Test 11", 4, firstUser) == "No question for this answer"

    assert MySurveys.AddQuestion("Survey Test 11", "This is a question 2 for survey 1") == None
    assert len(MySurveys.GetSurvey("Survey Test 11").questions) == 2

    assert MySurveys.AddResponse("Survey Test 11", 1, firstUser) == None
    assert len(MySurveys.GetSurvey("Survey Test 11").responses[0].answer) == 2
    assert MySurveys.GetSurvey("Survey Test 11").responses[0].answer[1] == 1

    assert MySurveys.AddResponse("Survey Test 11", 3, secondUser) == None
    assert len(MySurveys.GetSurvey("Survey Test 11").responses) == 2
    assert len(MySurveys.GetSurvey("Survey Test 11").responses[1].answer) == 1
    assert len(MySurveys.GetSurvey("Survey Test 11").responses[0].answer) == 2
    assert MySurveys.GetSurvey("Survey Test 11").responses[1].answer[0] == 3

    assert MySurveys.AddResponse("Survey Test 11", 4, secondUser) == None
    assert len(MySurveys.GetSurvey("Survey Test 11").responses) == 2
    assert len(MySurveys.GetSurvey("Survey Test 11").responses[1].answer) == 2
    assert len(MySurveys.GetSurvey("Survey Test 11").responses[0].answer) == 2
    assert MySurveys.GetSurvey("Survey Test 11").responses[1].answer[1] == 4

    MySurveys.CreateSurvey("Survey Test 12")
    assert MySurveys.AddQuestion("Survey Test 12", "This is a question for survey 1") == None
    assert len(MySurveys.GetSurvey("Survey Test 12").questions) == 1

    assert MySurveys.AddResponse("Survey Test 12", 2, firstUser) == None
    assert len(MySurveys.GetSurvey("Survey Test 11").responses) == 2
    assert len(MySurveys.GetSurvey("Survey Test 11").responses[1].answer) == 2
    assert len(MySurveys.GetSurvey("Survey Test 11").responses[0].answer) == 2
    assert MySurveys.GetSurvey("Survey Test 11").responses[1].answer[1] == 4
    assert len(MySurveys.GetSurvey("Survey Test 12").responses[0].answer) == 1
    assert MySurveys.GetSurvey("Survey Test 12").responses[0].answer[0] == 2

def test_get_survey_stat():
    firstUser = 1
    secondUser = 2
    MySurveys = Controller()
    MySurveys.CreateSurvey("Survey Test 13")
    assert MySurveys.AddQuestion("Survey Test 13", "This is a question for survey 1") == None
    assert MySurveys.AddQuestion("Survey Test 13", "This is a question 2 for survey 1") == None
    assert len(MySurveys.GetSurvey("Survey Test 13").questions) == 2

    surveyStat = MySurveys.GetSurveyStat("Survey Test 13")
    assert MySurveys.GetSurveyStat("Unknow Survey") == "Survey not found"
    assert surveyStat == {}

    assert MySurveys.AddResponse("Survey Test 13", 4, firstUser) == None
    assert MySurveys.AddResponse("Survey Test 13", 2, firstUser) == None

    surveyStat = MySurveys.GetSurveyStat("Survey Test 13")
    assert surveyStat["max"] == 6
    assert surveyStat["min"] == 6
    assert surveyStat["average"] == 6

    assert MySurveys.AddResponse("Survey Test 13", 1, secondUser) == None
    assert MySurveys.AddResponse("Survey Test 13", 2, secondUser) == None

    surveyStat = MySurveys.GetSurveyStat("Survey Test 13")
    assert surveyStat["max"] == 6
    assert surveyStat["min"] == 3
    assert surveyStat["average"] == 4.5
    assert surveyStat["stand_dev"] == 2.1213203435596424

    MySurveys.CreateSurvey("Survey Test 14")
    assert MySurveys.AddQuestion("Survey Test 14", "This is a question for survey 1") == None
    assert MySurveys.AddQuestion("Survey Test 14", "This is a question 2 for survey 1") == None
    assert len(MySurveys.GetSurvey("Survey Test 14").questions) == 2
    assert MySurveys.AddResponse("Survey Test 14", 4, firstUser) == None
    assert MySurveys.AddResponse("Survey Test 14", 2, firstUser) == None