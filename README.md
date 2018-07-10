# Code Your Own Quiz: Numerical Reasoning Quiz
by Mostafa Elsheikh, part of [Intro to Programming Nanodegree](https://www.udacity.com/course/intro-to-programming-nanodegree--nd000)

## About
A simple numerical reasoning questions that takes user input to grade his/her answers.
Users can select difficulty level, and they can show explanation of their wrong answered questions.

### Project Files:
- `model.py` - This script implements the structure of the question
- `quiz.py` - This script simulates the quiz and view the data
- `numerical_reasoning.json` - JSON file that contains questions, model answers, explanation

## How to run
To run the script, clone this repository directory and run this command:
```sh
python quiz.py
```

## Preview
```sh
    Select your difficulty level:
    (1) Beginner
    (2) Intermediate
    (3) Advanced

    Please type the level number.

    0
Error! You've entered an invalid input.

    Select your difficulty level:
    (1) Beginner
    (2) Intermediate
    (3) Advanced

    Please type the level number.

    1
You have chosen beginner level..
Questions have been loaded for beginner level

    Question No. 1:
What least number should be added to 1056,
so that the sum is completely divisible by 23?
Answer Example: X
    2
Correct answer

    Question No. 2:
Find the median of 29, 23, 25, 29, 30, 25, 28
Answer Example: X
    3
Wrong answer

    Question No. 3:
Find the value of 6 + [ 5 - { 4 + ( 3 - ( 2 + 1 ) } ]
Answer Example: Rs. X
    5
Wrong answer

    Quiz has been ended...

    Results
    =======
    Correct Answers: 1
    Wrong Answers: 2
    Score: 0

Do you want to show explanations of wrong answered questions? (Y/N)Y

            Question No. 2 Explanation:
            =============================
Arranging the observations in the ascending order,
we get 23, 25, 25, 28, 29, 29, 30.
N = Number of observations = 7, This is an odd integer.
=> Median = [ ( N + 1 ) / 2]th term
= [ ( 7 + 1 ) / 2 ]th = 4th term in the ascending order data = 28


            Question No. 3 Explanation:
            =============================
The rule to be followed for this type of problems is BODMAS
and brackets in the order (), {}, [].
=> 6 + [ 5 - { 4 + ( 3 - ( 2 + 1 ) } ]
= 6 + [ 5 - { 4 + ( 3 - 3 ) } ]
= 6 + [ 5 - { 4 + 0 } ]
= 6 + [ 5 - 4 ]
= Rs. 7
```