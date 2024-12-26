# Que.  Write a program to find and replace a specific word in a text file.

with open ("file5.txt" , "w") as f :
    f.write("""She called him a bastard after he 
ignored her efforts to help, which only made things worse.\n 
'You’re such a useless jerk,' she shouted, her frustration boiling over.\n
He retorted by calling her stupid and stormed out, leaving the argument unresolved.""")

with open ("file5.txt" , "r") as f :
    content = f.read()


List = ['bastard' , 'worse' , 'useless' , 'jerk' , 'stupid' , 'stormed']

for word in List :
    if word in content :
        content = content.replace(word , "@#$!")

with open ("file5.txt" , "w") as f :
    f.write(content)