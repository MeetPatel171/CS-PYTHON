##############################################################
# cse 231 Project_06
#
# import csv/ operator/ itemgetter
# set variables for multiple strings
# open file function
# read file function
# criterion function
# criteria function
# region list function
# sort function
# display character function
# option function
# main function
#   call open file, read file and option function
#   while loop for different function to reprompt option
#       if option 1
#           algorithm
#       if option 2
#           algorithm
#       if option 3
#           algorithm
#       if option 4
#           break
#       repromt
# call main function
#############################################################










import csv
from operator import itemgetter

NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"

def open_file():
    '''
    input for filename
        while loop
            try-except function to open the file
            if not reprompt
    '''
    file_pointer = str(input("Enter file name: ")) 
    
    while True:
        
        try:
            fp = open(file_pointer)
            return fp
            break
        except FileNotFoundError:
            print("\nError opening file. Please try again.")
            file_pointer = str(input("Enter file name: "))
            
        
    
        
    

def read_file(fp):
    ''' 
    read file as a csv file
    for loop to read file
        set variables through indexing
            
        create list of tuple
    return list of tuples
    '''
    
    next(fp, None)
    character_list = []
    reader = csv.reader(fp)
    
    for line in reader:
        
        
        name = line[0]
        rarity = int(line[1])
        element = line[2]
        weapon = line[3]
        region = line[4]
        
        
        if region == "":
            region = None
        character_tuple = (name, element, weapon, rarity, region)
        character_list.append(character_tuple)
    return character_list
    

    
def get_characters_by_criterion (list_of_tuples, criteria, value):
    '''
    create new empty list
    for loop to read through the parameter list
        if criteria is rarity
            double check for int with if function
                append to the list
        else
            double check for string with if function
                append to the list
    return new list
    '''
    
    result = []
    
    for l in list_of_tuples:
        if criteria == RARITY: 
            if l[criteria] and type(value) == int and l[criteria] == value:
                result.append(l)
            
        else:
            if l[criteria] and type(value) == str and l[criteria].lower() == value.lower():
                result.append(l)
    return result
    


def get_characters_by_criteria(master_list, element, weapon, rarity):
    '''
    use criterion function three times to get list in criteria
    '''
    
    tup_list1 = get_characters_by_criterion(master_list, ELEMENT, element)
    tup_list2 = get_characters_by_criterion(tup_list1, WEAPON, weapon)
    tup_list3 = get_characters_by_criterion(tup_list2, RARITY, rarity)
    return tup_list3
    
    
    
def get_region_list(master_list):
    '''
    create new list
    for loop to read master list
        if region empty
            continue
        if region already in new list
            continue
        else
            append region to the new list
    sort new list
    return new list
    '''
    new_list = []
    for i in master_list:
        if i[4] == None:
            continue
        elif i[4] in new_list:
            continue
        else:
            new_list.append(i[4])
    new_list.sort()
    return new_list
            
            

def sort_characters (list_of_tuples):
    '''
    sort list of tuples
    sort list of tuples again but with a different key and reverse it for descending order
    return sorted list
    '''
    sorted_list = sorted(list_of_tuples)
    sorted_list= sorted(sorted_list,   key=itemgetter(3), reverse = True)
    return sorted_list
    
   
    
def display_characters (list_of_tuples):
    '''
    check if list is empty
        print nothing to print
    else
        print header formart
        for loop to read list of tuples
            if region empty
                print region as N/A
            else
                print row format
    '''
    
    
    if len(list_of_tuples) == 0:
        print("\nNothing to print.")
        
    else:
        print(HEADER_FORMAT.format("Character", "Element", "Weapon", "Rarity", "Region" ))
        for tup in list_of_tuples:
            if tup[4] == None:
            
                print(ROW_FORMAT.format(tup[0], tup[1], tup[2], tup[3], 'N/A'))
            else:
                print(ROW_FORMAT.format(tup[0], tup[1], tup[2], tup[3], tup[4]))
        
        

def get_option():
    '''
    option input
    while loop to error check until right
    '''
    input_opt = input(MENU)
    while True:
        try:
            input_opt = int(input_opt)
            if input_opt <= 4 and input_opt >= 1:
                return input_opt
                break
            else:
                print("INVALID_INPUT")
                input_opt = input(MENU)
        except ValueError:
            print(INVALID_INPUT)
            input_opt = input(MENU)
    
    


def main():
    '''
    call open file/ read file/ option functions
    while loop 
        if option 1
            call region list
        if option 2
            criteria input
            error check for int and within bounds i.e. between 1 and 4
            value input
            if criteria is rarity
                error check for int
            call criteriob function
            sort the list
            display the list
        if option 3
            three inputs for element, weapon and rarity
            error check for rarity to be an int
            call criteria function
            sort the list
            display the list
        if option 4
            break
        reprompt for option
    '''
    fp = open_file()
    list_of_tuples = read_file(fp)
    option = get_option()
    while option >= 1 and option <= 4: 
        
        
        if option == 1:
            print("\nRegions:")
            region_list = get_region_list(list_of_tuples)
            print(", ".join(region_list))
            
        
        
        
        
        if option == 2:
            criteria_input = input(CRITERIA_INPUT)
            
            while True:
                try:
                    criteria_input = int(criteria_input)
                    break
                except ValueError:
                    print(INVALID_INPUT)
                    criteria_input = input(CRITERIA_INPUT)
            
            
            
            while criteria_input < 1 and criteria_input > 4:
                print(INVALID_INPUT)
                criteria_input = input(CRITERIA_INPUT)
            
            value_input = input(VALUE_INPUT)
            
                
            if criteria_input == RARITY:
                while True:
                    try:
                        value_input = int(value_input)
                        break
                    except ValueError:
                        print(INVALID_INPUT)
                        value_input = input(VALUE_INPUT)
            
            criterion_list = get_characters_by_criterion(list_of_tuples, criteria_input, value_input)
            sorted_list = sort_characters(criterion_list)
            display_characters(sorted_list)
        
        
        if option == 3:
            element = input(ELEMENT_INPUT)
            weapon = input(WEAPON_INPUT)
            rarity = input(RARITY_INPUT)
            while True:
                try:
                    rarity = int(rarity)
                    break
                except ValueError:
                    print(INVALID_INPUT)
                    rarity = input(RARITY_INPUT)
            
            criteria_list = get_characters_by_criteria(list_of_tuples, element, weapon, rarity)
            sorted_list = sort_characters(criteria_list)
            display_characters(sorted_list)
        
        if option == 4:
            break
       
        option = get_option()
    
            
    
            
            
                












if __name__ == "__main__":
    main()
    