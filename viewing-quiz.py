# This questionnaire was created by Sabrina Palis
# during the Bertelsmann Scholarship Challenge 2019
# It focuses on the commands for viewing files.

import random

# The Quiz class consists of a question, a correct answer and
# the wrong answers. 
class Quiz:
    def __init__(self, question, correctAnswer, otherAnswers):
        self.question = question
        self.correctAnswer = correctAnswer
        self.otherAnswers = otherAnswers

# List of Quiz objects.
quizList = [Quiz("What command should you use to view the dictionary.txt file?", "cat dictionary.txt", ["dog dictionary.txt", "purr dictionary.txt?"]),
Quiz("What command displays the full contents of the file christmas_list.txt'", "cat christmas_list.txt", ["cat full christmas_list.txt", "cat plus christmas_list.txt"]),
Quiz("The file drama.txt has more text than will fit on the screen at once. \n What command should you run?", "less drama.txt ", ["short drama.txt", "mcbeth drama.txt"]),
Quiz("Is there a search feature that comes with less?", "Yes, that's why less is useful", ["Nope", "Maybe"]),
Quiz("How do you search for shakespeare", "You run /shakespeare", ["You run ?Shakespeare", "You run !Shakespeare"]),
Quiz("You've started the less program, then you press the spacebar. \n What happens?'", "It scrolls downs", ["It highlights words", "It prompts you to enter a word to search"]),
Quiz("You've started the less program, then you press the q key. \n What happens?", "You exit less", ["It searches for all the words starting with q", "It displays a list of high tech widgets"]),
Quiz("In the less program, when do you need to type a forward slash?", "Before the word you want to search", ["After the word you want to search", "You don't use the forward slash, the forward slash uses you."]),
Quiz("In the less program, how do you scroll up?", "You press the b key", ["You press the u key", "You press the 8 key"])]

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
