def Grocery_List():
    grocery = [ ["milk",'10001', 6, 40],
                ["almond",'10002',22, 40],
                ["bread", '10003', 5, 27],
                ["salt", '10004', 6, 5],
                ["egg", '10005',10,100], 
                ["banana", '10006', 6, 40],
                ["chicken", '10007',20, 5], 
                ["rice", '10008', 50, 14],
                ["onion", '10009',7, 19], 
                ["yoghurt", '10010', 6, 20],
                ["salmon", '10011',28, 21],
                ["tuna", '10012', 17, 26],
                ["potato", '10013',3, 44], 
                ["tomato", '10014', 6, 23],
                ["lettuce", '10015',11, 2], 
                ["pasta", '10016', 2, 4],
                ["apple", '10017',5, 16], 
                ["orange", '10018', 8, 70],
                ["carrot", '10019',9, 88], 
                ["beef", '10020', 21, 40],
            ]

    item_list = []
    unit_price = []
    quantity_list = []
    id = []
    print("Welcome to our online grocery shopping!")
    print("Groceries in stock: ")
    for item in grocery:
        print(item[0], ":", "AED", item[2])

        item_list.append(item[0])
        id_list.append(item[1])
        unit_price.append(item[2])
        quantity_list.append(item[3])

    return item_list, id, unit_price, quantity_list

item_list, id_list, unit_price_list, quantity_list = Grocery_List()



def TakeOrders():
    item = []
    final_dict = {}
    ordered_item = input("Please enter the item you want to purchase or enter 'pay' to complete the order: ")
    while (ordered_item.lower() != "pay"):
        if (ordered_item.lower() not in item_list):
            print("Sorry,the entered item is not available, please enter another item: ")

        else :
            x = item_list.index(ordered_item.lower())
            item.append(ordered_item.lower())

            ordered_quantity = input("Please enter the quantity of the item you want to purchase: ")
            while ((not ordered_quantity.isdigit()) or (int(ordered_quantity) <= 0)):
                print("Please enter a positive number and try again! ")
                ordered_quantity = input("Please enter the quantity of the item you want to purchase: ")

            if(int(ordered_quantity) > quantity_list[x]):
                print(f" Sorry, There is only {quantity_list[x]} quantity of {ordered_item}(s) is in stock, Please try another one!  ")

            else:
                updated_quantity = final_dict.get(ordered_item, 0)
                updated_quantity += int(ordered_quantity)
                remainder = quantity_list[x] - int(ordered_quantity)
                quantity_list[x] = remainder
                final_dict[ordered_item] = updated_quantity
        ordered_item = input("Please enter the item you want to purchase or enter 'pay' to complete the order: ")

    print(final_dict)
    return final_dict   
customer_order = TakeOrders()
    


def Calculate_Order(item_list, unit_price_list, final_dict):
    orders = []
    for ordered_item in final_dict:
        updated_quantity = final_dict[ordered_item]


        index = item_list.index(ordered_item)
        unit_price = unit_price_list[index]
        total_price = unit_price * updated_quantity
        
        orders.append((ordered_item, unit_price, updated_quantity, total_price))
    print(orders)
    return orders

orders = Calculate_Order(item_list , unit_price_list , customer_order)





def Initial_Total_Bill(orders):
    initial_total_bill = sum(orders[i][3] for i in range(len(orders)))
        
    print(initial_total_bill)
    return initial_total_bill

initial_total_bill = Initial_Total_Bill(orders)



def Customer_Info():
    name = input("Please enter your name: ")
    while (len(name) == 0):
        print("You did not enter your name. Please try again!")
        name = input("Please enter your name: ")

    credit_card = input("Please enter your credit card number. Make sure it is 16-digits: ")
    while not credit_card.isdigit() or len(credit_card) != 2:
        print("You either did not enter numbers or the number you entered is not 16 digits long. Please enter a valid 16-digit credit card number.")
        credit_card = input("Please enter your credit card number. Make sure it is 16-digit: ")
    print(name, credit_card)
    return name, credit_card

