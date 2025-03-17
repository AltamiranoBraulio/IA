def is_year_leap(year):
    if (year % 400==0):
        return True
    elif(year % 100==0):   
        return False
    elif (year % 4==0):
        return True
    else:
        return False
    

def days_in_month(year, month):
    if month < 1 or month > 12 or year < 1
       return None
    
    day_per_month= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

    if month == 2 and is_year_leap(year):
        return 29
    return day_per_month[month]


test