# def Grocery_List():
#     grocery = [ ["milk",'10001', 6, 40],
#                 ["almond",'10002',22, 40],
#                 ["bread", '10003', 5, 27],
#                 ["salt", '10004', 6, 5],
#                 ["egg", '10005',10,100], 
#                 ["banana", '10006', 6, 40],
#                 ["chicken", '10007',20, 5], 
#                 ["rice", '10008', 50, 14],
#                 ["onion", '10009',7, 19], 
#                 ["yoghurt", '10010', 6, 20],
#                 ["salmon", '10011',28, 21],
#                 ["tuna", '10012', 17, 26],
#                 ["potato", '10013',3, 44], 
#                 ["tomato", '10014', 6, 23],
#                 ["lettuce", '10015',11, 2], 
#                 ["pasta", '10016', 2, 4],
#                 ["apple", '10017',5, 16], 
#                 ["orange", '10018', 8, 70],
#                 ["carrot", '10019',9, 88], 
#                 ["beef", '10020', 21, 40],
#             ]
#     org_dict = {"milk" : 40}
#     item_list = []
#     unit_price = []
#     quantity = []
#     id = []
#     for item in grocery:
#         print(item[0], ":", "AED", item[2])

#         item_list.append(item[0])
#         id.append(item[1])
#         unit_price.append(item[2])
#         quantity.append(item[3])

#     return item_list, id, unit_price, quantity


# grocery_in_stock = list(Grocery_List())

# # print(grocery_in_stock)
# # print(type(grocery_in_stock))
# # print(grocery_in_stock[0])


# def Take_Order():
#     org_dict = {"milk" : 40}
#     item = []
#     quantity = []
#     last_quantity = {}
#     item_name = input("Please enter the item you want to purchase or enter 'pay' to complete the order: ")
#     while (item_name.lower() != "pay"):
#         if (item_name.lower() in grocery_in_stock[0]):
#             x = grocery_in_stock[0].index(item_name.lower())
#             if item_name.lower() == org_dict.keys():
#                 grocery_in_stock[3][x] = org_dict[item_name.lower()]
#             else:
#                 item.append(item_name.lower())
#                 x = grocery_in_stock[0].index(item_name.lower())
#                 item_quantity = input("Please enter the quantity of the item you want to purchase: ")
#                 while ((not item_quantity.isdigit()) or (int(item_quantity) <= 0)):
#                     print("You did not enter a positive number, please try again!")
#                     item_quantity = input("Please enter the quantity of the item you want to purchase: ")            

#                 while (int(item_quantity) > grocery_in_stock[3][x]):
#                     if (grocery_in_stock[3][x] <= 0):
#                         print(grocery_in_stock[3][x])
#                         print(f"Sorry, {item_name} is out of stock, please try another one.")
#                     else: 
#                         print(f" Sorry, you exceeded the stock amount available. \n We only have {grocery_in_stock[3][x]} {item_name}(s) in stock, Please enter another quantity and try again: ")
#                     item_quantity = input("Please enter the quantity of the item you want to purchase: ")
            
#                 last_quantity[item_name.lower()] = int(item_quantity)
#                 grocery_in_stock[3][x] -= int(item_quantity)
#                 print('left', grocery_in_stock[3][x])

#                 quantity.append(int(item_quantity))
#                 print('ordered quantity', int(item_quantity))
#         else :
#             print("Sorry,the entered item is not available, please enter another item! ")
#         item_name = input("Please enter the item you want to purchase or enter 'pay' to complete the order: ")

#     for item_name, quant in last_quantity.items():
#         x = grocery_in_stock[0].index(item_name)
#         grocery_in_stock[3][x] -= quant
#         print('left in stock:', grocery_in_stock[3][x])

#     item_quantity_order = dict(zip(item,quantity))
#     return item_quantity_order



        
# customer_order = Take_Order()


# def Calculate_Order(item_list, unit_price_list, quant,item_quantity_order):
#     orders = []
#     for item_name, quant in item_quantity_order.items():

#         index = item_list.index(item_name)
#         unit_price = unit_price_list[index]
#         total_price = unit_price * quant
        
#         orders.append((item_name, unit_price, quant, total_price))
#     print(orders)

# order_details = Calculate_Order(grocery_in_stock[0], grocery_in_stock[2], grocery_in_stock[3], customer_order)

# # for item in order_details:
# #     print(f"Item: {item[0]}\n Unit Price: {item[1]} AED\n Quantity: {item[2]}\n Total Price: {item[3]} AED")




# def Grocery_List():
#     grocery = [ ["milk",'10001', 6, 40],
#                 ["almond",'10002',22, 40],
#                 ["bread", '10003', 5, 27],
#                 ["salt", '10004', 6, 5],
#                 ["egg", '10005',10,100], 
#                 ["banana", '10006', 6, 40],
#                 ["chicken", '10007',20, 5], 
#                 ["rice", '10008', 50, 14],
#                 ["onion", '10009',7, 19], 
#                 ["yoghurt", '10010', 6, 20],
#                 ["salmon", '10011',28, 21],
#                 ["tuna", '10012', 17, 26],
#                 ["potato", '10013',3, 44], 
#                 ["tomato", '10014', 6, 23],
#                 ["lettuce", '10015',11, 2], 
#                 ["pasta", '10016', 2, 4],
#                 ["apple", '10017',5, 16], 
#                 ["orange", '10018', 8, 70],
#                 ["carrot", '10019',9, 88], 
#                 ["beef", '10020', 21, 40],
#             ]

