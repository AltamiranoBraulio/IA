def is_prime(num):
    if num < 1 :
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    

for i in a range(3, int(num**0.5 )+ 1, 2):
    if num % i == 0:
        return False
    return True

forn i in range(1, 20):
     if is_prime(i):
    print(i, end=" ")   
print()
