# Que. Write a program to read a text file and count the number of lines and words.

import os

filename = "file1.txt"
with open( filename , "r+") as file :
    try :
        file.write(" Hello World !\n How are you !\n I hope you are doing all\t good : ) ")

        content = file.readlines()
        line = len(content)
        print(f" In current file {filename} {line} Lines Existed ! ")
    except FileNotFoundError as f :
        print(f)