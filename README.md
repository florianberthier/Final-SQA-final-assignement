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

One of the interesting metrics to calculate in scrum is velocity metrics. Velocity refers to the average amount of work a Scrum team performs during a sprint. Measured in story points or hours, it is very useful for forecasting.

## Project Documentation

## Unit testing and Test-Driven development

Testing is the basis of a successful project. It is imperative that you provide tests for each of your code additions. The tests must be complete, i.e. test all possible cases. The name of the test should be the same as the name of the function being tested to simplify the work of other developers. In our example project, the basic python tool py.test is used. To start the test series, run the command:
```
    py.test
```
If you get red after typing the command, it means that there is an error in the code or in the test. So it's up to you to debug the project. Once everything is green, then you can push your work.

Test-Driven development is a development method that aims to reduce the anomalies of an application by encouraging frequent testing. You have to keep in mind that you are not alone on a project. It is therefore essential to push on your branch with each new addition. It is also very important to put the name of your test and project function in your commit before pushing.

## Test Coverage Metric

## Team version-control

## Code-review checklist

