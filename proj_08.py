########################################################################
# cse 231 project 08
#
# Set Menu as varible
# open file function
#   keep prompting until file opens
# read names function
#   read file to return a list of names
# read friends function
#   read file to  return list of lists of friends
# create friends dictionary function
#   create a dictionary with the two lists from previous functions
# find common friends function
#   algorithm to find common friends from the dictionary
# find max friends function
#   algorithm to find the max number of friends in the dictionary
# find max common friends function
#   algoithm to find the max common
# find second friends function
#   algorithm to find friends of friends
# find max second friends function
#   algorithm to find the max of the friens of the friend dictionary
# main function
#   algorithm
# call main function
########################################################################



MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''
    
def open_file(s):
    '''
    input to enter file name with formating the parameter
        while loop to open it until it opens
    '''
    fp = input('\nInput a {} file: '.format(s))
    while True:
            
        try:
            fp = open(fp, 'r')
            return fp
            break
            
        except FileNotFoundError:
            print("\nError: No such file; please try again.")
            fp = input('\nInput a {} file: '.format(s))

def read_names(fp):
    '''
    iterate throught the names file
    strip and append to a list
    return: list of names
    '''
    l_names = []
    for line in fp:
        line = line.strip()
        l_names.append(line)
    return l_names


def read_friends(fp,names_lst):
    '''
    for loop to iterate through the list
        strip and split it
        for loop to find the index 
            append the names from the names list with that particular index
        append the friends list to a new list 
    returns: list of list contaning friend names
    '''
    
    l_friends =[]
    for line in fp:
        
        line_list = line.strip().split(',')
        
        l_list = []
        for num in line_list[:-1]:
            num = int(num)
            l_list.append(names_lst[num])
        l_friends.append(l_list)
    return l_friends
    
    
    
def create_friends_dict(names_lst,friends_lst):
    '''
    use dict and zip operation to create a dictionary with names as the key 
    and list of friends as the value
    returnthe dictionary
    '''
    friends_dict = dict(zip(names_lst, friends_lst))
    return friends_dict



def find_common_friends(name1, name2, friends_dict):
    '''
    create two sets
    use & operarion to find the common elements
    return the common set 
    '''
    set1 = set(friends_dict[name1])
    set2 = set(friends_dict[name2])
    
    common_set = set(set1 & set2)
    
    return common_set
    



def find_max_friends(names_lst, friends_lst):
    '''
    set a variable to 0
    create empty list
    for loop to iterate through the friends list
        find the maximum value using max and len
    for loop to iterate throught the list again with enumerate to get the index
        if len of the list is same as the maximum value
        append the names with the index
    sort the list
    return the list and the maximum number
    '''
    maximum = 0
    max_friends = []
    for lst in friends_lst:
        maximum = max(maximum, len(lst))
    
    for i, list_of_friends in enumerate(friends_lst):
        if len(list_of_friends) == maximum:
            max_friends.append(names_lst[i])
    max_friends.sort()
    return max_friends, maximum    
        
        
    

def find_max_common_friends(friends_dict):
    '''
    neste for loop to iterate through the dictionary
    3 skips with if statements so that theres no repeated names
    create a dictioanry
    algorithm to find the max value of the dictionary
    reuturn the list and the max value
    '''
    common_dict = {}
    for name1, v1 in friends_dict.items():
        for name2, v2 in friends_dict.items():
            
            if (name2, name1) in common_dict:
                continue
            if name1 in v2 or name2 in v1:
                continue
            if name1 == name2:
                continue
            
            common_dict[(name1, name2)] = find_common_friends(name1, name2, friends_dict)
    
    
    max_common_friends = []
    max_common = []
    
    for mutual_lst in common_dict.values():
        max_common_friends.append(len(mutual_lst))
    max_value = max(max_common_friends)
    
    
    
    for name1_lst, mutual1_lst in common_dict.items():
        if len(mutual1_lst) == max_value:
            max_common.append(name1_lst)
    max_common.sort()
    
    return max_common, max_value
            
        
        
def find_second_friends(friends_dict):
    '''
    for loop to iterate the key and value in the friends dictionary
        for loop to iterate throught he friends list
            find friends of friends 
            for loop to iterate throught he list of friends of friends
                add the names to a set to filter out the duplicates
        use - operation to filter out the sets
        add the set to the dictionary
    return the dictionary
    '''
    second_dict = {}
    
    for k_name, v_friends in friends_dict.items():
        friends = set()
        
        for name in v_friends:
            friends2 = friends_dict[name]
            for name1 in friends2:
                friends.add(name1)
                
        first_friend = set(v_friends)    
        second_set = friends - first_friend - {k_name}
        second_dict[k_name] = second_set
    
    return second_dict
            
         
def find_max_second_friends(seconds_dict):
    '''
    Same algorithm as in find max common friends friends function 
    from a dictionary
    returns max second friends list and max value
    '''
    max_lst = []
    second_max = []
    
    for second_lst in seconds_dict.values():
        max_lst.append(len(second_lst))
    max_value = max(max_lst)
    
    for name, name_lst in seconds_dict.items():
        if len(name_lst) == max_value:
            second_max.append(name)
    second_max.sort()
    
    return second_max, max_value
        


def main():
    '''
    open file
    read the files to get the names and friends list
    call create_friends_dict toc create a dictionary
    prompt for the options
    while loop to error check the inout for options
    if option 1:
        algorithm
    if option 2:
        algorithm
    if option 3:
        algorithm
    if option 4:
        algorithm
    if option 5:
        break
    reprompt for the option
    '''
    
    print("\nFriend Network\n")
    fp = open_file("names")
    names_lst = read_names(fp)
    fp = open_file("friends")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst,friends_lst)
    
    
    print(MENU)
    choice = input("\nChoose an option: ")
    while choice not in "12345":
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")
        
    while choice != '5':

        if choice == "1":
            max_friends, max_val = find_max_friends(names_lst, friends_lst)
            print("\nThe maximum number of friends:", max_val)
            print("People with most friends:")
            for name in max_friends:
                print(name)
                
        elif choice == "2":
            max_names, max_val = find_max_common_friends(friends_dict)
            print("\nThe maximum number of commmon friends:", max_val)
            print("Pairs of non-friends with the most friends in common:")
            for name in max_names:
                print(name)
                
        elif choice == "3":
            seconds_dict = find_second_friends(friends_dict)
            max_seconds, max_val = find_max_second_friends(seconds_dict)
            print("\nThe maximum number of second-order friends:", max_val)
            print("People with the most second_order friends:")
            for name in max_seconds:
                print(name)
                
        elif choice == "4":
            name_input = input("\nEnter a name: ")
            while True:
                if name_input in names_lst:
                    break
                else:
                    print("\nThe name {} is not in the list.".format(name_input))
                    name_input = input("\nEnter a name: ")
                
                
            print("\nFriends of {}:".format(name_input))
            friends_input = friends_dict[name_input]
            for name in friends_input:
                print(name)
    
                
        else: 
            print("Shouldn't get here.")
            
        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")

if __name__ == "__main__":
    main()