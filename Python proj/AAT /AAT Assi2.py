print("-------------------------------------------------------------------------------------------------------------------------------")
# print a welcoming statement to the Ferrari World Yas Island, Abu Dhabi for the user
print("\t \t \t \t WELCOME TO FERRARI WORLD YAS ISLAND, ABU DHABI \n \t \t Love speed? Then gear up for the ride of your life only here at Ferrari World Abu Dhabi. Home to\n \t the world's fastest rollercoaster, the highest loop ride, the tallest space-frame structure ever built on the planet\n and over 40 record-breaking attractions, this is the ultimate destination for non-stop, hyper-adrenaline, heart-racing fun! ")
# print a line before entering to the sign-in or register options
print("*******Purchase as many tickets, annual passes, experiences, and offers as you want for anyone. BOOK YOUR TICKETS NOW! ENJOY!******")
print("-------------------------------------------------------------------------------------------------------------------------------")
# create a dictionary that has a username and a password as its key-value pair and call it username_password
username_password = {"Amna" : "1234", "Eleni" : "5678", "Tsion" : "abcd"}
# create a set that contains only the keys(which are the usernames) from the above dictionaary(username_password) and call it username
username = {"Amna", "Eleni", "Tsion"}
# define a function called 'Sign_In()' that lets users log in into their accounts
def Sign_In():
    # prompt the user to enter their username and save it in a variable called enter_username
    enter_username = input("Please enter your username: ")
    # prompt the user to enter their password and save it in a variable called enter_password 
    enter_password = input("Please enter your password: ")
    # enter a while loop to validate the user's username and password input until the user entered a value that is in the username set, and until the username they entered corresponds to the correct password in the username set
    while ((enter_username not in username) or (len(enter_username) == 0)) or ((enter_password != username_password[enter_username]) or (len(enter_password) == 0)):
        # print an invalid message that informs the user that the information they entered is incorrect
        print("You either did not enter values or the information you entered does not match. Please try again.")
        # prompt the user again to enter a username
        enter_username = input("Please enter your username: ")
        # prompt the user again to enter a password
        enter_password = input("Please enter your password: ")
    # print a successful try message for the user 
    print("You have successfully signed in!")

# define a function called 'Register()' that lets user register for an account for their first time
def Register():
    # prompt the user to enter their username and save it in a variable called enter_username
    enter_username = input("Please enter a username: ")
    # enter a while loop to validate the user's username input until the user entered a value that is not already in the username dictionary
    while enter_username in username or len(enter_username) == 0:
        # print an invalid message that informs the user that the information they entered is incorrect
        print("The username you entered already exists or you did not enter anything. Please try again.")
        # prompt the user again to enter a username
        enter_username = input("Please enter a username: ")
    # Once the user's usernameis is validated, prompt the user to enter a password
    enter_password = input("Please enter a password: ")
    # enter a while loop until the user typed something for their password
    while len(enter_password) == 0:
        # print an invalid message for the user to inform them they have not entered anything for their password 
        print("You did not enter a password. Please try again.")
        # prompt the user again to enter a password
        enter_password = input("Please enter a password: ")
    # add the user's username and password (as a key-value pair) to the dictionary username_password  
    username_password[enter_username] = enter_password
    # add the user's username into the set username
    username.add(enter_username)
    # print a message to inform the user that their registration was successful
    print("You are successfully registered!")
    # call the 'Sign_In()' function to let the user login into their accounts after registration
    Sign_In()
# prompt the user to choose from 'sign-in' and 'register' options
enter = input("If you have an account, enter 'sign in'. If you do not have an account, please enter 'register': ")
# enter a while loop to validate the user's input until the user entered either'sign in' or 'register'
while enter.lower() != 'sign in' and enter.lower() != 'register':
    # print an error message for the user 
    print("The value you entered is not 'sign in' or 'register'. Please try again.")
    # prompt the user again to choose from 'sign-in' and 'register' options only
    enter = input("If you have an account, enter 'sign in'. If you do not have an account, please enter 'register': ")
# if the user entered 'sign in' for the 'enter' input 
if enter.lower() == 'sign in':
    # call the 'Sign_In()' function to let the user login into their accounts
    Sign_In()
# otherwise, if the user entered 'register' for the 'enter' input 
else:
    # call the 'Register()' function to let the user register for an account for their first time
    Register()

# print a line before entering to entry ticket options
print("--------------------------------------------ENTRY TICKETS--------------------------------------------------------")

