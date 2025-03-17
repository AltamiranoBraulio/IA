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
    

    days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  


    if month == 2 and is_year_leap(year):
        return 29
    return days_per_month[month]



def day_of_year(year, month, day):
    if month <1 or month > 12 or year < 1 or day < 1:
        return None
    

    days_in_current_month = days_in_month(year, month)

    if day >days_in_current_month:
        return None 
    

    total_days = sum(days_in_month(year, m) for m in range(1, month)) + day 
    return total_days 


test_dates=[
    (1900, 2, 28),  
    (2000, 2, 29),  
    (2016, 1, 15),  
    (1987, 11, 30), 
    (2024, 2, 29),  
    (2023, 6, 31),  
    (2023, 13, 5),  
    (-5, 5, 10), 
]


expected_results=[59, 60, 15, 334, 60, None, None, None]

for i in range (len(test_dates)):
    yr, mo, dy = test_dates[i]
     
                  
