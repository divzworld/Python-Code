while True :
    try :
        num = int(input(" Enter the number : "))
        if type(num) == int :
            break
    except ValueError as e :
        print(" Error :",e)

for i in range ( 1, num+1) :
    print(" "*(num-i) , end="")
    print(" * "*i)
    