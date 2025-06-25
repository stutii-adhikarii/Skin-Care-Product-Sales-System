import datetime
import random

'''this .py file contains all the code needed for writing to the file and printing in the console.
It contains code for:
1. creating a unique filename for each txt invoice
2. writing the updated product details to the store.txt file
3. code for creating sale invoice and purchase invoice as well as printing it to idle shell'''

def new_filename():
    
    """ Summary: Generates a unique filename for invoices using current datetime and random number.
        Parameters: None
        Variables: now (datetime): Current datetime
                   date_part (str): Date components 
                   time_part (str): Time components 
                   random_num (int): Random number between 1-100
        Returns (str): Unique filename
        Raises: None """
    
    now=datetime.datetime.now() #using the datetime package for the date and time part of invoice  
    date_part= str(now.year) + str(now.month) + str(now.day)
    time_part= str(now.hour) + str(now.minute) + str(now.second)
    random_num= random.randint(1, 100) #using the random package for generating random num from 1 to 100
    return "Invoice_" + date_part + "_" + time_part + "_" + str(random_num) + ".txt"

def rewrite_products(product_dict):
    
    """ Summary: Writes updated product data back to 'store.txt' file.
        Parameters: product_dict (dict): Dictionary containing updated product data
        Variables: lines (list): List of product strings to write
                   line (str): Formatted product string
                   file (file object): File handler for store.txt
        Returns: None
        Raises: None (handles exceptions internally) """
    try:
        #storing the updated details in the arraylist and then writing to the file 
        lines=[]
        for product in product_dict.values():
            line=product[0] + ',' + product[1] + ',' + str(product[2]) + ',' + str(product[3]) + ',' + product[4]
            lines.append(line)
        file=open('store.txt', 'w')
        for line in lines:
            file.write(line + '\n')
        file.close()
    except:
        print("Error writing products to file")

def create_sale_invoice(details):

    """ Summary: Creates and saves a sales invoice file, and prints it to console.
        Parameters: details (dict): Dictionary containing keys as name, phone, items []
        Variables: filename (str): Generated invoice filename
                   f (file object): Invoice file handler
                   same_items (dict): Items dictionary
                   key (str): Unique key for same items
                   grand_total (int): Total sale amount
                   item (dict): Individual product details
        Returns: None
        Raises: None (handles exceptions internally) """
    
    #for writing the invoice to the txt file
    
    filename=new_filename()
    try:
        f=open(filename, 'w')
        f.write("------------------------------- Wecare Pvt. Ltd -------------------------------\n")
        f.write("Transaction Type: SALE\n")
        f.write("Customer Name: " + details['name'] + '\n')
        f.write("Contact number: " + details['phone'] + '\n')
        f.write("Date and time of transaction: " + str(datetime.datetime.now()) + '\n')
        f.write("-------------------------------------------------------------------------------\n")
        f.write("\n")
        f.write("ProductName       Brand        Quantity  Free   UnitPrice   Origin      Total\n")
        
        #for checking if the same product is bought twice seperately and billing it by adding it as one item 
        same_items={}
        for item in details['items']:
            key= item['name'] + item['brand'] + str(item['price']) + item['origin']
            if key in same_items:
                same_items[key]['quantity'] += item['quantity']
                same_items[key]['free'] += item['free']
                same_items[key]['total'] += item['total']
            else:
                same_items[key]=item
        
        grand_total=0
        #adding the spacing by the length of string 
        for item in same_items.values():
            name= item['name'] + ' ' * (18 - len(item['name']))
            brand= item['brand'] + ' ' * (13 - len(item['brand']))
            quantity= str(item['quantity']) + ' ' * (10 - len(str(item['quantity'])))
            free= str(item['free']) + ' ' * (7 - len(str(item['free'])))
            price= str(item['price']) + ' ' * (12 - len(str(item['price'])))
            origin= item['origin'] + ' ' * (12 - len(item['origin']))
            total= str(item['total'])
            f.write(name + brand + quantity + free + price + origin + total + '\n')
            grand_total += item['total']
        f.write("\n-------------------------------------------------------------------------------")
        f.write("\nGrand Total: Rs. " + str(grand_total) + '\n')
        f.write("-------------------------------------------------------------------------------\n")
        f.close()
    except:
        print("Error creating sale invoice file")


