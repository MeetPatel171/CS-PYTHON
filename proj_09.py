#####################################################
# cse 231 project 09
#
# import csv
# set variables for MENU & WELCOME
# open_file function
# read_file function
#  algorithm
# add_prices function
#   algorithm
# get_max_price_of_company function
#   algorithm
# get_max_company_price function
#   algorithm
# get_avg_price_of_company function
#   algorithm
# display_lst function
#   algorithm
# main function
#   main algorithm
#   call and use all the functions to print them
# call main function
#####################################################


import csv

MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
    
def open_file():
    '''
    input for prices and securities file
    try-except within while to loop to reprompt for input if file DNE
    
    '''
    file_pointer = input("\nEnter the price's filename: ")
    
    while True:
        
        try:
            prices_fp = open(file_pointer)
            break
        except FileNotFoundError:
            print("\nFile not found. Please try again.")
            file_pointer = str(input("Enter file name: "))
    
    file_pointer1 = input("\nEnter the security's filename: ")
    
    while True:
        
        try:
            securities_fp = open(file_pointer1)
            break
        except FileNotFoundError:
            print("\nFile not found. Please try again.")
            file_pointer = str(input("Enter file name: "))
            
    return prices_fp, securities_fp




def read_file(securities_fp):
    '''
    skip header in the file
    use csv to read the file
    create empty dictionary and sets
    for loop to iterate through the file
    create a list with the information from the file
    append a deepcopy list to the information list created before
    add the list to the dictionary with the symbols as the key
    add the company name to the empty set
    return the set and the dictionary
    '''
    next(securities_fp, None)
    reader = csv.reader(securities_fp)
    securities_dict ={}
    securities_set = set()
    extra_list = []
    for line in reader:
        info_list = [line[1],line[3],line[4],line[5],line[6]]
        info_list.append(extra_list[:])
        securities_dict[line[0]]=info_list
        securities_set.add(line[1])
    
    return securities_set, securities_dict
        
        
    
def add_prices (master_dictionary, prices_file_pointer):
    '''
    skip the header of the file
    use csv to read the csv file
    for loop to iterate thorugh the file
    create the list with the required infomation
    iterate through the dictionary
    check if the symbols match and append the  price list to the dictionary with the right key and index
    '''
    next(prices_file_pointer, None)
    reader = csv.reader(prices_file_pointer)
    for line in reader:
        price_list = [line[0], float(line[2]), float(line[3]), float(line[4]), float(line[5])]
        for k in master_dictionary.keys():
            if k == line[1]:
                master_dictionary[k][5].append(price_list)
            
    
    
    

def get_max_price_of_company (master_dictionary, company_symbol):
    '''
    create an empty list
    return None if company symbol not in dictionary
    iterate through the dictionary
    iterate through the price list
    create another list with the price and the date
    append the list to the empty list
    error check if the list in empty
    find the max usind max function
    return a tuple of that max price with date
    '''
    L = []
    if company_symbol not in master_dictionary:
        return (None, None)
    for k, v in master_dictionary.items():
        info_list = v[5]
        if company_symbol == k:
            for lst in info_list:
                lst1 = [lst[4], lst[0]]
                L.append(lst1)
        
    if len(L) == 0:
        return (None, None)
    
    max_tup = max(L)
    return (max_tup[0], max_tup[1])






def find_max_company_price (master_dictionary):
    '''
    create empty list
    iterate through the dictionary
    use get_max_price_of_company function to find the max of every company
    create a tuple with the max price and symbol
    error check to see if it's empty
    append to the empty list if not
    find the max of the list using max function
    return the tuple with the symbol and max price
    '''
    max_list = []
    
    for k, v in master_dictionary.items():
        
        max_tup = get_max_price_of_company(master_dictionary, k)
        tup1 = (max_tup[0], k)
        if None in max_tup:
            continue
        else:
            max_list.append(tup1)
        
    max1 = max(max_list)
    return (max1[1], max1[0])
    
    


def get_avg_price_of_company (master_dictionary, company_symbol):
    '''
    create empty list
    error check to see if the symbol is in the dictionary or not
    iterate thorugh the dictionary
    get the information list
    append the price from that to the empty list
    error check to see if the list is empty or not
    find the average of the list
    return and round the average
    '''
    price_list = []
    if company_symbol not in master_dictionary:
        return 0.0
    for k, v in master_dictionary.items():
        if company_symbol == k:
            info_list = v[5]
            for lst in info_list:
                price_list.append(lst[4])
    if len(price_list) == 0:
        return 0.0
    
    avg = sum(price_list)/len(price_list)
    return round(avg, 2)
            


def display_list (lst):  # "{:^35s}"
    '''
    set a variable to 0
    iterate through list
    print the elements of the list
    increse variable by 1
    if count reaches 3
    blank print statement
    set cound back to 0
    print new line
    '''
    count = 0
    for word in lst:
        print("{:^35s}".format(word), end = '')
        count += 1
        if count == 3:
            print()
            count = 0        
    print("\n")
            
    



def main():
    '''
    print WELCOME
    call open file and read file function and set the variables
    call add prices function to update the dictionary
    print MENU
    prompt for input
    while loop to check if the input is within 1 and 6
    algorithm for each and every options
    break when option 6
    '''
    print(WELCOME)
    prices_fp, securities_fp = open_file()
    securities_set, master_dict = read_file(securities_fp)
    add_prices(master_dict, prices_fp)
    
    
    
    print(MENU)
    choice = input("\nOption: ")
    while choice not in "123456":
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")
        
    while choice != '6':

        if choice == "1":
            print("\n{:^105s}".format("Companies in the New York Stock Market from 2010 to 2016"))
            sorted_set = sorted(securities_set)
            display_list(sorted_set)
            
                
        elif choice == "2":
            print("\ncompanies' symbols:")
            symbol_lst = []
            for k in master_dict.keys():
                symbol_lst.append(k)
            symbol_lst.sort()
            display_list(symbol_lst)
                
        
        
        elif choice == "3":
            
            while True:
                symbol = input("\nEnter company symbol for max price: ")
                if symbol in master_dict:
                    break
                else:
                    print("\nError: not a company symbol. Please try again.")
            
            max_tup = get_max_price_of_company(master_dict, symbol)
            
            max_price = max_tup[0]
            date = max_tup[1]
            
            if None in max_tup:
                print("\nThere were no prices.")
            
            else:
                print("\nThe maximum stock price was ${:.2f} on the date {:s}/\n".format(max_price, date))
                
       
        
       
        elif choice == "4":
            com_symbol, com_price = find_max_company_price(master_dict)
            print("\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".format(com_symbol, com_price))
        
        
        
        elif choice == "5":
            while  True:
                avg_symbol = input("\nEnter company symbol for average price: ")
                if avg_symbol in master_dict:
                    break
                else:
                    print("\nError: not a company symbol. Please try again.")
            avg = get_avg_price_of_company(master_dict, avg_symbol)
            print("\nThe average stock price was ${:.2f}.\n".format(avg))

                
        
        print(MENU)
        choice = input("\nOption: ")
        while choice not in "123456":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")





if __name__ == "__main__": 
    main() 