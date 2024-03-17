#Maru Puran
#What this code does - testing inputs, variables, and outputs, as well as how they interact w/ each other
#September 19th, 2023


# instructions 1 - asks user to input their name and favorite animal, then combines both answers into a sentence + prints

name = input("What is your name?: ")
animal = input("\nWhat is your favorite animal?: ")

print("\nHello, " + name + ". Your favorite animal is the " + animal + ".")

# instructions 2 - asks user to input a number then prints that number 3 times

number = input("\nPlease enter a number: ")
print("")
print(number, " ", number, " ", number)

# instruction 3 - asks user to input 3 test scores converts them to integers then finds the average by finding sum, storing in variable, then dividing the variable's value by 3 and storing it in another variable which is printed

test1 = int(input("\nPlease enter a test score: "))
test2 = int(input("Please enter another test score: "))
test3 = int(input("Please enter a third test score: "))

testSum = test1 + test2 + test3
testAvg = testSum/3
print("")
print(testAvg)

# instructions 4 - asks user for three words and prints the words in reverse orders from when they were entered 

word1 = input("\nPlease enter a word: ")
word2 = input("Please enter another word: ") 
word3 = input("Please enter a third word: ")

print("\n" + word3 + " " + word2 + " " + word1 )

# instructions 5 - asks users to enter integer for length and width, prints a rectangle with length and width labeled as well as the area, attainted by multiplying the integers the user enters

print("")
length = int(input("Please enter an integer for length: "))
width = int(input("Please enter an integer for width: "))
area = length*width

print("")

print(">  _____", width, "____\n> |             |\n> |             |\n> |             |", length, "\n> |             |\n> |             |\n> |_____________|")
print("\n     area = ", area)