# create a dictionary that contains type of entry tickets with their corresponding price as its key-value price and call it 'ticket_type_dict'
ticket_type_dict = {"Single Day Ticket (Adult)" : 345, "Single Day Ticket (Junior)" : 265, "2 Park Ticket (4 years above)" : 475, "3 Park Ticket (4 years above)" : 575, "4 Park Ticket (4 years above)" : 675}
# create a nested data structure that contains tuples(each containing a roll number, ticket type and corresponding price) inside a list and call it 'ticket_type_list'
ticket_type_list = [(1, "Single Day Ticket (Adult)", 345), (2, "Single Day Ticket (Junior)", 265), (3, "2 Park Ticket (4 years above)", 475), (4, "3 Park Ticket (4 years above)", 575), (5, "4 Park Ticket (4 years above)", 675)]

# iterate through every item(which are the tuples in the list 'ticket_type_list') in the list 'ticket_type_list'
for i in ticket_type_list:
    # print the first, second and third elements of the tuple inside the 'ticket_type_list' list
    print(i[0], ".", i[1], ":", "AED", i[2])
# define a function called 'Prompt_Entry_Ticket()' to return the chosen ticket types with their corresponding quantity
def Prompt_Entry_Ticket():
    # create an empty dictionary to save the corresponding number to the ticket-type chosen with the quantity as a key-value pair and call it 'indiv_ticket_dict'
    indiv_ticket_dict = {}
    # prompt the user to choose the type of ticket they want to purchase
    ticket_type = input("Please enter the value corresponding to the ticket you would like to purchase or type 'quit' to finish: ")
    # enter a while loop to let the user choose as many ticket-types with their quantity, until the user enters 'quit'
    while ticket_type.lower() != 'quit':
        # check if the user entered non-digits or a number not in range(1,6)
        if not ticket_type.isdigit() or int(ticket_type) not in range(1, 6):
            # then print an error message, and inform the user to enter a number between 1 and 5
            print("The ticket option you entered is not valid. Please choose from the above ticket option and enter a number between 1 and 5(included).")
        # otherwise check if the user entered a number between 1 and 5
        else:
            # prompt the user to choose the quantity of ticket that they have chosen to purchase
            ticket_quantity = input("Please enter the number of tickets of your chosen type of ticket: ")
            # enter a while loop to validate the quantity of the tickets, until the user entered a positive integer
            while not ticket_quantity.isdigit() or int(ticket_quantity) <= 0:
                # print an error message to inform the user to enter only positive integers for quantitiy
                print("The value you entered is not valid. Please enter a positive number since the quantity is asked.")
                # prompt the user again to choose the quantity of ticket that they have chosen to purchase
                ticket_quantity = input("Please enter the number of tickets of your chosen type of ticket: ")
            # add the tickets chosen together with the ticktet's quantity as a key-value pair to the 'indiv_ticket_dict' dictionary  
            indiv_ticket_dict[ticket_type] = int(ticket_quantity)
        # prompt the user to choose the type of ticket they want to purchase 
        ticket_type = input("Please enter the value corresponding to the ticket you would like to purchase or type 'quit' to finish: ")
    # return the value of "indiv_ticket_dict" dictionary to use it in the subsequent functions
    return indiv_ticket_dict

# define a function called 'Total_Num_Tickets()' and pass the 'indiv_ticket_dict' dictionary as its parameter, to calculate the total number of tickets purchased 
def Total_Num_Tickets(indiv_ticket_dict):
    # return the total number of tickets the user purchased, from the values of the 'indiv_ticket_dict' dictionary
    return sum(indiv_ticket_dict.values())

# define a function called 'Total_Entry_Price()' and pass the 'ticket_type_list, indiv_ticket_dict' as its parameters, to calculate the total price of the tickets purchased
def Total_Entry_Price(ticket_type_list, indiv_ticket_dict):
    # initialize a variable to accumulate the total ticket prices and call it 'ticket_price_total'
    ticket_price_total = 0
    # iterate through every key in the "indiv_ticket_dict" dictionary 
    for i in indiv_ticket_dict:
        # calculate the total ticket price by multiplying each chosen ticket type prices with their corresponding quantity
        # from the 'ticket_type_list'(access the each element from the list, and the third element from the tuple inside the list) and multiply it with the prices(from the 'indiv_ticket_dict' dictionary values )
        ticket_price = ticket_type_list[int(i) - 1][2] * indiv_ticket_dict[i]
        # update the total ticket price every time the loop iterates by adding it to the previous total ticket price
        ticket_price_total += ticket_price
    # return the total ticket price to use it in the subsequent functions
    return ticket_price_total

