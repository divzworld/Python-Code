# Que.  Write a program to delete a specific line from a text file.
try :
    with open ("file6.txt" , "w") as f :
        f.write("You’re an important part of this team, and your efforts make a big difference.\n")
        f.write("Thank you for being so helpful; your support means a lot to me.\n ")
        f.write("bad word\n ")
        f.write("This plan is brilliant; I’m confident it’s going to succeed!\n")

    with open ("file6.txt" , "r") as f :
        lines = f.readlines()

    # Taking input from user to delete specific line
    inputLine = input("Enter the line that you wanted to get deleted :")

    updatedLines = []
    for line in lines :
        if inputLine == line.strip() :
            print(" Line successfully deleted ! ")
            continue
        else :
            updatedLines.append(line)

    with open ("file6.txt" , "w") as f :
        f.writelines(updatedLines)
except FileNotFoundError as e :
    print(" Error : ",e)