# Que. Write a program to copy the contents of one file to another.

with open ("File3.txt" , "w" ) as file :
    file.write("""A trusting little leaf of green,
A bold audacious frost;
A rendezvous, a kiss or two,
And youth for ever lost.
""")

with open ("File3.txt" , "r" ) as file :
    content = file.read()


with open("copyfile3.txt", "w") as f1 :
    f1.write(str(content))
file.close()