# call the 'Prompt_Entry_Ticket()' function and assign it to a variable called "indiv_ticket_dict"
indiv_ticket_dict = Prompt_Entry_Ticket()
# call the 'Total_Num_Tickets(indiv_ticket_dict)' function and assign it to a variable called "otal_num_tickets"
total_num_tickets = Total_Num_Tickets(indiv_ticket_dict)
# call the 'Total_Entry_Price(ticket_type_list, indiv_ticket_dict)' function and assign it to a variable called "total_entry_price"
total_entry_price = Total_Entry_Price(ticket_type_list, indiv_ticket_dict)


# print a line before entering to annual pass options
print("--------------------------------------------ANNUAL PASS OPTIONS-----------------------------------------------------")
# create a dictionary that contains type annual pass options with their corresponding price as its key-value price and call it 'Pass_types'
Pass_types = {"1-Silver Yas Annual Pass : AED 1295 \n Four Parks Access: Including SeaWorld Admission for 12 months to Warner Bros. World, Yas Waterworld, Ferrari World, and SeaWorld.": 1295,"2-Golden Yas Annual Pass: AED 1495 \n Four Parks Access: Including SeaWorld Unlimited year-round access to Ferrari World Abu Dhabi, Yas Waterworld, Warner Bros. World, and SeaWorld Abu Dhabi.": 1495,"3-Diamond Yas Annual Pass: AED 3195 \n Four Parks Access: Including SeaWorld Our most exclusive tier! Unlimited year-round access with Quick Pass to Warner Bros. World, Yas Waterworld, Ferrari World, and SeaWorld.": 3195} #create a dictionary with all the annual passes with their details and prices
# create a nested data structure that contains tuples(each containing a roll number, annual pass option type and a corresponding price) inside a list and call it 'Pass_types'
annual_type_list = [(1, "Silver Yas Annual Pass", 1295), (2, "Gold Yas Annual Pass", 1495), (3, "Diamond Yas Annual Pass", 3195)]
# Display the available annual passes
print("Available Annual Pass Types:") 
# iterate through 'Pass_types' to access each element in the 'Pass_types' dict
for key in Pass_types: 
    # Display the keys of the 'Pass_types' dictionary that contains the annual type with their prices
    print(key)

# define a function to save the annual pass options chosen together with the number of tickets as a dictionary
def Annual_Pass_Type_Dict():
    # create an empty dictionary to save the corresponding number to the annual pass-type chosen with the quantity as a key-value pair and call it 'annual_pass_type_dict'
    annual_pass_type_dict = {}
    # Ask the user if they would like to purchase annual passes
    choice = input("Would you like to purchace an annual pass from the above options (yes/no)? ") 
    # While loop if the user entered an invalid input other than yes or no
    while choice.lower() != "yes" and choice.lower() != "no": 
        # Let the user know its invalid
        print("The choice you entered is not 'yes' or 'no'. Please try again!") 
        # Re-Ask the user if they would like to purchase annual passes
        choice = input("Would you like to purchase an annual pass from the above options (yes/no)? ") 

    # If the user chose yes
    if choice.lower() == "yes":
        # Promt the user to input the number corresponding to their desired annual pass type 
        Pass_chosen= input("Please enter the number corresponding to the desired annual pass type or enter 'quit' to finish: ")
        # enter a while loop until the user types 'quit'
        while Pass_chosen.lower() != "quit":
            # if the user did not enter a number from 1 to 3(included)
            if not Pass_chosen.isdigit() or int(Pass_chosen) not in range (1,4):
                # Display an error message if an invalid input was entered
                print("You did not enter a value from 1 to 3 or 'quit'. Please only choose from the available annual passes and try again!") 

            # If statment for the sliver annual pass
            elif Pass_chosen == "1": 
                # Promt the user to enter the quantity wished to purchase
                pass_quantity = input("How many silver annual passes would you like to purchase? ")
                # While statment for invalid inputs like strings and negative numbers 
                while not pass_quantity.isdigit() or int(pass_quantity) <= 0: 
                    # Let the user know that its an invalid input
                    print("The quantity you entered is not a number, or it is a number less than 1. Please try again!")
                    # Re-ask the user for the quantity wished to purchase 
                    pass_quantity = input("How many silver annual passes would you like to purchase? ") 
                # add the annual pass type with its quantity as a key-value pair into 'annual_pass_type_dict' dictionary
                annual_pass_type_dict[Pass_chosen] = int(pass_quantity)

             # If statment for the golden annual pass
            elif Pass_chosen == "2":
                # Promt the user to enter the quantity wished to purchase
                pass_quantity = input("How many Golden annual passes would you like to purchase? ")
                # While statment for invalid inputs like strings and negative numbers
                while not pass_quantity.isdigit() or int(pass_quantity) <= 0: 
                    # Let the user know that its an invalid input
                    print("The quantity you entered is not a number, or it is a number less than 1. Please try again!")
                    # Re-ask the user for the quantity wished to purchase 
                    pass_quantity = input("How many Golden annual passes would you like to purchase? ")
                # add the annual pass type with its quantity as a key-value pair into 'annual_pass_type_dict' dictionary   
                annual_pass_type_dict[Pass_chosen] = int(pass_quantity)

            # Final else if the cutomer chose the diamond pass
            else: 
                # Promt the user to enter the quantity wished to purchase
                pass_quantity = input("How many Diamond annual passes would you like to purchase? ") 
                # While statment for invalid inputs like strings and negative numbers
                while not pass_quantity.isdigit() or int(pass_quantity) <= 0:
                    # Let the user know that its an invalid input 
                    print("The quantity you entered is not a number, or it is a number less than 1. Please try again!") 
                    # Re-ask the user for the quantity wished to purchase
                    pass_quantity = input("How many Diamond annual passes would you like to purchase? ") 
                # add the annual pass type with its quantity as a key-value pair into 'annual_pass_type_dict' dictionary                    
                annual_pass_type_dict[Pass_chosen] = int(pass_quantity)
            # Promt the user to input the number corresponding to their desired annual pass type 
            Pass_chosen= input("Please enter the number corresponding to the desired annual pass type or enter 'quit' to finish: ") #Ask the user to re-enter the pass type desired again
    # return the 'annual_pass_type_dict' dictionary that has the annual-pass type with their corresponding quantity as a key-value pair
    return annual_pass_type_dict

