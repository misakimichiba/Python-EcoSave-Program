#Done by Misaki Michiba, Student ID No: B1901267

def main():
    choice = 0
    #Here is to call the function inputDetails for Task 1
    userName, age, gender, paperQuantity, plasticQuantity, oilQuantity, electricQuantity = inputDetails()
    #I assigned values to these variables to avoid the error that happens when the user uses the membership
    #tier function before calculating their points
    collectorPoint = 0
    recyclerPoint = 0
    choice = menu()
    if choice == 'q' or choice == 'Q':
        print("\nThank you for using this program.")
    
    #The loop to ensure the menu will reappear until user chooses to quit
    while choice == '1':
        #Call function pointCalculator for Task 2
        collectorPoint,recyclerPoint = pointCalculator(paperQuantity, plasticQuantity, oilQuantity,\
                                                       electricQuantity)
        #Print out the statement on points earned and whether user is a collector or recycler
        #Done here since variable userName is needed and not used in the pointCalculator function
        if recyclerPoint > 0:
            print("\nRecycler " + str(userName) + " earned " + str(recyclerPoint) + " points")
        else:
            print("\nCollector " + str(userName) + " earned " + str(collectorPoint) + " points")
        choice = menu()
        if choice == 'q' or choice == 'Q':
            print("\nThank you for using this program.")
        
    while choice == '2':
        if choice == 'q' or choice == 'Q':
                print("\nThank you for using this program.")
        elif recyclerPoint != 0 or collectorPoint != 0:
            status, remainingPoint = viewMembership(userName, collectorPoint, recyclerPoint)
            choice = menu()
            #Added another while loop to ensure that the menu will reappear even if user chose '1'
            while choice == '1':
                collectorPoint,recyclerPoint = pointCalculator(paperQuantity, plasticQuantity,\
                                                           oilQuantity, electricQuantity)
                if recyclerPoint > 0:
                    print("Recycler " + str(userName) + " earned " + str(recyclerPoint) + " points")
                else:
                    print("Collector " + str(userName) + " earned " + str(collectorPoint) + " points")
                choice = menu()
                if choice == 'q' or choice == 'Q':
                    print("\nThank you for using this program.")
            if choice == 'q' or choice == 'Q':
                print("\nThank you for using this program.")
        #The else statement is what will print out if the user does not use the point calculator before using the membership tier function
        #This is to prevent an error from happening 
        else:
            print("")
            print("Please use the points calculator function first or do not enter only 0s into the input")
            choice = menu()
            #Added another while loop to ensure that the menu will reappear even if user chose '1'
            while choice == '1':
                collectorPoint,recyclerPoint = pointCalculator(paperQuantity, plasticQuantity,\
                                                           oilQuantity, electricQuantity)
                if recyclerPoint > 0:
                    print("Recycler " + str(userName) + " earned " + str(recyclerPoint) + " points")
                else:
                    print("Collector " + str(userName) + " earned " + str(collectorPoint) + " points")
                choice = menu()
                if choice == 'q' or choice == 'Q':
                    print("\nThank you for using this program.")
            

    while choice == '3':
        print("")
        #Called the function main here to repeat/reset the entire thing
        main()
        
def inputDetails():
    #This function is to prompt the user to enter values into the variables used
    print("Please input your details below:")
    userName = input("Name: ")

    #To ensure that user does not enter something besides an integer
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Please enter an integer")
        age = int(input("Age: "))
        
    gender = input("Gender[F/M]: ")
    #Validate user input for gender by using while loop
    while gender != 'F' and gender != 'f' and gender != 'Female' and gender != 'female' \
and gender !='M' and gender != 'm' and gender != 'Male' and gender != 'male':
        print("Please enter either F/M/Female/Male/female/male")
        gender = input("Gender[F/M]: ")
        
    paperQuantity = eval(input("Paper Quantity [kg]: "))
    plasticQuantity = eval(input("Plastic Quantity [kg]: "))
    oilQuantity = eval(input("Oil Quantity [bottle]: "))
    electricQuantity =  eval(input("Electrical [unit]: "))
    
    return (userName, age, gender, paperQuantity, plasticQuantity, oilQuantity, electricQuantity)

def menu():
    #Welcome and introductory message here
    print("\nWelcome to the EcoSave program!\nThis program is used\
 to calculate your points and to\ninform you of your membership tier info.")
    
    #The full menu is displayed here
    print("Choose your option below:\n\
1 - Points Calculator\n\
2 - Membership Tier\n\
3 - Reset\n\
Q/q - Quit")
    choice = input("Your choice? ")
    
    #Validate user input for choice in the menu by using while loop
    while choice != '1' and choice != '2' and choice != '3' and choice != 'Q' and choice != 'q':
        print("Invalid choice! Please select from the list of choices.\n")
        print("Choose your option below:\n\
1 - Points Calculator\n\
2 - Membership Tier\n\
3 - Reset\n\
Q/q - Quit")
        choice = input("Your choice? ")
    
    return(choice)

