#####################################################
# cse231_project #4 week 4
# import math
# set epsilon
# define MENU
# factorial function
# e function
# pi function
# sinh function
# main function
#   multiple if statement for different functions
# call main function
#####################################################

import math 

EPSILON = 0.0000001

MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''

def factorial(N): 
    N = int(N)
    if N < 0:
        return None
    
    
    if N==1 or N==0:
        return 1
    return N*factorial(N-1)
    

def e():
    
    n = 0
    calc = 0 
    
    while(1/math.factorial(n))>EPSILON:
        calc+=1/math.factorial(n)
        n+=1 
    return round(calc,10) 




def pi():
    n=0
    calc= float(0)
    
   
    while abs(((-1)**n)/(2*n+1))>EPSILON:
        calc += ((-1)**n)/(2*n+1)
        n+=1 
    
    return (4*round(calc, 10))

def sinh(X):
    n=0
    calc=0
    while abs(X**(2*n+1)/(factorial(2*n+1))) > EPSILON:
        calc+= ((X**(2*n+1))/(factorial(2*n+1)))
        n +=1
    return round(calc, 10)




def main():
    print(MENU)
    opts="FfEePpSsMmXx"
    while(1):
        opt = input("\nChoose an option: ")
        if opt not in opts:
            opt = opt.upper()
            print("\nInvalid option:", opt )
            print(MENU)
        
        
        if opt == 'M' or opt=='m':
            print(MENU)
        
        
        
        if opt=='F' or opt=='f':
            print("\nFactorial")
            
            
            N = (input("Input non-negative integer N: "))
            if N.isdigit():
                N = int(N)
                print("\nCalculated:",factorial(N))
                print("Math:", round(math.factorial(N), 10))
                diff = math.factorial(N) - factorial(N)
                print("Diff:",diff)
            else:
                print("Invalid N.")
            
            
                

            
            
       
        
        if opt=='E' or opt=='e': 
            print("\ne")
            print("Calculated:",e()) 
            
            print("Math:", round(math.e, 10))
            
            
            print("Diff: {:.10f}".format(math.e-e()))
    
        
        
        
        if opt=='P' or opt=='p': 
            print("\npi")
            print("Calculated:",pi() )
            print("Math:",round(math.pi, 10))
            print("Diff: {:.10f}".format(math.pi - pi()))
        
        
        if opt=='S' or opt=='s':
            print("\nsinh")
            
            X = float((input("X in radians: ")))
            try:
                float(X)
            except ValueError:
                print("Invalid X.")
                return None
                
            
            print("\nCalculated:",sinh(X))
            print("Math:", round(math.sinh(X), 10))
            print("Diff: {:.10f}".format(math.sinh(X) - sinh(X)))
            
           
                
                
                
        
       
        
        if opt=='X' or opt=='x':
            print("\nThank you for playing.")
            break 
if __name__ == '__main__':
    main()