# save the returned values from the 'Annual_Pass_Type_Dict()' as a variable called "annual_pass_type_dict "
annual_pass_type_dict = Annual_Pass_Type_Dict()
# define a function called "Entry_Annual()" and pass 'annual_type_list, annual_pass_type_dict, total_entry_price' as its parameters to calculate total entry and annual pass prices
def Entry_Annual(annual_type_list, annual_pass_type_dict, total_entry_price):
    # use the variable "entry_annual_price" to save the total entry price
    entry_annual_price = total_entry_price
    # iterate through the keys of the 'annual_pass_type_dict' dictionary
    for i in annual_pass_type_dict:
        # calculate the total ticket-annual-pass price by multiplying each chosen annual-pass-type prices with their corresponding quantity
        # from the 'annual_type_list'(access the each element from the list, and the third element from the tuple inside the list) and multiply it with the prices(from the 'annual_pass_type_dict' dictionary values )       
        entry_annual_calc = annual_type_list[int(i) - 1][2] * annual_pass_type_dict[i]
        # update the total ticket-annual-pass price every time the loop iterates by adding it to the previous total ticket-annual-pass price
        entry_annual_price += entry_annual_calc
    # return the total ticket-annual-pass price to use it in the subsequent functions
    return entry_annual_price
# call the function and assign it to a variable called "entry_annual_price"
entry_annual_price = Entry_Annual(annual_type_list, annual_pass_type_dict, total_entry_price)



            



# print a line before entering to experiences options 
print("--------------------------------------------EXPERIENCES---------------------------------------------------------")

# create a dictionary that contains type experience options with their corresponding price as its key-value price and call it 'Experience_type'
Experience_type = {"1-Driving Experience: AED 895 \n Choose the Driving Experience and experience Yas Island roads behind the wheel of a Ferrari! Or choose the Passenger Experience and enjoy a luxury drive.": 895,"2-VIP Experiences: AED 1995 \n Nothing beats the VIP Experience.Choose the VIP+ Experience and enjoy priority access, in addition to one adventurous Driving Experience. Or choose the VIP Experience to get exclusive benefits.": 1995,"3-Advanced Scuderia Challenge Simulator: AED 50 \n Experience firsthand what it's like to train like a Ferrari driver with our state-of-the-art racing simulators. The tickect is only valid in conjunction with an entry tickect.": 50,"4-Roof Walk Experience: AED 125 \n Get up close to the world's largest Ferrari logo and experience the stunning backdrop of Yas Island.": 125} #Create a dictionary with all the experinces types and their prices
# create a nested data structure that contains tuples(each containing a roll number, experience options and their corresponding price) inside a list and call it 'experience_choice_list'
experience_choice_list = [(1, "Driving Experience", 895), (2, "VIP Experiences", 1995), (3, "Advanced Scuderia Challenge Simulator", 50), (4, "Roof Walk Experience", 125)]
# Display the available Experience types
print("Available Extra Experiences:") 

# For loop to access each element in the Experience_type dict
for key in Experience_type:
    # Display the experiences and their prices in the dict
    print(key)

