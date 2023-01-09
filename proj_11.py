###############################################################
# cse 231 project 11
# 
# set variables for conversion
# class Volume
#   initialize method
#       check for validity
#           set magnitude and units
#   str methiod
#       return the magnitude and units in string
#   repr method
#       return the magnitude and units in string
#   is_valid method
#       return boolean
#   get_units method
#       return units
#   get_magnitude method
#       return magnitude
#   metric method
#       return the class in metric system
#   customary method
#       return the class in US customary system
#   eq method
#       check the if two class volume is same
#   add method
#       add the magnitudes of two volume in the same untis
#   sub method
#       subtract he magnitudes of two volume in the same untis
###############################################################

UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    
    def __init__(self, magnitude = 0, units = "ml"):   # this line is incomplete: parameters needed
        '''
        set is_valid to false/none
        if  magnitude is a int or float
            if magnitude is 0 or positive
                if units is ml or oz
                    set magnitude and units
                    set is_valid to true
        else
            set magnitude and units to either 0 and none
        '''
        
        self.__is_valid = None
        
        if type(magnitude) == int or type(magnitude) == float:
            if magnitude >= 0:
                if units in UNITS:
                    self.__magnitude = magnitude
                    self.__units = units
                    self.__is_valid = True
                else:
                    self.__magnitude = None
                    self.__units = None
            else:
                self.__magnitude = 0
                self.__units = None
        else:
            self.__magnitude = 0
            self.__units = None
        
    def __str__(self):    # this line is incomplete: parameters needed
        '''
        check for validity
            return formated string with a 3 point decimal for magnitude
        else
            return not a volume
        '''
        
        if self.__is_valid:
            return "{:.3f} {}".format(self.__magnitude, self.__units)
        else:
            return "Not a Volume"
        
    def __repr__(self):    # this line is incomplete: parameters needed
        '''
        check for validity
            return formated string with a 6 point decimal for magnitude
        else
            return not a volume
        '''
        
        if self.__is_valid:
            return "{:.6f} {}".format(self.__magnitude, self.__units)
        else:
            return "Not a Volume"
        
    def is_valid(self):     # this line is incomplete: parameters needed
        '''
        return is_valid
        '''
        
        return self.__is_valid
    
    def get_units(self):     # this line is incomplete: parameters needed
        '''
        return units
        '''
       
        return self.__units
        
    
    def get_magnitude(self):  # this line is incomplete: parameters needed
        '''
        return magnitude
        '''
        
        return self.__magnitude
       
    
    def metric(self):      # this line is incomplete: parameters needed
        '''
        check if units is customary(oz)
            convert the magnitude to metric(ml)
            return Volume with those parameters
            
        else
            return the volume
        '''
        
        if self.__units == "oz":
            mag = self.__magnitude * MLperOZ
            unit = "ml"
            out = Volume(mag, unit)
            return out
        else:
            out = Volume(self.__magnitude, self.__units)
            return out
            
        
    def customary(self):    # this line is incomplete: parameters needed
        '''
        check if units is metric(ml)
            convert the magnitude to customary(oz)
            return Volume with those parameters
            
        else
            return the volume
        '''
        
        if self.__units == "ml":
            mag = self.__magnitude / MLperOZ
            unit = "oz"
            out = Volume(mag, unit)
            return out
        else:
            out = Volume(self.__magnitude, self.__units)
            return out
    
        
    def __eq__(self, other):  # this line is incomplete: parameters needed
        '''
        check if the type of other is also a Class
            return True if the absolute value of the difference of the magnitude is less than DELTA
        '''
        
        if not isinstance(other, Volume):
            return False
        
        return abs(self.get_magnitude()-other.get_magnitude()) < DELTA
            
        
    
    
    def add(self, other):  # this line is incomplete: parameters needed
        '''
        check if the type of other is also a Class
            check if the units is same
                return the Volumne with the sum of two magnitudes
            check if units is either ml or oz
                convert the volume to same units
                return the Volumne with the sum of two magnitudes
        else
            add the int/float to the magnitude
            return Volume with the new magnitude
                    
        '''
        
        if isinstance(other, Volume):
            if  self.get_units() == other.get_units():
                mag = self.get_magnitude()+other.get_magnitude()
                out = Volume(mag, self.get_units())
                return out
            
            else:
                if self.get_units() == "ml":
                    new_V = other.metric()
                    mag = self.get_magnitude() + new_V.get_magnitude()
                    out = Volume(mag)
                    return out
                
                elif self.get_units() == "oz":
                    new_V = other.customary()
                    mag = self.get_magnitude() + new_V.get_magnitude()
                    out = Volume(mag, self.get_units())
                    return out
        else:
            if type(other) == int or type(other) == float:
                mag = self.get_magnitude() + other
                out = Volume(mag, self.get_units())
                return out
                
            
            
            
            
    def sub(self, other): # this line is incomplete: parameters needed
        '''
        check if the type of other is also a Class
            check if the units is same
                return the Volumne with the difference of two magnitudes
            check if units is either ml or oz
                convert the volume to same units
                return the Volumne with the difference of two magnitudes
        else
            subtract the int/float to the magnitude
        '''
        
        if isinstance(other, Volume):
            if  self.get_units() == other.get_units():
                mag = self.get_magnitude() - other.get_magnitude()
                out = Volume(mag, self.get_units())
                return out
            
            else:
                if self.get_units() == "ml":
                    new_V = other.metric()
                    mag = self.get_magnitude() - new_V.get_magnitude()
                    out = Volume(mag)
                    return out
                
                elif self.get_units() == "oz":
                    new_V = other.customary()
                    mag = self.get_magnitude() - new_V.get_magnitude()
                    out = Volume(mag, self.get_units())
                    return out
        else:
            if type(other) == int or type(other) == float:
                mag = self.get_magnitude() - other
                out = Volume(mag, self.get_units())
                return out
        
