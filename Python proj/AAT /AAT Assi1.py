# Display a welcoming statement
print("Welcome to the Smartphone Shopping Center!")
# Display the available phone model options
print('''Available options:
1. iPhone 12
2. iPhone 13 Mini
3. iPhone 13 Pro
4. Samsung Galaxy S1
5. Samsung Galaxy S2''')



# Assign starting value for the total price 
total_price = 0
# Assign starting value for a price of a specific phone
total = 0
# Assign starting value for the phone model
phone_model = "To be chosen"
# Enter a while loop until the user enters "quit"
while phone_model.lower() != "quit":
    # Prompt the user to choose a phone model
    phone_model = input("Enter the number corresponding to your desired smartphone or type 'quit' to finish: ")
    # Check which phone model that the user chooses
    if (phone_model == "1"):
        # Prompt the user to enter the memory size
        memory_size = int(input("Enter the memory size(GB) for iphone 12(128 or 256): "))
        # Enter a while loop until the user enters either 128 or 256
        while (memory_size != 128 and memory_size != 256):
            # Display that the input is invalid and ask the user to enter the right value
            print("Please enter a valid input! Enter either 128 or 256")
            memory_size = int(input("Enter the memory size(GB) for iphone 12(128 or 256): "))
        # Prompt the user to enter how many phones do they need and change it into an integer data type
        quantity = input("Enter the quantity: ")
        # If the user enters zero or a negative number, then enter a while loop until the user enters a positive number
        while (not quantity.isdigit() or int(quantity) < 0):
            # Display that the input is invalid and ask the user to enter the quantity
            print("Invalid input! Please enter a non-negative integer and try again!")
            quantity = input("Enter the quantity: ")
        # Check if the memory size is 128 or 256
        if (memory_size == 128):
            # Calculate the total by multiplying the quantity with the unit price
            total = int(quantity) * 3199
        else:           
            # Calculate the total by multiplying the quantity with the unit price
            total = int(quantity) * 3599

    # Check if the number chosen is #2
    elif (phone_model == "2"):
        # Prompt the user to enter the memory size
        memory_size = int(input("Enter the memory size(GB) for iphone 13 Mini(64 or128): "))
        # Enter a while loop until the user enters either 64 or 128.
        while (memory_size != 64 and memory_size != 128):
            # Display that the input is invalid and ask the user to enter the right value
            print("Please enter a valid input! Enter either 64 or 128")
            memory_size = int(input("Enter the memory size(GB) for iphone 13 Mini(64 or 128): "))
        # Prompt the user to enter how many phones do they need and change it into an integer data type        
        quantity = input("Enter the quantity: ")
        while (not quantity.isdigit() or int(quantity) < 0):
            print("Invalid input! Please enter a non-negative integer and try again!")
            quantity = input("Enter the quantity: ")
        # Check if the memory size is 64 or 128            
        if (memory_size == 64):
            # Calculate the total by multiplying the quantity with the unit price
            total = int(quantity) * 2499
        else:
            # Calculate the total by multiplying the quantity with the unit price
            total = int(quantity) * 2799
            


    # Check if the number chosen is #3    
    elif (phone_model == "3"):
        # Prompt the user to enter the memory size
        memory_size = int(input("Enter the memory size(GB) for iphone 13 Pro(256 or 512): "))
        # Enter a while loop until the user enters either 256 or 512.
        while (memory_size != 256 and memory_size != 512):
            # Display that the input is invalid and ask the user to enter the right value
            print("Please enter a valid input! Enter either 256 or 512")
            memory_size = int(input("Enter the memory size(GB) for iphone 13 Pro(256 or 512): "))
        # Prompt the user to enter how many phones do they need and change it into an integer data type 
        quantity = input("Enter the quantity: ")
        while (not quantity.isdigit() or int(quantity) < 0):
            print("Invalid input! Please enter a non-negative integer and try again!")
            quantity = input("Enter the quantity: ")  
        # Check if the memory size is 256 or 512         
        if (memory_size == 256):
            # Calculate the total by multiplying the quantity with the unit price
            total = int(quantity) * 4999
        else:
            # Calculate the total by multiplying the quantity with the unit price
            total = int(quantity) * 5999


    # Check if the number chosen is #4
    elif (phone_model == "4"):
        # Prompt the user to enter the memory size
        memory_size = int(input("Enter the memory size(GB) for Galaxy S1(128 or 256): "))
        # Enter a while loop until the user enters either 128 or 256.
        while (memory_size != 128 and memory_size != 256):
            # Display that the input is invalid and ask the user to enter the right value
            print("Please enter a valid input! Enter either 128 or 256")
            memory_size = int(input("Enter the memory size(GB) for Galaxy S1(128 or 256): "))
        # Prompt the user to enter how many phones do they need and change it into an integer data type 
        quantity = input("Enter the quantity: ")
        while (not quantity.isdigit() or int(quantity) < 0):
            print("Invalid input! Please enter a quantity which is a non-negative integer and try again!")
            quantity = input("Enter the quantity: ")  
        # Check if the memory size is 128 or 256          
        if (memory_size == 128):
            # Calculate the total by multiplying the quantity with the unit price
            total = int(quantity) * 2899
        else:
            # Calculate the total by multiplying the quantity with the unit price
            total = int(quantity) * 3299

    # Check if the number chosen is #5
    elif (phone_model == "5"):
        # Prompt the user to enter the memory size
        memory_size = int(input("Enter the memory size(GB) for Galaxy S2(64 or 128): "))
        # Enter a while loop until the user enters either 64 or 128.
        while (memory_size != 64 and memory_size != 128):
            # Display that the input is invalid and ask the user to enter the right value
            print("Please enter a valid input! Enter either 64 or 128")
            memory_size = int(input("Enter the memory size(GB) for Galaxy S2(64 or 128): "))
        # Prompt the user to enter how many phones do they need and change it into an integer data type 
        quantity = input("Enter the quantity: ")
        while (not quantity.isdigit() or int(quantity) < 0):
            print("Invalid input! Please enter a non-negative integer and try again!")
            quantity = input("Enter the quantity: ")  
        # Check if the memory size is 64 or 128         
        if (memory_size == 64):
            # Calculate the total by multiplying the quantity with the unit price
            total = int(quantity) * 1799
        else:
            # Calculate the total by multiplying the quantity with the unit price
            total = int(quantity) * 1999
    # if the user enters something other than the options, display that they should try again
    elif(phone_model.lower() == "quit"):
        print("Thank you! Let's proceed to the payment methods!")
    else:
        print("Invalid input, Please enter numbers from the available options and try again!")
    
    # Calculate the total price by adding the previous total price and total values
    total_price = total_price + total
    # Reset the value of total to zero
    total = 0
