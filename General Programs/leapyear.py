# Que.Write a program to check if a year is a leap year.

while True :
    try :
        year = int(input( "Enter the year :"))
        if year > 0 :
            break
    except ValueError :
        print("Enter Valid Year e.g.(1980,2010 etc.) !")

if year % 100 == 0 :
    if year % 400 == 0 :
        print(f"{year} Is a Leap Year !")
    else :
        print(f"{year} Is Not a Leap Year !")
elif year % 4 == 0 :
    print(f"{year} Is a Leap Year !")
else :
    print(f"{year} Is Not a Leap Year !")