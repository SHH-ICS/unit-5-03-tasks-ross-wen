# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.

#Ask for all the inputs
multipleChoice = input("Please Input your Multiple Choice Question: \n")
answerA = input("Input answer for choice A: \n")
answerB = input("Input answer for choice B: \n" )
answerC = input("Input answer for choice C: \n")
answerD = input("Input answer for choice D: \n")
correct = input("Input Letter for Correct Answer: \n")

#create the file handle
questions = open("questions.txt","w")
#write all the inputs to the file
questions.write(multipleChoice + "\n")
questions.write(answerA + "\n")
questions.write(answerB + "\n")
questions.write(answerC + "\n")
questions.write(answerD + "\n")
questions.write(correct)
#close the file
questions.close()
