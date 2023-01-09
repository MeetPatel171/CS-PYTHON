#############################################################################
# cse231 project 10
#
# import Card and Deck class
# MENU string
# initalize function
#   set the the data structures for stock, waste, tableau and foundation
# display funtion
# stock to waste function
#   a move to move a card from stock to waste
# waste to foundation function
#   move a card from waste to foundation with right conditions
# waste to tableau function
#   move a card from waste to tableau with right conditions
# tableau to foundation function
#   move a card from tableau to foundation with right conditions
# tableau to tableau function
#   move a card within tableau itself with right condition
# check win function 
#   check conditions for win
# parse option function
#   given function
# main function
#   algorithm using all the functions
# call main
#############################################################################






from cards import Card, Deck

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''

def initialize():
    '''
    Set variables for tableau, stock, waste and foundation
    nested loop to deal card in tableau
        flip last card in each column
    deal a card in waste
    return tableau, stock, foundation and waste
    '''
    stock = Deck()
    foundation = [[], [], [], []]
    tableau = [[], [], [], [], [], [], []]
    waste = []
    stock.shuffle()
    for i in range(7):
        for j in range(i, 7):
            card = stock.deal()
            card.flip_card()
            tableau[j].append(card)
    for lst in tableau:
        lst[-1].flip_card()
    waste_card = stock.deal()
    waste.append(waste_card)
    return tableau, stock, foundation, waste
    
    
    
def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):
    '''
    check if stock is empty
    if not append a card from stock to waste
    return true if it moves
    '''
    if len(stock) > 0:
        waste_card = stock.deal()
        waste.append(waste_card)
        return True
    else:
        return False

def waste_to_foundation( waste, foundation, f_num ):
    '''
    check waste is empty
        check conditions for if foundation is empty
            check if card is ace
                append to foundation
        check if card is same suit and one rank higher
            append card to foundation
    '''
    if len(waste)>0:
        card = waste[-1]
        try:
            if len(foundation[f_num]) == 0:
                if card.rank() == 1:
                    foundation[f_num].append(card)
                    waste.pop(-1)
                    return True
                else:
                    return False
                
            elif card.suit() == foundation[f_num][-1].suit() and card.rank() - foundation[f_num][-1].rank() == 1:
                foundation[f_num].append(card)
                waste.pop(-1)
                return True
            
            else:
                return False
        except:
            return False
    else:
        return False


       
def waste_to_tableau( waste, tableau, t_num ):
    '''
    check is waste is not empty
        check if column is empty
            check if card is a king
                append the card to the column
        else
            check for opposite suit and a rank lower
                append the card to the column
    '''
    if len(waste)>0:
        card = waste[-1]
        
        if len(tableau[t_num]) == 0:
            if card.rank() == 13:
                tableau[t_num].append(card)
                waste.pop(-1)
                return True
            else:
                return False
            
        if len(tableau[t_num]) > 0:
            if (card.suit() == 1 or card.suit() == 4):
                if (tableau[t_num][-1].suit() == 2 or tableau[t_num][-1].suit() == 3):
                    if tableau[t_num][-1].rank() - card.rank() == 1:
                        tableau[t_num].append(card)
                        waste.pop(-1)
                        return True
                    else:
                        return False
                else:
                    return False
                
        
            elif (card.suit() == 2 or card.suit() == 3):
                if (tableau[t_num][-1].suit() == 1 or tableau[t_num][-1].suit() == 4):
                    if tableau[t_num][-1].rank() - card.rank() == 1:
                        tableau[t_num].append(card)
                        waste.pop(-1)
                        return True
                    else:
                        return False
                else:
                    return False
    return False



def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    '''
    check if foundation is empty
        check if card is a ace
            append to the foundation
            removee the card 
            flip the last card
    else
        check for same suit and a rank higher
            append the card to foundation
            remove the card
            flip the card
    '''
    card = tableau[t_num][-1]
    
    if len(foundation[f_num]) == 0:
        if card.rank() == 1:
            foundation[f_num].append(card)
            tableau[t_num].pop(-1)
            try:
                if not tableau[t_num][-1].is_face_up():
                    tableau[t_num][-1].flip_card()
                return True
            except:
                return True
        else:
            return False
    
    elif card.suit() == foundation[f_num][-1].suit() and card.rank() - foundation[f_num][-1].rank() == 1:
        foundation[f_num].append(card)
        tableau[t_num].pop(-1)
        try:
            if not tableau[t_num][-1].is_face_up():
               tableau[t_num][-1].flip_card()
               return True
        except:
            return True
        return True
    
    else:
        return False


