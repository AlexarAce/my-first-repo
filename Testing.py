test = input("what tes would you like to run?")

if(test == "input"):
    name = input() #takes a string input from the user. Can contain quotes like asking a question
    print(name) #prints the variable given

if(test == "intprint"):
    number = 4 #saved as an integer
    print(number)

if(test == "math"):
    a = 10 
    b = 3

    print(a+b) #add integers
    print(a-b) #subtract integers
    print(a*b) #multiply integers
    print(a/b) #divide integers
    print(a**b) #Exponent. The First number is taken as the exponent of the second number.
    print(a//b) #Floor divides. Basically just removes the decimal place

if(test == "back slashes"):
    print("It's a \"groovy\" day!") # The backslashes (\) prevent the quotes from being considered as an operation

if(test == "changing data types"):
    final_grade = 97 #can only be used in this operation because its defined in this opperation
    print("you final grade was " + str(final_grade)) #without changing the datat type it would try to add a str with an integer because it was saved a s an integer

if(test == "formatting strings"):
    name = "rob"
    final_grade = 99
    print(f"hello {name}! I see your final grade was {final_grade}") #Note the F at the beginning
    print("hello " + name + "! i see your final grade was " + str(final_grade)) #the long way of doing this)