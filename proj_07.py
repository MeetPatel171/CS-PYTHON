#############################################
# cse 231 project 07
# set variables
# open file function
#   algorithm
# 3 read file functions
#   algorithm
# year movies function
#   algorithm to filter out by year
# genre movies function
#   algorithm to filter out by genres
# gen user function
#   algorithm to filter by gender of user
# occ user function
# algorithm to filter by occupation of user
# highest rated movie function
#   algorithm
# highest rated reviewer function
#   algorithm
# main function
#   algorithm
# call main
##############################################




GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', 'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''
def open_file(s):
    ''' input to enter file name with formating the parameter
        while loop to open it until it opens
    '''
    fp = input('\nInput {} filename: '.format(s))
    while True:
            
        try:
            fp = open(fp, 'r', encoding ="windows-1252")
            return fp
            break
            
        except FileNotFoundError:
            print("\nError: No such file; please try again.")
            fp = input('\nInput {} filename: '.format(s))
    
  




def read_users(fp):
    ''' make an empty list
        for loop to read the file
        setting variable from the file
        creating a tuple of age, gender and occupation
        append the tuple to the list
        return the list
    
    '''
    L_users = [[]]
    
    for line in fp:
        user = line.split('|')
        age = int(user[1])
        gender = str(user[2])
        occupation = str(user[3])
        user_tuple = (age, gender, occupation)
        
        L_users.append(user_tuple)
    
    return L_users
    
        
        

    


def read_reviews(N,fp):
    ''' create an empty list
        create lists withon list
        read the file through for loop
        assign variables
        create tuple and append to the list
        sort the new list
        return the list
    '''
    L_reviews = []
    
    for i in range(N+1):
        L_reviews.append([])
    
    for line in fp:
        userID,movieID,rating,_ = line.strip().split()
        userID = int(userID)
        movieID = int(movieID)
        rating = int(rating)
        L_reviews[userID].append((movieID,rating))
    
    for lst in L_reviews:
        lst.sort()
    
    return L_reviews












def read_movies(fp):
    ''' create empty list
        read the file
        assign variables
        create a list of genres
        create a new list
        make the elements in the genre list an integer and append to the new list
        read that list with a for loop
        check if the value is 1
        if it is append the index of the value from the GENRES list
        create a tuple
        append the tuple to the list
        return the list
        
    '''
    
    L_movies = [[]]
    
    for line in fp:
        
        movies = line.split('|')
        title = str(movies[1])
        date = str(movies[2])
        genres1 = list(movies[5:])
        
        genres = []
        
        for i in genres1:
            i = int(i)
            genres.append(i)
            
        L_genre = []
        
        for i , val in enumerate(genres):
            
            if val == 1:
                L_genre.append(GENRES[i])
            
        movie_tuple = (title, date, L_genre)
        L_movies.append(movie_tuple)
                
    return L_movies
                
        
        
       
        

def year_movies(year, L_movies):
    ''' create empty list
        read the list
        assign variables to filter out the year
        make the year an integer
        compare it the parameter to append the index
        use try and except to filter out from empty lists
        return the list
    '''
    L_years = []
    
    for tup in L_movies:
        try:
            L = tup[1]
            index = L_movies.index(tup)
            year1 = L[-4:]
            year1 = int(year1)
            if year == year1:
                L_years.append(index)
        except:
            continue
                
            
    return L_years
        
        
        





def genre_movies(genre,L_movies):
    ''' create new list
        read the file
        filter out the genres
        check if genre parameter is in the genres list
        if it is append the index
        return the list
    '''
    L_genre =[]
    
    for tup in L_movies:
        try:
            genres = tup[2]
            index = L_movies.index(tup)
            
            if genre in genres:
                L_genre.append(index)
        except:
            continue
    
    return L_genre




def gen_users (gender, L_users, L_reviews):
    ''' create an empty list
        set a variable as 1
        read the list
        set the gender
        check if it is the same as the parameter and append the index of the variable 
        increade the varible by 1
        return the list
        
    '''
    
    L_gen = []
    count = 1
    for tup in L_users:
        
        try:
            gen = tup[1]
            if gender == gen:
                L_gen.append(L_reviews[count])
        except:
            continue
        count+=1
    return L_gen
    
    
    
    
    
    
def occ_users (occupation, L_users, L_reviews):
    ''' same algorithm as previous function
        just changing the tuple index
    '''
    L_occ = []
    count = 1
    for tup in L_users:
        
        try:
            occ = tup[2]
            if occupation == occ:
                L_occ.append(L_reviews[count])
        except:
            continue
        count+=1
    return L_occ




def highest_rated_by_movie(L_in,L_reviews,N_movies):
    ''' Docstring'''
    pass





def highest_rated_by_reviewer(L_in,N_movies):
    ''' Docstring'''
    pass   # remove this line
 





def main():
    fp_users = open_file('users')
    fp_reviews = open_file('reviews')
    fp_movies = open_file('movies')
    print(MENU)
    menu = int(input('\nSelect an option (1-5): '))
    while menu >= 1 and menu <= 5:
         
        if menu == 5:
            break

if __name__ == "__main__":
    main()
                                           