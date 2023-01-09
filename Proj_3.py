################################################
# cse231_project #3 week3
# print banner
# prompt for user input
# if statement 
#    while statement
#        prompt for side inputs
#        If state for degenerate
#        elif state for valid
#           all calculation and classification
#        else statement for not a triangle
#        user input for the loop
# counter for the num of valid triangles
################################################


import math
print()
BANNER = '''
╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''

print(BANNER)
print()
user_input = input("Do you wish to process a triangle (Y or N)?  " )
counter = 0

if user_input == 'Y' or user_input == 'y':
    while user_input == 'Y' or user_input == 'y':
        a = input('\nEnter length of side AB: ')
        b = input('\nEnter length of side BC: ')
        c = input('\nEnter length of side CA: ')
        a = float(a)
        b = float(b)
        c = float(c)
       
        if a + b == c or b + c == a or a + c == b:    
            print()
            print()
            print("  Degenerate Triangle")
            print()
       
        elif a + b > c and b + c > a and a + c > b:
            print()
            print()
            print("  Valid Triangle")
            print()
            print("  Triangle sides:")
            print("    Length of side AB:", float(a))
            print("    Length of side BC:", float(b))
            print("    Length of side CA:", float(c))
            
            rad_a = math.acos((a**2+c**2-b**2)/(2*a*c))      
            rad_b = math.acos((a**2+b**2-c**2)/(2*a*b))
            rad_c = math.acos((b**2+c**2-a**2)/(2*b*c))
            deg_a = (rad_a * 180)/(math.pi)
            deg_b = (rad_b * 180)/(math.pi)
            deg_c = (rad_c * 180)/(math.pi)
           
            print()
            print("  Degree measure of interior angles:")
            print("    Angle A:", round(deg_a, 1))
            print("    Angle B:", round(deg_b, 1))
            print("    Angle C:", round(deg_c, 1))
            print()
            print("  Radian measure of interior angles:")
            print("    Angle A:", round(rad_a, 1))
            print("    Angle B:", round(rad_b, 1))
            print("    Angle C:", round(rad_c, 1))
            print()
            print("  Perimeter and Area of triangle:")
            perimeter = float(a + b + c)
            s = perimeter / 2
            area = math.sqrt((s)*(s-a)*(s-b)*(s-c))
            print("    Perimeter of triangle:", round(perimeter, 1))
            print("    Area of triangle:", round(area, 1))
            print()
            print("  Types of triangle:")
           
            if a != b and b != c and c != a:
                print("    Scalene Triangle")
           
            if a == b or b == c or a == c:
                print("    Isosceles Triangle")
           
            if a == b == c:
                print("    Equilateral Triangle")
           
            if deg_a != 90 and deg_b != 90 and deg_c != 90:
                print("    Oblique Triangle")
            
            if deg_a == 90 or deg_b == 90 or deg_c == 90:
                print("    Right Triangle")
            
            if deg_a > 90 or deg_b > 90 or deg_c > 90:
                print("    Obtuse Triangle")
           
            counter += 1
            print()
        
        else:
            print()
            print()
            print("  Not a Triangle")
            print()
            
        user_input = input("Do you wish to process another triangle? (Y or N) ")

print()
print("Number of valid triangles:", counter)
        
        
    
         
        
    
          
        
            
            
        
    









