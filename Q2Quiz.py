# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.

#read file
readQ = open("questions.txt","r")

#print the multiple choice question
question = readQ.readline()
print("The question is:\n" + question)
a = readQ.readline()
b = readQ.readline()
c = readQ.readline()
d = readQ.readline()
answer = readQ.readline()
print("A." + a)
print("B." + b)
print("C." + c)
print("D." + d)

#ask user for answer
UserAnswer = input("What is the correct answer?\n")

#determine if answer is right or not
if UserAnswer == answer:
    print("Correct!")
else:
    print("Wrong!")