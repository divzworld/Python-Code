# Que.  Write a program to append text to a file and display its content.

with open ("File4.txt" , "w" ) as file :
    file.write("""A trusting little leaf of green,
A bold audacious frost;
A rendezvous, a kiss or two,
And youth for ever lost.
""")
    
with open ("file4.txt" , "a") as f :
    f.write("Voila ..... Hello ! Its append statement working here ...... ")