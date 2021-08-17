f=open("numbers.txt","w")

choice = "Yes"

# As long as user enters 'Yes' accept input from the user
while choice.lower() != "no":
    num = input("Enter an integer: ")

    # If input is not an integer, prompt the user to enter valid input
    if not num.isdigit():
        print("Invalid input.")
        num = input("Enter a valid integer: ")

    # write the number to file
    f.write(f"{num}\n")
    
    choice = input("Do you want to continue?(Yes/No) :")

# close the file
f.close()
