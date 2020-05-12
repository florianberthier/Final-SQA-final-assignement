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