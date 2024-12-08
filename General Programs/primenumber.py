# Que. Print all prime numbers between 1 and 100.

num = 2
while num < 101 :
    count = 0
    for i in range (2, int(num**0.5)+1) :
        if num % i == 0 :
            count += 1

    if count > 0 :
        pass
    else :
        print(num)
    num += 1