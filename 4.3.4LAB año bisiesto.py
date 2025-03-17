def is_year_leap(year):
    if (year % 400==0)
        return True
    elife(year % 100==0)
        return False
    elif (year % 4==0)
        return True
    else:
        return False

test data = [1900, 2000, 2016, 1987]
test results = [False, True, True, False]

for i in range(Len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    if is_year_leap(yr):
        print("ok")
    else:
        print("fallido")