# define a function to save the experience options chosen together with the number of tickets as a dictionary
def Experience_Choice_Dict():
    # create an empty dictionary to save the corresponding number to the experience chosen with their corresponding quantity as a key-value pair and call it 'annual_pass_type_dict'
    experience_choice_dict = {}
    # Ask the user if they would like to purchase any of the available experiences
    Experience_choice = input("Would you like to have an extra ultimate experience from the above options (yes/no)? ") 
    # While loop if the user entered an invalid input other than yes or no
    while Experience_choice.lower() != "yes" and Experience_choice.lower() != "no": 
        # Let the user know its an invalid input
        print("The choice you entered is not either 'yes' or 'no'. Please choose only from (yes/no)!") 
        # Re-Ask the user if they would like to purchase any of the available experiences
        Experience_choice = input("Would you like to have an extra ultimate experience from the above options (yes/no)? ") 

    # If the user chose yes, and would like to puchase an experience type
    if Experience_choice.lower() == "yes": 
        # Promt the user to input the the desired experience type number
        Experience_chosen= input("Please enter the number corresponding to the desired Experience type, or enter 'quit' to finish: ") 
        # enter a while loop until the user enters "quit"
        while Experience_chosen.lower() != "quit":
            # check if the number entered is valid, which is only numbers between 1 and 4
            if not Experience_chosen.isdigit() or int(Experience_chosen) not in range (1,5):
                # Display an error message if an invaled input was entered 
                print("You did not enter a value from 1 to 4 or 'quit'. Please only choose from the available experience options and try again!") 

            # elif statment for the first experience type (Driving experience)
            elif Experience_chosen == "1": 
                # Promt the user to enter the quantity wished to purchase
                Experience_quantity = input("How many Driving experiences you would like to purchase? ")
                # While statment for invalid inputs like strings and negative numbers
                while not Experience_quantity.isdigit() or int(Experience_quantity) <= 0: 
                    # Let the user know that its an invalid input
                    print("The quantity you entered is not a number or lower than or equal to 0. Please try again!") 
                    Experience_quantity = input("How many Driving experiences you would like to purchase? ")
                    # Re-ask the user for the quantity wished to purchase
                # add the experience type with its quantity as a key-value pair into 'experience_choice_dict' dictionary
                experience_choice_dict[Experience_chosen] = int(Experience_quantity)


             # Elif statment for the second experience type (VIP Experience)
            elif Experience_chosen == "2":
                # Promt the user to enter the quantity wished to purchase
                Experience_quantity = input("How many VIP Experiences would you like to purchase? ") 
                # While statment for invalid inputs like strings and negative numbers
                while not Experience_quantity.isdigit() or int(Experience_quantity) <= 0: 
                    # Let the user know that its an invalid input
                    print("The quantity you entered is not a number or lower than or equal to 0. Please try again!")
                    # Re-ask the user for the quantity wished to purchase
                    Experience_quantity = input("How many VIP Experiences would you like to purchase? ") 
                # add the experience type with its quantity as a key-value pair into 'experience_choice_dict' dictionary
                experience_choice_dict[Experience_chosen] = int(Experience_quantity)


            # Elif statment for the third experience type (Advanced Scuderia Challenge Simulator)
            elif Experience_chosen == "3": 
                # Promt the user to enter the quantity wished to purchase
                Experience_quantity = input("How many Advanced Scuderia Challenge Simulator experience would you like to purchase? ")
                # While statment for invalid inputs like strings and negative numbers
                while not Experience_quantity.isdigit() or int(Experience_quantity) <= 0: 
                    # Let the user know that its an invalid input
                    print("The quantity you entered is not a number or lower than or equal to 0. Please try again!") 
                    # Re-ask the user for the quantity wished to purchase
                    Experience_quantity = input("How many Advanced Scuderia Challenge Simulator experience would you like to purchase? ") 
                # add the experience type with its quantity as a key-value pair into 'experience_choice_dict' dictionary
                experience_choice_dict[Experience_chosen] = int(Experience_quantity)

            # Final else statment for the forth experience type (Roof Walk Experience)
            else: 
                # Promt the user to enter the quantity wished to purchase
                Experience_quantity = input("How many Roof Walk Experiences would you like to purchase? ") 
                # While statment for invalid inputs like strings and negative numbers
                while not Experience_quantity.isdigit() or int(Experience_quantity) <= 0: 
                    # Let the user know that its an invalid input
                    print("The quantity you entered is not a number or lower than or equal to 0. Please try again!") 
                    # Re-ask the user for the quantity wished to purchase
                    Experience_quantity = input("How many Roof Walk Experiences would you like to purchase? ") 
            # Ask the user if they would like to purchase any of the available experiences
            Experience_chosen= input("Please enter the number corresponding to the desired Experience type, or enter 'quit' to finish: ")

    # return the 'experience_choice_dict' dictionary that has the experience type with their corresponding quantity as a key-value pair
    return experience_choice_dict