def tableau_to_tableau( tableau, t_num1, t_num2 ):
    '''
    check if column is empty
        check if card is a king
            append card to the particular column
            remove card
            flip last card
    else
        check is card is oppoite suit and a rank lower
            append the card 
            remove the card
            flip the last card
    '''
    card = tableau[t_num1][-1]
    
    try:
        if len(tableau[t_num2]) == 0:
            if card.rank() == 13:
                tableau[t_num2].append(card)
                tableau[t_num1].pop(-1)
                try:
                    if not tableau[t_num1][-1].is_face_up():
                       tableau[t_num1][-1].flip_card()
                       return True
                except:
                    return True
                return True
            else:
                return False
        
        else:
            if (card.suit() == 1 or card.suit() == 4):
                if (tableau[t_num2][-1].suit() == 2 or tableau[t_num2][-1].suit() == 3):
                    if tableau[t_num2][-1].rank() - card.rank() == 1:
                        tableau[t_num2].append(card)
                        tableau[t_num1].pop(-1)
                        try:
                            if not tableau[t_num1][-1].is_face_up():
                               tableau[t_num1][-1].flip_card()
                               return True
                        except:
                            return True
                        return True
                    else:
                        return False
                else:
                    return False
                
            if (card.suit() == 2 or card.suit() == 3):
                if (tableau[t_num2][-1].suit() == 1 or tableau[t_num2][-1].suit() == 4):
                    if tableau[t_num2][-1].rank() - card.rank() == 1:
                        tableau[t_num2].append(card)
                        tableau[t_num1].pop(-1)
                        try:
                            if not tableau[t_num1][-1].is_face_up():
                               tableau[t_num1][-1].flip_card()
                               return True
                        except:
                            return True
                        return True
                    else:
                        return False
                else:
                    return False
    except:
        return False
            
            
def check_win (stock, waste, foundation, tableau):
    '''
    check is stock, waste, tableau is empty and foundation is not empty
    '''
    if len(stock) == 0 and len(waste) == 0 and len(tableau[0]) == 0 and \
    len(tableau[1]) == 0 and len(tableau[2]) == 0 and len(tableau[3]) == 0 and \
    len(tableau[4]) == 0 and len(tableau[5]) == 0 and len(tableau[6]) == 0 and \
    len(foundation[0]) == 13 and len(foundation[1]) == 13 and len(foundation[2]) == 13 \
    and len(foundation[3]) == 13:
        return True
    else:
        return False
    
    
    
def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


        
def main():   
    '''
    set variables with initialize function
    print MENU
    while loop to keep prompting until user quits
        display function
        prompt for input
        call parse option function
        check for different options
            call respective functions to move the card
                check for win anytime a card is moved to foundation
        break out of the loop when user inputs Q
    '''
    tableau, stock, foundation, waste = initialize()
    print(MENU)
   
    
    while True:
        display(tableau, stock, foundation, waste)
        option = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")
        command_lst = parse_option(option)
        
        if not command_lst:
            continue
        
        if command_lst[0] == "TT":
            if not tableau_to_tableau(tableau, command_lst[1]-1, command_lst[2]-1):
                print("\nInvalid move!\n")
        
        elif command_lst[0] == "TF":
            if tableau_to_foundation(tableau, foundation, command_lst[1]-1, command_lst[2]-1):
                if check_win(stock, waste, foundation, tableau):
                    print("You won!")
                    break
                
            else:
                print("\nInvalid move!\n")
        
        elif command_lst[0] == "WT":
            if not waste_to_tableau(waste, tableau, command_lst[1]-1):
                print("\nInvalid move!\n")
        
        elif command_lst[0] == "WF":
            if waste_to_foundation(waste, foundation, command_lst[1]-1):
                if check_win(stock, waste, foundation, tableau):
                    print("You won!")
                    break
                
            else:
                print("\nInvalid move!\n")
        
        elif command_lst[0] == "SW":
            if not stock_to_waste(stock, waste):
                print("\nInvalid move!\n")
        
        elif command_lst[0] == "R":
            tableau, stock, foundation, waste = initialize()
            print(MENU)
            display(tableau, stock, foundation, waste)
            
            
        elif command_lst[0] == "H":
            print(MENU)
        
        elif command_lst[0] == "Q":
            break
                
            
                                   
if __name__ == '__main__':
          main()            
                 
                 
            
        
    
    
    
    
            
        
                    
            
            
            
            
                    
        
        
        
        
        
        
        
        