#for printing in the idle shell 
    print("\n\n\n------------------------------- Wecare Pvt. Ltd -------------------------------")
    print("Transaction Type: SALE")
    print("Customer Name: " + details['name'])
    print("Contact number: " + details['phone'])
    now=datetime.datetime.now()
    print("Date and time of transaction: " + str(now.year) + "-" + str(now.month) + "-" + 
          str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    print("-------------------------------------------------------------------------------")
    print("\n")
    print("ProductName       Brand        Quantity  Free   UnitPrice   Origin      Total")
    
    for item in same_items.values():
        name= item['name'] + ' ' * (18 - len(item['name']))
        brand= item['brand'] + ' ' * (13 - len(item['brand']))
        quantity= str(item['quantity']) + ' ' * (10 - len(str(item['quantity'])))
        free= str(item['free']) + ' ' * (7 - len(str(item['free'])))
        price= str(item['price']) + ' ' * (12 - len(str(item['price'])))
        origin= item['origin'] + ' ' * (12 - len(item['origin']))
        total= str(item['total'])
        print(name + brand + quantity + free + price + origin + total)
    print("\n-------------------------------------------------------------------------------")
    print("\nGrand Total: Rs. " + str(grand_total))
    print("-------------------------------------------------------------------------------\n\n")

def create_purchase_invoice(details):
    
    """ Summary: Creates and saves a purchase invoice file, and prints it to console.
        Parameters: details (dict): Dictionary containing keys as name, phone, items []
        Variables: filename (str): Generated invoice filename
                   f (file object): Invoice file handler
                   same_items (dict): Items dictionary
                   key (str): Unique key for same items
                   grand_total (int): Subtotal before VAT
                   vat (int): 13% VAT amount
                   item (dict): Individual product details
       Returns: None
       Raises: None (handles exceptions internally) """
    
    #for writing the invoice in the txt file

    filename=new_filename()
    try:
        f=open(filename, 'w')
        f.write("------------------------------- Wecare Pvt. Ltd -------------------------------\n")
        f.write("Transaction Type: PURCHASE\n")
        f.write("Supplier Name: " + details['name'] + '\n')
        f.write("Contact number: " + details['phone'] + '\n')
        f.write("Date and time of transaction: " + str(datetime.datetime.now()) + '\n')
        f.write("-------------------------------------------------------------------------------\n")
        f.write("\n")
        f.write("ProductName       Brand        Quantity  UnitPrice   Origin      Total\n")
        
        #for checking if the same product is bought twice seperately and billing it by adding it as one item 
        same_items={}
        for item in details['items']:
            key= item['name'] + item['brand'] + str(item['price']) + item['origin']
            if key in same_items:
                same_items[key]['quantity'] += item['quantity']
                same_items[key]['total'] += item['total']
            else:
                same_items[key]=item
        
        grand_total=0
        #adding the spacing by the length of string
        for item in same_items.values():
            name= item['name'] + ' ' * (18 - len(item['name']))
            brand= item['brand'] + ' ' * (13 - len(item['brand']))
            quantity= str(item['quantity']) + ' ' * (10 - len(str(item['quantity'])))
            price= str(item['price']) + ' ' * (12 - len(str(item['price'])))
            origin= item['origin'] + ' ' * (12 - len(item['origin']))
            total= str(item['total'])
            f.write(name + brand + quantity + price + origin + total + '\n')
            grand_total += item['total']
        
        vat=grand_total * 13 // 100
        f.write("\n-------------------------------------------------------------------------------")
        f.write("\nSub Total: Rs. " + str(grand_total) + '\n')
        f.write("VAT (13%): Rs. " + str(vat) + '\n')
        f.write("Grand Total: Rs. " + str(grand_total + vat) + '\n')
        f.write("-------------------------------------------------------------------------------\n")
        f.close()
    except:
        print("Error creating purchase invoice file")
        
#for printing in the idle shell
    print("\n\n\n------------------------------- Wecare Pvt. Ltd -------------------------------")
    print("Transaction Type: PURCHASE")
    print("Supplier Name: " + details['name'])
    print("Contact number: " + details['phone'])
    now=datetime.datetime.now()
    print("Date and time of transaction: " + str(now.year) + "-" + str(now.month) + "-" + 
          str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    print("-------------------------------------------------------------------------------")
    print("\n")
    print("ProductName       Brand        Quantity  UnitPrice   Origin      Total")
    
    for item in same_items.values():
        name= item['name'] + ' ' * (18 - len(item['name']))
        brand= item['brand'] + ' ' * (13 - len(item['brand']))
        quantity= str(item['quantity']) + ' ' * (10 - len(str(item['quantity'])))
        price= str(item['price']) + ' ' * (12 - len(str(item['price'])))
        origin= item['origin'] + ' ' * (12 - len(item['origin']))
        total= str(item['total'])
        print(name + brand + quantity + price + origin + total)
    
    vat=grand_total * 13 // 100
    print("\n-------------------------------------------------------------------------------")
    print("\nSub Total: Rs. " + str(grand_total))
    print("VAT (13%): Rs. " + str(vat))
    print("Grand Total: Rs. " + str(grand_total + vat))
    print("-------------------------------------------------------------------------------\n\n")