# save the returned values from the 'Experience_Choice_Dict()' as a variable called "experience_choice_dict "
experience_choice_dict = Experience_Choice_Dict()
# define a function to calculate total entry, annual pass, and experience prices
def Entry_Annual_Experience(experience_choice_list, experience_choice_dict, entry_annual_price):
    # save the total price in a variable called 'entry_annual_experience_price'
    entry_annual_experience_price = entry_annual_price
    # iterate through the keys of the 'experience_choice_dict' dictionary   
    for i in experience_choice_dict:
        # calculate the  price by multiplying each chosen experience prices with their corresponding quantity
        # from the ' experience_choice_list'(access the each element from the list, and the third element from the tuple inside the list) and multiply it with the prices(from the 'experience_choice_dict' dictionary values )       
        entry_annual_experience_calc = experience_choice_list[int(i) - 1][2] * experience_choice_dict[i]
        # update the total price every time the loop iterates by adding it to the previous total price
        entry_annual_experience_price += entry_annual_experience_calc
    # return the total ticket-annual-pass-experience price to use it in the subsequent functions
    return entry_annual_experience_price
# call the function and assign it to a variable called 'entry_annual_experience_price'
entry_annual_experience_price = Entry_Annual_Experience(experience_choice_list, experience_choice_dict, entry_annual_price)


# print a line before entering to offers options
print("--------------------------------------------OFFERS-----------------------------------------------------------")
# create a dictionary that contains a roll number and a list(that contains type of offer with a description) as its key-value pair
offer_options =  {
    '1': ['Family and Friends Offer',"25% off on entry tickets"],
    '2': ["Senior's Offer", "60% off on entry tickets"],
    '3': ['Exclusive Offer For People of Determination','Buy 1 get 1 for free'],
    '4': ['Bank or Discount Card Offer(only choose this offer, if you use one of these banks)', {
        'a': ['FAB','20% discount'],
        'b': ['ADIB','20% discount'],
        'c': ['ENBD','20% discount'],
        'd': ['RAK BANK','20% discount'],
        'e': ['FAZAA','20% discount'],
        'f': ['ESAAD','20% discount'],

        }],
    '5': ["Choose this if you are not eligible for the offers displayed", "no discounts"]
}

# iterate through each roll numbers(key) of the dictionary 'offer_options'
for item in offer_options:
    # if the user chooses 'bank or discount offer'
    if(item == '4'):
        # create a variable called 'banks' to access the banks dictionary inside the 'offer_options' dictionary
        banks = offer_options[item][1]
        # print the discount type which is 'Bank or Discount Card Offer'
        print(item,":", offer_options[item][0])
        # iterate through every banks in the 'banks' dictionary
        for bank in banks:
            # print the specific type of bank with its corresponding discount rate
            print(f'\t {bank}: {banks[bank][0]} with discount rate of 20%')
    # if the user chooses other discounts than bank offer
    else:
        # print the discount offer with their discount rate
        print(f'{item}: {offer_options[item][0]} with offer of {offer_options[item][1]}')


