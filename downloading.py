# This questionnaire was created by Sabrina Palis
# during the Bertelsmann Scholarship Challenge 2019
# It focuses on the commands to navigate directories.

import random

# The Quiz class consists of a question, a correct answer and
# the wrong answers. 
class Quiz:
    def __init__(self, question, correctAnswer, otherAnswers):
        self.question = question
        self.correctAnswer = correctAnswer
        self.otherAnswers = otherAnswers

# List of Quiz objects.
quizList = [Quiz("What does curl stand for?", "See url", ["Curl up like a cat", "Can you rule the log?"]),
Quiz("What happens when you run \n    curl 'http://www.google.com'", "By default it will download the file and display the content in the terminal", ["It will open a browser window", "It will launch a google search"]),
Quiz("Why do you put single quotes ' around the URL after curl?", "Because a lot of URLs have special characters in them ", ["Because it's more polite", "Because it complies with Harvard referencing"]),
Quiz("What happens if you add the -L option to curl?", "It will follow any redirects and then download the file stored at that location", ["It will give you a long list", "You will see the UR but not the L"]),
Quiz("What does the s stand for in https?", "secure", ["awesome sauce", "sassy"]),
Quiz("What happens when you run \n    curl 'https//www.google.com'?'", "A very large block of HTML gets displayed in the terminal window", ["Nothing happen you cannot curl Google", "It changes the font on your web page"]),
Quiz("How do you tell curl to output the data to a file?", "By adding the -o option", ["By adding OUTPUT", "By adding -Out here"]),
Quiz("What does this command do? \n    curl -L -o some_file.html 'http://www.google.com'", "It follows redirects, downloads, and output the data to some_file", ["It creates a long log about the file and upload it on Google", "It doesn't exist"]),
Quiz("What happens when you run \n    curl -L -o dictionary.txt 'https://tinyurl.zeyq9vc'?", "It follows redirects, downloads, and save the data as dictionary.txt  ", ["It ouputs the data on the terminal", "It converts the dictionary file into a list"])]

# Correct Answers counter
correctCount = 0

# Shuffle the list of Quiz objects
random.shuffle(quizList)

# Loop to iterate over each item of the list
for quizItem in quizList:
  print(quizItem.question)
  possible = quizItem.otherAnswers + [quizItem.correctAnswer]
  random.shuffle(possible)
  count = 0 # list indexes start at 0 in python
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Please enter the number of your answer:")
  userAnswer = input()
  while not userAnswer.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    userAnswer = input()
  userAnswer = int(userAnswer)
  while not (userAnswer > 0 and userAnswer <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    userAnswer = input()
  if possible[userAnswer-1] == quizItem.correctAnswer:
    print("Well done! Your answer was correct.")
    correctCount += 1
  else:
    print("I'm so sorry. Your answer was wrong.")
    print("The correct answer was: " + quizItem.correctAnswer)
  print("")

print("You answered " + str(correctCount) + " of " + str(len(quizList)) + " questions correctly.")
if correctCount > 8:
    print("Congratulations")
else:
    print("Watch the video lessons again and come back test your knowledge!")
