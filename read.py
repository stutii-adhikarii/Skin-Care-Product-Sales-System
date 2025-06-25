#this .py file contains the code required for reading from txt file and displaying it in a tabular format

def read_products():
    
    """ Summary: Reads product data from 'store.txt' file and returns it as a dictionary.
        Parameters: None
        Variables: product_dict (dict): Dictionary to store product data
                   file (file object): File handler for store.txt
                   lines (list): List of lines from the file
                   product_id (int): Counter for product IDs
                   line (str): Single line from file
                   info (list): Split product information
        Returns (dict): Product dictionary with key as product_id or returns empty dictionary if error occurs 
        Raises: None (handles exceptions internally) """
    
    product_dict={} #creating a dictionary products_dict which has id as the key  
    try:
        file=open('store.txt', 'r')
        lines=file.read().split('\n') 
        file.close()
        product_id=1
        #looping through the array which was seperated by '\n' and storing it in dictionary by spliting by ','
        for line in lines:  
            if line != '':
                info=line.split(',')
                product_dict[product_id]=[info[0], info[1], int(info[2]), int(info[3]), info[4]]
                product_id += 1
        return product_dict
    except:
        print("Error reading products from file")
        return {}

def display_products(product_dict):
    
    """ Summary: Displays all products in a formatted table in the console.
        Parameters: product_dict (dict): Dictionary containing product data
        Variables: key (int): Product ID
                   value (list): Product details [name, brand, quantity, price, origin]
                   id_str (str): String representation of product ID
                   qty_str (str): String representation of quantity
                   selling_price (str): String representation of calculated price
        Returns: None
        Raises: None """
    
    #for displaying in the idle shell 
    print("\nHere are all the products available in WeCare:")
    print('-' * 65)
    print("ID  ProductName       Brand      Quantity   Price   Origin  ")
    print('-' * 65)
    #loops through all key, value pairs and displays it with spacing calculated by the string length
    for key, value in product_dict.items():
        id_str=str(key)
        print(id_str + ' ' * (3 - len(id_str)), end=' ')
        print(value[0] + ' ' * (17 - len(value[0])), end=' ')
        print(value[1] + ' ' * (13 - len(value[1])), end=' ')
        qty_str=str(value[2])
        print(qty_str + ' ' * (8 - len(qty_str)), end=' ')
        selling_price=str((value[3]*200)//100)
        print(selling_price + ' ' * (7 - len(selling_price)), end=' ')
        print(value[4] + ' ' * (9 - len(value[4])))
    print('-' * 65)