# define a function called "Offers()" that lets users choose their desired offer choices and return the final user choice
def Offers():
    # Ask the user if they want an offer or not
    user_input = input("Enter 'yes' if you want any of the above offers or enter 'no' if you don't: ")
    # enter a while loop to validate user's input until the user enters only either 'yes' or 'no'
    while (user_input.lower() != "yes" and user_input.lower() != "no" ):
        # print an error message to inform the user that their input is invalid and inform them to enter either 'yes' or 'no'
        print("Invalid input, Please enter only either 'yes' or 'no'.")
        # again prompt the user to enter either 'yes' or 'no'
        user_input = input("Enter 'yes' if you want any of the above offers or enter 'no' if you don't: ")

    # if the user did not want the offer
    if(user_input == 'no'):
        # print a message to inform the user that they did not select any offer
        print("You have not selected any offers")
        # return a 'None' value 
        return None

    # prompt the user to enter the number corresponding to their desired offer type 
    offer_choice = input("Choose the type of offer you want from the above offers and enter their corresponding numbers from 1 to 5: ")
    # enter a while loop until the user enters a value that satisfies the while condition
    # the followings are the conditions to check
    # the input must be between 1 and 5
    # the user can not choose 'Family and Friends Offer' if they have lessthan 4 single day tickets
    # the user can not choose 'Senior's Offer' if they have not purchased atleast one single day ticket
    while(offer_choice not in ["1", "2", "3", "4","5"]) or (((indiv_ticket_dict.get("1", 0) + indiv_ticket_dict.get("2", 0)) < 4) and (offer_choice == "1")) or (((indiv_ticket_dict.get("1", 0) == 0) and (indiv_ticket_dict.get("2", 0) == 0)) and (offer_choice == "2")):
        # print an error message and inform the user to choose another offer option
        print('Please check your input! Either you did not enter the valid numbers which are from 1 to 4 or the offer you chose is unavailable for the type/amount of ticket you purchased.')
        # prompt the user to enter the number corresponding to their desired offer type 
        offer_choice = input("Choose the type of offer you want from the above offers and enter their corresponding numbers from 1 to 5: ")

    # check if the user chose one of the 'Family and Friends Offer','Senior's Offer', or 'Exclusive Offer For People of Determination'
    if offer_choice in ["1", "2", "3"]:
        # save the user's choice in a variable called 'final_user_choice'
        final_user_choice = offer_choice
        # print a successful try message for the user 
        print('Successfully selected an offer!')

    # if the user is not eligible for the above offers and chose the "Choose this if you are not eligible for the offers displayed" options
    elif offer_choice == "5":
        # save the user's choice in a variable called 'final_user_choice'
        final_user_choice = offer_choice
        # display a message to inform the user that they have not claimed any offer
        print('You have not claimed any offers.')

    # otherwise, if the user uses one of the listed banks and chose the "Bank or Discount Card Offer"
    else:
        # print "Bank or Discount Card Offer" statement
        print(offer_options["4"][0])
        # iterate through every bank in the 'banks' dictionary
        for bank in banks:
            # print the specific banks with their corresponding alphabet and discount rate
            print(f'\t {bank}: {banks[bank][0]} with discount rate of 20%')


        # prompt the user to choose their bank choices for the discount by entering the alphabets corresponding to the banks
        bank_choice = input('Choose the bank you want from the above options and enter your choice from "a" to "f": ')
        # enter a while loop to validate the input from the user, until the user enters a valid input(from 'a' to 'f')
        while(bank_choice not in ['a','b','c','d','e','f']):
            # print an error message and inform the user to enter alphabets from 'a' to 'f'
            print("You did not enter alphabet that corresponds to the bank. Please enter options 'a' to 'f' and try again!")
            # prompt the user to choose their bank choices for the discount by entering the alphabets corresponding to the banks
            bank_choice = input('Choose the bank you want from the above options and enter your choice from "a" to "f": ')

        # if the bank choosen is in the available bank lists
        if(bank_choice in ['a','b','c','d','e','f']):
            # give the variable "final_user_choice", a value of "4"
            final_user_choice = "4"
            # print a successful try message for the user           
            print('Successfully selected an offer!')

    # return the final user choice of offer as a string
    return final_user_choice

# call the 'Offers()' function and assign it into a variable called "offers"
offers = Offers()

# define a function to calculate and return the overall total price 
def TotalPrice(entry_annual_experience_price):
    
    # create a variable called 'offerable_price' and assign to the total price of single day entry tickets
    offerable_price = (ticket_type_list[0][2] * indiv_ticket_dict.get("1", 0)) + (ticket_type_list[1][2] * indiv_ticket_dict.get("2", 0))

    # if the offer is 'Family and Friends Offer'
    if(offers == "1"):
        # decrease the offerable price by 25% and subtract it from the overall total price
        entry_annual_experience_price = entry_annual_experience_price - (0.25 * offerable_price)
    # if the offer is 'Senior's Offer'
    elif(offers == "2"):
        # decrease the offerable price by 60% and subtract it from the overall total price
        entry_annual_experience_price = entry_annual_experience_price - (0.6 * offerable_price)
    # if the offer is 'Exclusive Offer For People of Determination'
    elif(offers == "3"):
        # do not change the overall total price, it remains unchanged
        entry_annual_experience_price = entry_annual_experience_price

    # if the offer is 'Bank or Discount card offer"
    elif(offers == "4"):
        # decrease the overall total price by 20%
        entry_annual_experience_price = 0.8 * entry_annual_experience_price 

    # otherwise, if the offer is not one of the these options
    else:
        # do not change the overall total price, it remains unchanged
        entry_annual_experience_price = entry_annual_experience_price

    # return the overall total price
    return entry_annual_experience_price

# call the function and assign it to a variable called 'total_price'
total_price = TotalPrice(entry_annual_experience_price)