# Display the total price
print("Total price: " , total_price)



    
# Display the available payment options
print('''Available options:
1. FAB banking cards
2. ADIB banking cards
3. Other banking cards
4. cash''')

# Assign a starting value to a membership point
membership_points = 0  
# Prompt the user to enter payment method 
payment_method = input(("Enter the number corresponding to your payment method: "))

# check which payment method the user chooses
if (payment_method == "1"):
    # Deduct the discount from the total price
    total_price = total_price - (total_price * 0.1)
    # Display the total price after the discount
    print("Total price: ", total_price, "AED(After 10% FAB banking card discount).")


# Check if the number chosen is 2
elif (payment_method == "2"):
    # Deduct the discount from the total price
    total_price = total_price - (total_price * 0.15)
    # Display the total price after the discount
    print("Total price: ", total_price, "AED(After 15% ADIB banking card discount).")


# Check if the number chosen is 3
elif (payment_method == "3"):
    # Deduct the discount from the total price
    total_price = total_price - (total_price * 0.05)
    # Display the total price after the discount
    print("Total price: ", total_price, "AED(After 5% other banking cards discount).")


# Check if the number chosen is 4
elif (payment_method == "4"):
    # Deduct the discount from the total price
    total_price = total_price 
    # Display the total price after the discount
    print("Total price: ", total_price, "(With no discount).")


# If the user enters something other than the options, display that they should try again 
# In this case the code will have failure case, and there would be a logical error because the user enters an invalid input.
else:
    print("Your choice is not in the menu, Please enter a number corresponding to the available options and try again!")


# Calculate the membership point by using floor division
membership_points = total_price // 100
# Display the membership points earned
print("Membership Points Earned: ", membership_points, "(1 point for every 100 AED spent)")   




# Check if the membership points are above 10
if(membership_points >= 10):
    # Ask the user if they want to redeem their membership
    redemption = input("Would you like to redeem your membership points?(yes/no): ")
    # Check if the user wants the redemption
    if (redemption.lower() == "yes"):
        # Display the redemption rate
        print("Redemption Rate: 1 point = 5 AED")
        # Calculate the discount by multiplying the membership points by 5
        discount = membership_points * 5
        # Display the discount
        print("Discount Applied: ", discount)
        # Calculate the total price deducing the discount
        total_price = total_price - discount
        # Display the updated total point
        print("Updated Total Price: ", total_price, "AED")
    # Check if the user does not want the redemption
    elif (redemption.lower() == "no"):
        # Just display the total price
        print("Total Price: ", total_price)
    
    # If the user enters an invalid input, inform the user to try again
    else:
        print("Invalid input, please enter either yes or no and try again!")
# If the membership points are above 10, just display the total price 
else:
    print("Total Price", total_price)

# Display a message for the user
print("Thank you for shopping with us!")

