#this .py file contains the main operation and logic behind selling and purchasing products

from read import display_products
from write import rewrite_products, create_sale_invoice, create_purchase_invoice

def sell_product(product_dict):
    
    """ Summary:Handles the product selling process including user input validation, stock updates, and invoice generation.
        Parameters: product_dict (dict): Dictionary containing current product data
        Variables: name (str): Customer name
                   phone (str): Customer phone
                   details (dict): Sale details dictionary
                   product_id (int): Selected product ID
                   quantity (int): Quantity to sell
                   stock (int): Current product stock
                   free_items (int): Free items from the offer of store
                   total_needed (int): Total items to deduct (quantity + free)
                   unit_price (int): Calculated selling price
                   total (int): Line item total

        Returns: None
        Raises: None (handles exceptions internally) """
    
    display_products(product_dict)
    try: #the user inputs are taken and validated 
        name=input("\nEnter the name of the Customer: ")
        if not name.isalpha():
            print("Invalid name, please enter only letters")
            return
        
        phone=input("Enter the phone number of the customer: ")
        if not phone.isdigit():
            print("Invalid phone number, please enter only digits")
            return
        
        #a dictionary is made which has the keys as name, phone and items (arraylist)
        details = {'name': name, 'phone': phone, 'items': []}
        
        while True:
            try:
                product_id=int(input("Enter product ID to sell or press 0 to stop: "))
                if product_id == 0:
                    break
                if product_id not in product_dict:
                    print("Invalid product ID")
                    continue

                '''the entered quantity is compared to being:
                    1. more than stock
                    2. more than stock due to offer
                    3. less or equal to zero'''
                
                quantity=int(input("Enter quantity to sell: "))
                if quantity <= 0:
                    print("Quantity must be a positive number")
                    continue

                if quantity > product_dict[product_id][2]:
                    print ("Not enough stock")
                    continue
            
                stock=product_dict[product_id][2]
                free_items=quantity // 3
                total_needed=quantity + free_items
                
                if total_needed > stock:
                    print("The quantity to sell is not enough due to our offer")
                    continue
                
                #the values are then appended to the items arraylist
                
                product_dict[product_id][2] -= total_needed
                unit_price = (product_dict[product_id][3]*200)//100
                total = unit_price * quantity
                details['items'].append({
                    'name': product_dict[product_id][0], 
                    'brand': product_dict[product_id][1],
                    'quantity': quantity, 
                    'free': free_items, 
                    'price': unit_price, 
                    'total': total,
                    'origin': product_dict[product_id][4]
                })
            except ValueError:
                print("Invalid input, please enter only numbers")
        
        if len(details['items']) > 0:
            #calling the create_sale_invoice and rewrite_products for billing and rewriting to the file
            create_sale_invoice(details)
        rewrite_products(product_dict)
    except:
        print("An error occurred during selling")

def buy_product(product_dict):
    
    """ Summary: Handles the product restocking process including user input validation, stock updates, and invoice generation.
        Parameters: product_dict (dict): Dictionary containing current product data
        Variables: name (str): Supplier name
                   phone (str): Supplier phone
                   details (dict): Purchase details dictionary
                   product_id (int): Selected product ID
                   quantity (int): Quantity to restock
                   total (int): Line item total

        Returns: None
        Raises: None (handles exceptions internally) """
    
    display_products(product_dict)
    try: #the user inputs are taken and validated 
        name=input("\nEnter the name of the Supplier: ")
        if not name.isalpha():
            print("Invalid name, please enter only letters")
            return
        
        phone=input("Enter the phone number of the Supplier: ")
        if not phone.isdigit():
            print("Invalid phone number, please enter only digits")
            return
        
        #a dictionary is made which has the keys as name, phone and items (arraylist)
        details= {'name': name, 'phone': phone, 'items': []}
        
        while True:
            try:
                product_id=int(input("Enter product ID to restock or press 0 to stop: "))
                if product_id == 0:
                    break
                if product_id not in product_dict:
                    print("Invalid product ID")
                    continue
                
                quantity=int(input("Enter quantity to restock: "))
                if quantity <= 0:
                    print("Quantity must be a positive number")
                    continue

                #the values are then appended to the items arraylist
                product_dict[product_id][2] += quantity
                product_dict[product_id][3] 
                total = product_dict[product_id][3] * quantity
                details['items'].append({
                    'name': product_dict[product_id][0], 
                    'brand': product_dict[product_id][1],
                    'quantity': quantity, 
                    'price': product_dict[product_id][3], 
                    'total': total,
                    'origin': product_dict[product_id][4]
                })
            except ValueError:
                print("Invalid input, please enter only numbers")
        
         #calling the create_purchase_invoice and rewrite_products for billing and rewriting to file
        if len(details['items']) > 0:
            create_purchase_invoice(details)
        rewrite_products(product_dict)
    except:
        print("An error occurred during restocking")