# print a line before printing the receipt
print("-------------------------------------------------RECEIPT-----------------------------------------------------------")
# define a function called "Receipt()" to print out receipt for the user
def Receipt():
    # iterate through every type of tickets purchased in the 'indiv_ticket_dict' dictionary
    for i in indiv_ticket_dict:
        # print the type(s) of entry ticket the user purchased
        print("Ticket type: ", ticket_type_list[int(i) - 1][1])
        # if the user chose something different from 'Exclusive Offer For People of Determination'
        if offers != "3":
            # print the total number of entry tickets from the 'indiv_ticket_dict' dictionary
            print("Number of the above type of ticket purchased: ", indiv_ticket_dict[i], "Ticket(s)")
        # if the user chose 'Exclusive Offer For People of Determination'
        else:
            # double the number of entry-tickets and print it
            print("Number of the above type of ticket purchased: ", indiv_ticket_dict[i] * 2, "Ticket(s)")

    # iterate through every annual pass ticket purchased in the 'annual_pass_type_dict' dictionary
    for i in annual_pass_type_dict:
        # print the annual pass type the user purchased
        print("Annual pass type: ", annual_type_list[int(i) - 1][1])
        # print the annual pass quantity the user purchased
        print("Number of the above annual pass type purchased: ", annual_pass_type_dict[i], "Ticket(s)")

    # iterate through every experience choice ticket purchased in the 'annual_pass_type_dict' dictionary
    for i in experience_choice_dict:
        # print the experience choice type the user purchased        
        print("Experience type: ", experience_choice_list[int(i) - 1][1])
        # print the experience quantity the user purchased       
        print("Number of the above experience type purchased: ", experience_choice_dict[i], "Experience(s)")
    
    # if the user chose "Family & Friends Offer"
    if offers == "1":
        # assign the offer to the variable "offer_display"
        offer_display = "Family & Friends Offer"
    # if the user chose "Senior's Offer"       
    elif offers == "2":
        # assign the offer to the variable "offer_display"
        offer_display = "Senior's Offer"
    # if the user chose "Exclusive Offer For People of Determination"        
    elif offers == "3":
        # assign the offer to the variable "offer_display"
        offer_display = "Exclusive Offer For People of Determination"
    # if the user chose "Bank or Discount Card Offers"
    elif offers == "4":
        # assign the offer to the variable "offer_display"     
        offer_display = "Bank or Discount Card Offers"
    # if the offer is not from the above options
    else:
        # assign 'None' to the variable "offer_display" 
        offer_display = "None"
    # display the offer type that the user has chosen
    print("Offer: ", offer_display)
    # display the total price without VAT to the user
    print("Total price (without VAT): AED ", round(total_price, 2))
    # calculate the VAT amount and display it to the user
    print("VAT (5%): AED ", round((total_price * 0.05),2))
    # calculate the total price including the VAT to display it to the user
    print("Total price (with VAT): AED ", round((total_price * 0.95), 2))

# call the function to print the receipt for the user  
Receipt()


# print a line with a thank you message to end the receipt 
print("-------------------THANK YOU FOR BOOKING WITH US----------------------")
















# grocery = [ ["milk",'10001', 6, 40],
#             ["almond",'10002',22, 40],
#             ["bread", '10003', 5, 27],
#             ["salt", '10004', 6, 5],
#             ["egg", '10005',10,100], 
#             ["banana", '10006', 6, 40],
#             ["chicken", '10007',20, 5], 
#             ["rice", '10008', 50, 14],
#             ["onion", '10009',7, 19], 
#             ["yoghurt", '10010', 6, 20],
#             ["salmon", '10011',28, 21],
#             ["tuna", '10012', 17, 26],
#             ["potato", '10013',3, 44], 
#             ["tomato", '10014', 6, 23],
#             ["lettuce", '10015',11, 2], 
#             ["pasta", '10016', 2, 4],
#             ["apple", '10017',5, 16], 
#             ["orange", '10018', 8, 70],
#             ["carrot", '10019',9, 88], 
#             ["beef", '10020', 21, 40],
#         ]
# item_list = []
# unit_price = []
# quantity = []
# id = []
# last_dict = {}
# for item in grocery:
#     print(item[0], ":", "AED", item[2])

#     item_list.append(item[0])
#     id.append(item[1])
#     unit_price.append(item[2])
#     quantity.append(item[3])
# item = input("enter item: ")
# while item.lower() != "pay":
#     if item.lower() not in item_list:
#         print("invalid")
#     else:
#         x = item_list.index(item)
#         num = input("number: ")
#         while not num.isdigit() or int(num) <= 0:
#             print("invalid") 
#             num = input("number: ")
#         #else: 
#         if int(num) >  quantity[x]:
#             print("out of stock 1")
#         else:
#             up_num = last_dict.get(item, 0)
#             up_num += int(num)
#             remainder = quantity[x] - int(num)
#             quantity[x] = remainder
#         #num = input("number: ")
#             last_dict[item] = up_num
#     item = input("enter item: ")
# print(last_dict)
