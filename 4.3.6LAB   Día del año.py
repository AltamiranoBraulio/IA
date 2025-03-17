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
    if month < 1 or month > 12 or year < 1:
        return None
    