################################################
# cse_231 project #5
#
#import math
# set math variables
# open_file function
#   algorithm
# make_float function
#   algorithm
# get _density function
#   algorithm
# temp_in_range function
#   algorithm
# get_dist_range function
#   algorithm
# main function
#   variables
#   for loop
#       algorithm/ calculations
#   print statements
# call main function
##################################################












import math

#Constants
PI = math.pi   
EARTH_MASS =  5.972E+24    # kg
EARTH_RADIUS = 6.371E+6    # meters
SOLAR_RADIUS = 6.975E+8    # radius of star in meters
AU = 1.496E+11             # distance earth to sun in meters
PARSEC_LY = 3.262

def open_file():
    file_input = str(input("Input data to open: ")) 
    
    open_file = file_input + ".csv"
    while True:
        
    
        try:
            r = open(open_file, 'r')
            return r
        except FileNotFoundError:
            print('\nError: file not found.  Please try again.')
            file_input = str(input("Enter a file name: "))
            open_file = file_input + ".csv"
    
    '''
    prompt for file name
    append .csv
    while loop for opening the right file
    keep prompting until the file is right and opens
    '''
            
            

def make_float(s):
    try:
        s = float(s)
        return s
    except ValueError:
        return -1
    '''
    convert the argument to float
    if it does not work
    return -1
    '''
  



def get_density(mass, radius):
    if radius <= 0:
        return -1
    mass = mass * EARTH_MASS
    radius = radius * EARTH_RADIUS
    volume = (4*PI*(radius**3))/ 3
    density = mass/volume
    return density

    '''
    convert the mass and radius in earth's terms
    formula for volume
    use volume to find density
    return density
    if radius negative
    return -1
    '''




def temp_in_range(axis, star_temp, star_radius, albedo, low_bound, upp_bound):
    if axis < 0 or star_temp < 0 or star_radius <0 or albedo < 0 or low_bound <0 or upp_bound <0:
       return False
    
    axis = AU * axis
    star_radius = star_radius * SOLAR_RADIUS
    planet_temp = star_temp * ((star_radius/(2*axis))**0.5)*(1-albedo)**0.25
    if (low_bound <= planet_temp) and (planet_temp <= upp_bound):
        return True
    else:
        return False 
    
    '''
    axis in earth's term
    star radius in solar's term
    formula for temperature
    if temperature withi the bounds
    return true
    else false
    '''
    



def get_dist_range():
    
    dist_prompt = input("\nEnter maximum distance from Earth (light years): ")
    
    while True:
        try:
            dist_prompt = float(dist_prompt)
            if dist_prompt < 0:
                print("\nError: Distance needs to be greater than 0.")
                dist_prompt = input("\nEnter maximum distance from Earth (light years): ")
            
            else:
                return dist_prompt
        
        except ValueError:
            print("\nError: Distance needs to be a float.")
            dist_prompt = input("\nEnter maximum distance from Earth (light years): ")
    
    '''
    prompt for maximum distance
    while loop to convert it into float 
    keep prompting untill its not negative or a string
    return the max distance
    '''
        
    
            
    
def main():
    print('''Welcome to program that finds nearby exoplanets '''\
          '''in circumstellar habitable zone.''')
    fp = open_file()
    dist = get_dist_range()
    dist1 = dist/PARSEC_LY
    lowwer_bound = 200
    upper_bound = 350
    albedo = 0.5
    total_mass_planet = 0
    habitable_planets = 0
    max_planet = -1
    max_stars = -1
    counter = 0
    rocky_dist = dist/ PARSEC_LY
    rocky_name = None
    gassy_dist = dist/ PARSEC_LY
    gassy_name = None
    fp.readline()
    
    for line in fp:
        
        planet_name = str(line[:25])
        num_stars = int(line[50:57])
        num_planet = int(line[58:65])
        axis = make_float(line[66:77])
        planet_radius = make_float(line[78:85])
        planet_mass = make_float(line[86:96])
        star_temp = make_float(line[97:105])
        star_radius = make_float(line[106:113])
        distance = make_float(line[114:])
        
        if distance >= 0 and distance <= dist1:
            
            if num_planet > max_planet:
                max_planet = num_planet
            if num_stars > max_stars:
                max_stars = num_stars
            
            if planet_mass > 0:
                total_mass_planet += planet_mass
                counter += 1
            
            avg_mass = total_mass_planet / counter
           
            density = get_density(planet_mass, planet_radius)
            
            if temp_in_range(axis, star_temp, star_radius, albedo, lowwer_bound, upper_bound) == True:
                habitable_planets += 1
            
                if (planet_mass <10 and planet_mass>0) or (planet_radius>0 and planet_radius<1.5) or (density>2000):
                    if distance < rocky_dist:
                        rocky_dist = distance
                        rocky_name = planet_name
                    
                else:
                    if distance < gassy_dist:
                        gassy_dist = distance
                        gassy_name = planet_name
        
        else:
            continue
            
        
        
    fp.close()
    
    
    
    print("\nNumber of stars in systems with the most stars: {:d}.".format(max_stars))
    print("Number of planets in systems with the most planets: {:d}.".format(max_planet))
    print("Average mass of the planets: {:.2f} Earth masses.".format(avg_mass))
    print("Number of planets in circumstellar habitable zone: {:d}.".format(habitable_planets))
    
    
    if rocky_name == None:
        print("No rocky planet in circumstellar habitable zone.")
    else: 
        print("Closest rocky planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(rocky_name.strip(), rocky_dist* PARSEC_LY))
        
    if gassy_name == None:
        print("No gaseous planet in circumstellar habitable zone.")
        
        
    else:
        print("Closest gaseous planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(gassy_name.strip(), gassy_dist* PARSEC_LY))
        
    '''
    open the file by calling the open_file function
    set all the different variables needed for the calculation and algorithm
    for loop to read the file
    read the file and set the different variables through string slicing
    set algorithm for a valid distance
    algorithm for max planets and stars
    calculate the total mass for the average mass
    call the get_density function to get density
    call temp_iun_range function to calculate rocky or gaseous planet's distance and name
    close the file
    all the print statements
    '''

    

if __name__ == "__main__":
    main()