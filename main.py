'''this .py file contains the main function that gives the selection options to the users
by calling the functions required for it'''

from read import read_products
from operation import sell_product, buy_product

def main():
        
    """ Summary: Main function that provides the menu options for the WeCare system admin.
        It allows users to sell products, buy/restock products, or exit the system.
        Parameters: None
        Variables: choice (int): User's menu selection (1, 2, or 3)
                   product_dict (dict): Dictionary containing product data
        Returns: None
        Raises: handles ValueError """
    
    print("\n----------------------------- Welcome to the System Admin of WeCare! -----------------------------")
    while True:
        print("\n\n--------------------------------------------------------------------------------------------------")
        print("Given below are some of the options for you to carryout in the system: ")
        print("\nPress 1: sell the products to customers ")
        print("Press 2: buy/restock the products from suppliers ")
        print("Press 3: exit from the system ")
        print("--------------------------------------------------------------------------------------------------\n")
        #user inputs an int value which is compared by the if statements 
        try:
            choice=int(input("\nEnter the option to continue: "))
            if choice==1:
                product_dict=read_products()
                sell_product(product_dict)
            elif choice==2:
                product_dict=read_products()
                buy_product(product_dict)
            elif choice==3:
                print("\nThank you for using the System Admin of WeCare! ")
                break
            else:
                print("Invalid option. Please enter 1, 2, or 3")
        except ValueError:
            print("Invalid input, please enter only a number") #exception handling 

main()