def pointCalculator(paperQuantity, plasticQuantity, oilQuantity, electricQuantity):
    #This function is to do the calculations for the points accumulated by the user
    print("\nChoose your option below:\n\
1 - collector\n\
2 - recycler")
    choicePC = input("Your choice? ")
    
    #Validate user input for choice with while loop
    while choicePC != '1' and choicePC != '2':
        print("That is not a valid choice. Please enter either 1 or 2")
        choicePC = input("Your choice? ")
        
    if choicePC == '1':
        #Calculation of points for collector
        collectorPoint = (paperQuantity * 30) + (plasticQuantity * 50) + (oilQuantity * 70) + (electricQuantity * 90)
        recyclerPoint = 0
        
    elif choicePC == '2':
        #Calculation of points for recycler
        recyclerPoint = (paperQuantity * 40) + (plasticQuantity * 60) + (oilQuantity * 80) + (electricQuantity * 100)
        collectorPoint = 0
        
    return(collectorPoint, recyclerPoint)

def viewMembership(name, collectorPoint, recyclerPoint):
    #This function is to show the user how many points they need for the next status and
    #what their current status is
    print("\nChoose your option below:\n\
1 - collector\n\
2 - recycler")
    choiceVM = input("Your choice? ")

    #To validate user input for choice with a while loop
    while choiceVM != '1' and choiceVM != '2':
        print("\nThat is not a valid choice. Please enter either 1 or 2")
        choiceVM = input("Your choice? ")

    #To make sure that the points fit with the choice of either recycler or collector that the user made before this
    if recyclerPoint == 0 and choiceVM == '2':
        status = "None"
        remainingPoint = 0
        print("\nThere is no recycler point.")
        
    elif collectorPoint == 0 and choiceVM == '1':
        status = "None"
        remainingPoint = 0
        print("\nThere is no collector point.")

    #Shows the status and remaining points for a collector who does not meet the minimum required points
    elif collectorPoint <500 and choiceVM == '1':
        status = "None"
        remainingPoint = 500 - collectorPoint
        print("\nCollector " + str(name) + " does not meet the minimum required points. Collect another " +
              str(remainingPoint) + " points to become the 'Eco Saver'.")

    #Shows the status and remaining points for a collector who has achieved the "Eco Saver" status
    elif collectorPoint >= 500 and collectorPoint <800:
        remainingPoint = 800 - collectorPoint
        status = "Eco Saver"
        print("\nCongratulations! Collector " + str(name) + " is the '" + str(status) + "'. Collect another " +
              str(remainingPoint) + " points to become the 'Eco Hero'.")

    #Shows the status and remaining points for a collector who has achieved the "Eco Hero" status
    elif collectorPoint >= 800 and collectorPoint <1000:
        remainingPoint = 1000 - collectorPoint
        status = "Eco Hero"
        print("\nCongratulations! Collector " + str(name) + " is the '" + str(status) + "'. Collect another " +
              str(remainingPoint) + " points to become the 'Eco Warrior'.")

    #Shows the status for a collector who has achieved the "Eco Warrior" status
    elif collectorPoint >=1000:
        remainingPoint = 0
        status = "Eco Warrior"
        print("\nCongratulations! Collector " + str(name) + " is the '" + str(status) + "'. This is the highest\
 title one can receive!")

    #Shows the status and remaining points for a recycler who does not meet the minimum required points
    elif recyclerPoint <500 and choiceVM == '2':
        status = "None"
        remainingPoint = 500 - recyclerPoint
        print("\nRecycler " + str(name) + " does not meet the minimum required points. Collect another " +
              str(remainingPoint) + " points to become the 'Eco Saver'.")

    #Shows the status and remaining points for a recycler who has achieved the "Eco Saver" status
    elif recyclerPoint >= 500 and recyclerPoint <800:
        remainingPoint = 800 - recyclerPoint
        status = "Eco Saver"
        print("\nCongratulations! Recycler " + str(name) + " is the '" + str(status) + "'. Collect another " +
              str(remainingPoint) + " points to become the 'Eco Hero'.")

    #Shows the status and remaining points for a recycler who has achieved the "Eco Hero" status
    elif recyclerPoint >= 800 and recyclerPoint <1000:
        remainingPoint = 1000 - recyclerPoint
        status = "Eco Hero"
        print("\nCongratulations! Recycler " + str(name) + " is the '" + str(status) + "'. Collect another " +
              str(remainingPoint) + " points to become the 'Eco Warrior'.")

    #Shows the status for a recycler who has achieved the "Eco Warrior" status
    elif recyclerPoint >=1000:
        remainingPoint = 0
        status = "Eco Warrior"
        print("\nCongratulations! Recycler " + str(name) + " is the '" + str(status) + "'. This is the highest\
 title one can receive!")

    return(status, remainingPoint)

#calling the main function to run the program
main()
    
