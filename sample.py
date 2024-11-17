# Check the list and if elt. is divided by 3 then relace that elt. with "Three" same for "Five"
# and "ThreeFive"

list = [2,4,5,6,10,15]
for i in range(len(list)) :
    if list[i] % 3 == 0 and list[i] % 5 == 0 :
        list[i] = "ThreeFive"
    elif list[i] % 5 == 0 :
        list[i] = "Five"
    elif list[i] % 3 == 0 :
        list[i] = "Three"
    else :
        pass

print(list)