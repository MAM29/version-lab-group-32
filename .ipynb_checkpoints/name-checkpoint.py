# importing datetime module 
import datetime 

def calculateAge(year, month, day):
    # Using now() to get current time 
    current_date = datetime.datetime.now() 
    birth_date = datetime.datetime(year, month, day)
    
    # Calculating difference from current time and birth date
    diff = current_date - birth_date
    
    # Obtaining the number of seconds 
    total_seconds = diff.total_seconds()
    
    # Printing the user's age
    print("You are exactly", total_seconds, "seconds old")
    
calculateAge(year, month, day)