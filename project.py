#Write a program that uses a while loop, if statement, break, and (if applicable) an array.  In the comments, write a brief description about what it does and how it is useful to you.  
#description: A fast food thing that stores fast food and displays the listed fast food places once stopped.

#array 
array = ["Chipotle", "Taco Bell", "Chic Fil A",]

#While loop
while True:
    userinput = input("Add your favorite fast food places!\nType 'quit' to quit.\n")

    #if statement
    if userinput.lower() == "quit":
        for food in array:
            print(food)
        #break
        break

    else:
        array.append(userinput.title())
        