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

