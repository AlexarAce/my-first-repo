quest = int(input("What question are you trying to test?"))

if quest == 1:
    print("question 1!")
    cel = float(input("What is the temperature in Celcius? ")) # Saves input as a float valuable
    fahr = cel * (9/5) + 32
    print("The temperature in Fahrenheit is " + str(fahr) + " degrees.")

if quest == 2:
    print("\nQuestion 2!")
    name = input("what is your name?\n")
    adjective = input("give a Adjective \n")
    verb = input("Give a verb in it's past form\n")
    location = input("give a location\n")
    print(f"{name} {verb} at the {location} with a {adjective}")

if quest == 3:
    print("\nQuestion 3!")
    width = float(input("What is the width of the rectangle?\n"))
    height = float(input("What is the height of the rectangle?\n"))
    area = width*height
    perimeter = (2*width) + (2*height)
    print(f"Width: {width:.3f}")
    print(f"Height: {height:.3f}")
    print(f"Area: {area:.3f}")
    print(f"Perimeter: {perimeter:.3f}")

if quest == 4:
    print("\nQuestion 4!")
    price = float(input("What is the price of one of these items?\n"))
    quant = input("How many of these are you buying?\n")
    subtotal = price* float(quant) 
    gst = float(subtotal * 0.05)
    gst = round(gst, 2) #rounds to 2 decimal places
    total = subtotal + gst
    total = round(total, 2)
    print(f"Purchasing {quant} of this item worth ${price} icluding the GST amount of ${gst} is ${total}")

if quest == 5:
    print("Question 5!\n")
    mile = float(input("Give a number of miles: \n"))
    kilo = mile * 1.609344
    print(f" {mile:.2f} miles in kilometers is {kilo:.2f}km")

if quest == 6:
    print("Question 6!\n")
    distance = float(input("Enter a distance in kilometres. "))
    consumption = float(input("How many litres are consumed per 100km? "))
    price = float(input("What is the cost of 1 litre? $"))
    fuel = distance * (consumption/100)
    total = price * fuel
    print(f" Distance travelled: {distance:.2f}km\n Fuel consumed every 100km: {consumption:.2f}L\n Price per litre: ${price:.2f}\n Fuel needed: {fuel:.2f}L\n Total cost: ${total:.2f}")