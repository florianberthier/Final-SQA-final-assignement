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