name, credit_card = Customer_Info()




def Delivery(emirate):
    if emirate.lower() == "abu dhabi":
        return 5
    elif emirate.lower() == "al ain":
        return 10
    else:
        return 20
delivery = input("Do you want delivery (yes/no)? ")
while delivery.lower() != "yes" and delivery.lower() != "no":
    print("You neither enter 'yes' nor 'no'. Please try again!")
    delivery = input("Do you want delivery (yes/no)? ")
if delivery.lower() == "yes":
    emirate = input("Please enter the emirate you want your items to be delivered to: ")
    while emirate.lower() not in ["abu dhabi", "dubai", "sharjah", "ajman", "umm al quwain", "ras al khaimah", "fujairah", "al ain"]:
        print("The emirate you entered is not correct. Please enter a valid input.")
        emirate = input("Please enter the emirate you want your items to be delivered to: ")
    delivery_amount = Delivery(emirate)
else:
    delivery_amount = 0



def Discount(initial_total_bill, delivery_amount, orders):
    total = initial_total_bill + delivery_amount
    quantity = sum(orders[i][2] for i in range(len(orders)))
    fazza = input("Do you use Fazza (yes/no)? ")
    while fazza.lower() != "yes" and fazza.lower() != "no":
        print("You neither entered 'yes' nor 'no'. Please try again.")
        fazza = input("Do you use Fazza (yes/no)? ")
    print("----Discounts available to you----")
    if quantity > 5:
        print("D1- 10% discount since you bought more than 5 items.")
    if total > 200:
        print("D2- 20% discount since the total price of the items you purchased and the services is more than 200 AED.")
    if fazza.lower() == "yes":
        print("D3- 15% discount since you used Fazza.")
    if quantity > 5 or total > 200 or fazza.lower() == "yes":
        discount_response = input("Do you want any of the above discounts (yes/no)? ")
        while discount_response.lower() != "yes" and discount_response.lower() != "no":
            print("You neither entered 'yes' nor 'no'. Please try again.")
            discount_response = input("Do you want any of the above discounts (yes/no)? ")
        if discount_response.lower() == "yes":
            discount_type = input("Please enter one of the available discount types (D1, D2, D3): ")
            while discount_type not in ['D1', 'D2', 'D3']:
                print("You did not enter input from (D1, D2, D3). Please try again.")
                discount_type = input("Please enter one of the available discount types (D1, D2, D3): ")

            if(discount_type == "D1"):
                upgraded_total = total * 0.9
                discount_percent = 10
            elif(discount_type == "D2"):
                upgraded_total = total * 0.8
                discount_percent = 20
            else:
                upgraded_total = total * 0.85
                discount_percent = 15

        else:
            upgraded_total = total
        VAT_price = 0.05 * upgraded_total
        total_price = upgraded_total + VAT_price
        print(total_price, "AED",upgraded_total, "AED", VAT_price, "AED", discount_percent, "%")
    return total_price, upgraded_total, VAT_price, discount_percent

total_price, upgraded_total, VAT_price, discount_percent = Discount(initial_total_bill, delivery_amount, orders)



import pandas as pd
payment = [name, credit_card, total_price]
invoice = [[orders], [payment]]
def Print_Invoice(order, payment, emirate, delivery_amount, discount_percent):
    print("----------Order Details----------")
    invoice_print = pd.DataFrame(data = order, columns = ["Item Type", "Unit Price", "Quantity", "Price"], index = range(1, len(order) + 1))
    print(invoice_print)
    print("----------Payment Details----------")
    print("Customer name: ", payment[0])
    print("Delivery to ", emirate)
    print("Delivery fee: AED ", round(delivery_amount, 2))
    print("Discount percent: ", discount_percent, "%")
    print("Total price without VAT: AED ", round(upgraded_total))
    print("VAT (5%): AED ", round(VAT_price, 2))
    print("Total price with VAT: AED ", round(total_price, 2))
    print("Thank you for purchasing with us!")
Print_Invoice(orders, payment, emirate, delivery_amount, discount_percent)







