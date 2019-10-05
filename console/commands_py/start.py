#Imports

#Start console
loop="true"
print()
print('Hello to the     Text-Coding-Libary      :')
print()
print("If you need any Help, type: 'help'")
print()
while loop=="true":
    input = input("Input: ")
    input = input.lower()
    print()
    #Start of splitting; Format: command(parameter1, parameter2, parameter3)[else]
    splitted1 = input.split("(")
    command = splitted1.pop(0)
    backtostring1 = str(splitted1)
    backtostring1 = backtostring1[:-2]
    backtostring1 = backtostring1.lstrip("['")
    splitted2 = backtostring1.split(", ")
    parameter1 = splitted2.pop(0)
    parameter2 = splitted2.pop(0)
    backtostring2 = str(splitted2)
    backtostring2 = backtostring2[:-2]
    backtostring2 = backtostring2.lstrip("['")
    splitted3 = backtostring2.split(")[")
    parameter3 = splitted3.pop(0)
    backtostring3 = str(splitted3)
    backtostring3 = backtostring3[:-3]
    backtostring3 = backtostring3.lstrip("['")
    other = backtostring3

    print("Command: " + command + "; Parameter: " + parameter1 + ", " + parameter2 + ", " + parameter3 + "; Other Arguments: " + other)
    if command=="help":
        print()
        print("Console help is still being written!")
        print("Help: For help, visit the repo.")
        print("Format of commands: command(parameter1, parameter2, parameter3)[other] ; command(), if no parameter is required.")
    loop="false"