#     item_list = []
#     unit_price = []
#     quantity = []
#     id = []
#     for item in grocery:
#         print(item[0], ":", "AED", item[2])

#         item_list.append(item[0])
#         id.append(item[1])
#         unit_price.append(item[2])
#         quantity.append(item[3])

#     return item_list, id, unit_price, quantity

# item_list, id, unit_price, quantity = Grocery_List()



# def Take_Order():
#     item = []
#     quantity = []
#     last_quantity = {}
#     order_name = input("Please enter the item you want to purchase or enter 'pay' to complete the order: ")
#     while (order_name.lower() != "pay"):
#         if (order_name.lower() in item_list):
#             item.append(order_name.lower())

#             x = item_list.index(order_name.lower())
#             order_quantity = input("Please enter the quantity of the item you want to purchase: ")
#             while (order_quantity <= 0 or order_quantity >= quantity[x]):
#                 print(f" Sorry, we have only {quantity[x]} {order_name}(s) in stock, Please enter another quantity and try again: ")
#                 order_quantity = int(input("Please enter the quantity of the item you want to purchase: "))
            
#             last_quantity[order_name.lower()] = order_quantity
#             # grocery_in_stock[3][x] -= item_quantity
#             # print('left', grocery_in_stock[3][x])

#             quantity.append(order_quantity)
#             print('ordered quantity', order_quantity)
#         else :
#             print("Sorry,the entered item is not available, please enter another item: ")
#         order_name = input("Please enter the item you want to purchase or enter 'pay' to complete the order: ")

#     for order_name, quant in last_quantity.items():
#         x = item_list.index(order_name)
#         quantity[x] -= quant
#         # print('left in stock:', grocery_in_stock[3][x])

#     item_quantity_order = dict(zip(item,quantity))
#     return item_quantity_order



        
# customer_order = Take_Order()


# def Calculate_Order(item_list, unit_price_list, quant,item_quantity_order):
#     orders = []
#     for item_name, quant in item_quantity_order.items():

#         index = item_list.index(item_name)
#         unit_price = unit_price_list[index]
#         total_price = unit_price * quant
        
#         orders.append((item_name, unit_price, quant, total_price))
#     print(orders)

# order_details = Calculate_Order(item_list , unit_price, quantity , customer_order)

# # for item in order_details:
# #     print(f"Item: {item[0]}\n Unit Price: {item[1]} AED\n Quantity: {item[2]}\n Total Price: {item[3]} AED")











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
    for item in grocery:
        print(item[0], ":", "AED", item[2])

        item_list.append(item[0])
        id.append(item[1])
        unit_price.append(item[2])
        quantity_list.append(item[3])

    return item_list, id, unit_price, quantity_list

item_list, id, unit_price, quantity_list = Grocery_List()



def Take_Order():
    item = []
    quantity = []
    last_dict = {"milk": 0, "almond": 0, "bread": 0 , "salt": 0, "egg": 0, "banana": 0, "chicken": 0, "chicken": 0, "onion":0, "yoghurt": 0, "salmon": 0, "tuna": 0, "potato": 0, "tomato": 0, "lettuce": 0, "pasta": 0, "apple": 0, "orange": 0, "carrot": 0, "beef": 0}
    order_name = input("Please enter the item you want to purchase or enter 'pay' to complete the order: ")
    while (order_name.lower() != "pay"):
        if (order_name.lower() in item_list):
            item.append(order_name.lower())

            x = item_list.index(order_name.lower())
            print(x)
            



            order_quantity = input("Please enter the quantity of the item you want to purchase: ")
            while ((not order_quantity.isdigit()) or (int(order_quantity) <= 0) or int(order_quantity) > quantity_list[x]):
                if ((not order_quantity.isdigit()) or (int(order_quantity) <= 0)):
                    print("Please enter a positive number and try again! ")
                elif (int(order_quantity) > quantity_list[x]):
                    print(f" Sorry, we have only {quantity_list[x]} {order_name}(s) in stock, Please enter a smaller quantity and try again: ")
                order_quantity = input("Please enter the quantity of the item you want to purchase: ")

            while (quantity_list[x] <= 0):
                print(f"Sorry,{order_name} is currently out of stock, please another item.")
                order_name = input("Please enter the item you want to purchase or enter 'pay' to complete the order: ")
                break
            
            
            last_dict[order_name.lower()] += int(order_quantity)
            for key in last_dict:
                if(last_dict[key] != 0 and int(order_quantity <= quantity_list[x])):
                    quantity.append(last_dict[key])
                    print('ordered quantity', quantity)



        else :
            print("Sorry,the entered item is not available, please enter another item: ")
        order_name = input("Please enter the item you want to purchase or enter 'pay' to complete the order: ")

    for order_name, quant in last_dict.items():
        x = item_list.index(order_name)
        quantity_list[x] -= quant


    item_quantity_order = dict(zip(item,quantity))
    return item_quantity_order



        
customer_order = Take_Order()


def Calculate_Order(item_list, unit_price_list, quant,item_quantity_order):
    orders = []
    for item_name, quant in item_quantity_order.items():

        index = item_list.index(item_name)
        unit_price = unit_price_list[index]
        total_price = unit_price * quant
        
        orders.append((item_name, unit_price, quant, total_price))
    print(orders)

order_details = Calculate_Order(item_list , unit_price, quantity_list , customer_order)

# for item in order_details:
#     print(f"Item: {item[0]}\n Unit Price: {item[1]} AED\n Quantity: {item[2]}\n Total Price: {item[3]} AED")


