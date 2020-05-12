# SQA-final-assignement

## Introduction

Today's software applications are increasingly complex, often operating in multi-layer and multi-platform environments, and built in fast and agile conditions with ambitious requirements. In this complex scenario, software quality assurance and testing becomes even more critical as a means of **improving quality** and **minimizing risk**, responding to market demands and business needs. We are going to go through all these good practices through a sample project. This project is a software component in **Python** to store information about surveys and responses. The project is available in the repository where this document can be found. This document is a reference guide for best practices. The purpose of this document is to show the best practices to be adopted in the development of a project. This document covers the following themes : 

- [**Sprint backlog and task estimation**](#sprint-backlog-and-task-estimation)

- [**Project Documentation**](#project-documentation)

- [**Unit testing and Test-Driven development**](#unit-testing-and-test-driven-development)

- [**Test coverage metric**](#test-coverage-metric)

- [**Team version-control**](#team-version-control)

- [**Code-review checklist**](#code-review-checklist)

## Sprint backlog and task estimation

1. Project structure
Imagine and create the structure of the project with all the classes and variables that will have to be present for the project. Time: **2 hours**.

2. Create a survey
Create the survey creation method. Of course, like every other part, you have to integrate the tests. Time: **25 min**.

3. Get a survey
Retrieve a survey by sending the name of the survey. Of course, like every other part, you have to integrate the tests. Time: **15 min**.

4. Get all surveys
Retrieve all survey. Of course, like every other part, you have to integrate the tests. Time: **15 min**.

5. Add a question to a survey
Add a question to a survey by sending the name of the survey and the question. No more than 10 questions per survey. Of course, like every other part, you have to integrate the tests. Time: **40 min**.

6. Add a response to a survey
Add a response to a survey by sending the name of the survey, the response and a userID.  It should not be possible to add an answer if there is no associated question. The answer must be a number between 1 and 5. Answers must be stored in relation to the user ID. Of course, like every other part, you have to integrate the tests. Time: **60 min**.

7. Get a survey statistics
Calculate and return the statistics of a survey. The statistics include a min, max, mean and standard deviation. Of course, like every other part, you have to integrate the tests. Time: **35 min**.

8. Get a question statistics
Calculate and return the statistics of a survey question. The statistics include a min, max, mean and standard deviation. Of course, like every other part, you have to integrate the tests. Time: **20 min**.

Estimating the duration of a task can be difficult. In the case of this project, the first task is one that will require more reflection than the others. The challenge of this task is to think carefully about the structure of the project and to code a solid foundation. The time allowed may seem long, but it is time to save for the next tasks. It is better to spend more time thinking and less time coding. Contrary to this task, the next 3 tasks should not take too much time. It is simply a matter of returning known values. However, you have to take into account the time needed to create the tests. The last two tasks have a different time estimation because we will be able to reuse the code from the last but one task in the last one.

One of the interesting metrics to calculate in scrum is velocity metrics. Velocity refers to the average amount of work a Scrum team performs during a sprint. Measured in story points or hours, it is very useful for forecasting. It is important to monitor the evolution of velocity over time. New teams can expect this velocity to increase as relationships and work processes are optimized. Existing teams can monitor their velocity to ensure consistency of performance over time and check whether or not a particular process change has led to improvements. A drop in average velocity is usually a sign that part of the team's development process has become inefficient and should be addressed in the next review. Thus, in the next sprint, improvements can be made to re-increase this metric. Velocity is unique for each team. If team A has a velocity of 50 and team B has a velocity of 75, it does not mean that team B has a higher velocity. The velocity is therefore only used to compare with yourself. 

## Project Documentation

All the functionalities of the project are achievable via the Controller class. The Controller class consists of 7 functions. To be able to use this class, it must first be initialized:
```
    MySurveys = Controller()
```
You can then call up the available functions of the controller via this new variable.

- **CreateSurvey, create a new survey**. You have the possibility to create several surveys. To do this you must call the CreateSurvey function:
```
    MySurveys.CreateSurvey("My new survey name")
```

OUTPUT:

    - None, if it works

- **GetSurveys, get the list of all created surveys**. You can also retrieve all created surveys via the GetSurveys function:
```
    allMySurveys = MySurveys.GetSurveys()
```

OUTPUT:

    - Array of Class Survey

- **GetSurvey, get a specific survey**. You can also retrieve a specific survey via the GetSurvey function by sending it the name of the survey you want to retrieve:
```
    mySurvey = MySurveys.GetSurvey("My new survey name")
```

OUTPUT:

    - Class Survey, if it works
    - "Survey not found", if the survey name is unknown

- **AddQuestion, add a question to a specific survey**. You can add questions to your survey via the AddQuestion function by sending it the name of the survey and the question. A survey is limited to a maximum of 10 questions:
```
    MySurveys.AddQuestion("My new survey name", "My question")
```

OUTPUT:

    - None, if it works
    - "Survey not found", if the survey name is unknown
    - "Question already exist if this survey", if the question is already associated to this survey
    - "Limit of 10 questions reached", if the survey's question limit is reached (10 questions)

- **AddResponse, add a response to a specific survey**. You can add responses to your survey via the AddResponse function by sending it the name of the survey and the response. The response must be a number between 1 and 5. You cannot add answers if there are no questions in your survey. You also need to send a user ID to be able to differentiate the answers between each person:
```
    MySurveys.AddResponse("My new survey name", 2[response], 1[userID])
```

OUTPUT:

    - None, if it works
    - "Survey not found", if the survey name is unknown
    - "No question for this answer", if there are less questions than response for this user
    - "Invalid answer", if the answer is not valid (between 1 and 5)

- **GetSurveyStat, get the survey's statistics**. You can retrieve the statistics of a specific survey by using the GetSurveyStat function and sending it the name of the survey. The statistics include the min score, max score, average score and standard deviation of the scores. A survey score is obtained by summing all the responses of a user: 
```
    mySurveyStat = MySurveys.GetSurveyStat("My new survey name")
```

OUTPUT:

    - Object of statistics, if it works (max, min, average, stand_dev)
    - "Survey not found", if the survey name is unknown

- **GetSurveyQuestionStat, get the survey's statistics**. You can retrieve the statistics of a specific question in a survey by using the GetSurveyQuestionStat function and sending it the name of the survey and the question. The statistics include the min score, max score, average score and standard deviation of the scores. A score is the response of the question by the user: 
```
    myQuestionStat = MySurveys.GetSurveyQuestionStat("My new survey name", "My question")
```

OUTPUT:

    - Object of statistics, if it works (max, min, average, stand_dev)
    - "Survey not found", if the survey name is unknown
    - "Survey Question not found", if the question is unknown for this survey


## Unit testing and Test-Driven development

Testing is the basis of a successful project. It is imperative that you provide tests for each of your code additions. The tests must be complete, i.e. test all possible cases. The name of the test should be the same as the name of the function being tested to simplify the work of other developers. In our example project, the basic python tool py.test is used. To start the test series, run the command:
```
    py.test
```
If you get red after typing the command, it means that there is an error in the code or in the test. So it's up to you to debug the project. Once everything is green, then you can push your work.

Test-Driven development is a development method that aims to reduce the anomalies of an application by encouraging frequent testing. You have to keep in mind that you are not alone on a project. It is therefore essential to push on your branch with each new addition. It is also very important to put the name of your test and project function in your commit before pushing.

## Test Coverage Metric

## Team version-control

Once again, the challenge of a project is above all teamwork. You must be able to work on your individual task while making sure that you don't interfere with other people assigned to the project. Git is a perfect tool for this. You need to follow a GitFlow process. A GitFlow process consists of several steps:

1. The creation of the git **branch**. It is very constraining to develop on code that is modified by others at the same time. To avoid this, each developer must create a git branch for each task assigned to him. The branch must be created from the last update of the Dev branch. The name of the branch must include the name of the developer as well as the name of the task to be performed. This task name must be the same as the one marked on its sprint map. To create a branch, just type :
```
    git checkout -b [branch-name]
```

2. Once the task is finished or you want to submit a progress, you must first of all retrieve the code that's on the dev branch. Other developers have also advanced on their tasks. So you have to get the latest version of the dev branch. To do this you must type the command: 
```
    git pull origin dev
```

3. Once you are up to date on the latest version of the dev branch, you can push your work on your branch. For the commit message, you must take the name of your task from your sprint as well as the added features. Here are the commands to type to submit your work:

```
    git add [files to add]
    git commit -m "[commit message]"
    git push origin [branch-name]
```

4. Finally, to submit your final work, you must make a pull request on the dev branch. Make sure you are up to date on the latest version. You can then go to the github interface and request a pull request on the dev branch. This pull request will then be reviewed and validated by an admin.

It is sometimes difficult to work with github in the beginning. You may have difficulty distinguishing the notion of branch or to see the progress of a project. Try to see a branch as a version of the project. Several tools can also help you to use github. For example, [GitKraken](https://www.gitkraken.com/) is a very good tool for managing github. I'll let you learn more about it if you're interested.

## Code-review checklist

1. General
    - [ ] The code works
    - [ ] The code is easy to understand
    - [ ] Follows coding conventions
    - [ ] Functions are simple and if possible short
    - [ ] Functions are spelt correctly
    - [ ] Names contain units where applicable
    - [ ] All class, variable, and method modifiers are correct.
    - [ ] There is no commented out code
    - [ ] There is no dead code (inaccessible at Runtime)
    - [ ] Debugging code is absent
    - [ ] Code is not repeated or duplicated
    - [ ] Ideal data structures are used
    - [ ] No memory leaks

- Documentation
    - [ ] All methods are commented in clear language.
    - [ ] Comments exist and describe rationale or reasons for decisions in code

- Security
    - [ ] All data inputs are checked (for the correct type, length/size, format, and range)
    - [ ] Invalid parameter values handled such that exceptions are not thrown
    - [ ] No sensitive information is logged or visible in a stacktrace