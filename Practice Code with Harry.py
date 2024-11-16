#!/usr/bin/env python
# coding: utf-8

# # Code With Harry

# # Chapter 01

# In[1]:


#01 Write a program to print twinkle twinkle poem
print(''' Twinkle, twinkle, little star
 How I wonder what you are
 Up above the world so high
 Like a diamond in the sky''')


# In[2]:


#02 Install an external module & use it an perform an operation of your interest
# import required module
get_ipython().system('pip install playsound')


# In[3]:


from playsound import playsound
# for playing 
playsound('C:\Users\divuy\Music\Chaleya(PagalWorld.com.pe).mp3')
print('playing sound using  playsound')


# In[ ]:


#03 Write a python program to print the contents of a directory using OS module . Search online for the function which does that.
import os
print(os.listdir())


# In[ ]:


a=3
b=5
print("Sum is : ",a+b)


# In[ ]:


# Chapter 2


# In[ ]:


# wap to add two numbers
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
print("Addition of num1 & num2 :",num1+num2)


# In[ ]:


# wap to find remainder when a number is divided by 2.
num=int(input("Enter the number :"))
print("Remainder after divided by 2 for entered number is :",num%2)


# In[ ]:


#check the type of the variable assigned using input() function
var=input("Enter the variable :")
print(type(var))


# In[ ]:


# use comparison operator to find out whether a given variable a is greater then b or not take a=34 and b=80
a=34
b=80
print(type(a))
if(a>b):
    print("a is greater than b")
else:
    print("b is greater than a")
print(a>b)
    
#wap to find average of two user entered numbers.
num1 = int(input("Enter the number :"))
num2 = int(input("Enter the number :"))
sum = num1 + num2
print("Average :",sum/2)
avg = sum / 2
print(type(avg))


# In[ ]:


# wap to calculate square of given number
num=int(input("Enter the number :"))
print("Square of entered number :",num**2)


# In[ ]:


# String reverse
str=input("Enter String :")
print(str)
print(str[::-1])
print(str[:-2])


# In[ ]:


# wap to display a user entered name followed by Good Afternoon using input()
name=input("Enter Name :")
print(" Good Afternoon !",name)


# In[ ]:


#wap to fill in a letter template given below with name and date letter='''Dear <|NAME|> you are selected ! <|DATE|>'''
letter=''' Dear <|NAME|>
\t You are Selected !
 <|DATE|>'''
name=input("Enter Name :")
date=input("\n Enter Date :")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)


# In[ ]:


#wap to detect double spaces in a string
str=input("Enter String :")
print(str)
if str.find("  "):
    print("Double space detected !")
else:
    print("Double space not present !")
ds=str.find("  ")
print(" index :",ds)


# In[1]:


#wap to detect double spaces in a string
str=input("Enter String :")
if "  " in str:
    print("Space detected !")
else:
    print("Space not detected !")
ds=str.find("  ")
print(" index :",ds)


# In[ ]:


#replace the double spaces with single space 
str="a  b  c d"
print(str)
str=str.replace("  "," ")
print(str)


# In[2]:


''' wap to format the following letter using escape sequence characters
letter="Dear Harry , This Python Course is nice . Thanks !"'''
letter="Dear Harry ,\n \tThis Python Course is nice . \n \t\tThanks !"
print(letter)


# In[ ]:


# Check String is palindrome or not
str=input("Enter String :")
str=str.lower()
print(str)
#Check palindrome or not
str2=str[::-1]
if str==str2:
    print("String is palindrome")
else:
    print("String is not palindrome")
   


# In[ ]:


#Check String is symmetrical(if we fold both parts are same e.g. khokho) or not
import sys


def test_fun(input_str, start_ind1, end_ind1, start_ind2, end_ind2):
    temp_str1 = ''
    temp_str2 = ''
    for ind,char in enumerate(input_str):
        if ind >= start_ind1:
            temp_str1 +=  char
        if ind == end_ind1:
            break
    return temp_str1
    print(temp_str1)
    for ind,char in enumerate(input_str):
        if ind >= start_ind2:
            temp_str2 +=  char
        if ind == end_ind2:
            break
    return temp_str2
    print(temp_str2)
    
    if temp_str1 == temp_str2:
        print( " Symmetric string !")
    else:
        print( " Asymmetric string !")
    


def for_even(input_str):
    # for first part of input_str
    end_ind1 = (len(input_str)/2) - 1
    start_ind1 = 0
    
    # for second part of input_str
    start_ind2 = len(input_str)/2
    end_ind2 =  len(input_str) - 1
    test_fun(input_str, start_ind1, end_ind1, start_ind2, end_ind2)

    
def for_odd(input_str):
    # for first part of input_str
    end_ind1 = (len(input_str)//2) - 1
    start_ind1 = 0
    
    # for second part of input_str
    start_ind2 = len(input_str)//2 + 2
    end_ind2 = -1
    test_fun(input_str, start_ind1, end_ind1, start_ind2, end_ind2)    
    
    

def main():
    input_str = input("Enter String :")
    input_str = input_str.lower()
    input_len = len(input_str)
    print(input_len)
    if input_len % 2 == 0:
        print("Even !")
        for_even(input_str)
    else:
        print("Odd !")
        for_odd(input_str)
if __name__ == "__main__":  
    main()


# In[ ]:





# In[ ]:





# # Chapter 04 Lists and Tuples

# In[ ]:


# 01. WAP to store seven fruits in a list entered by the user
list = []
print(type(list))
i=0
print(type(i))
while i<7 :
    list.append(input( " Enter Fruit : "))
    i+=1

print(list)


# In[3]:


# 02. WAP to accept marks of 6 students and display them in a sorted manner
marks=[]
i=0
while i<6 :
    marks.append(int(input(" Enter Marks of subject :")))
    i+=1
marks.sort()   
print(marks)


# In[ ]:


# 03. Check that a tuple cannot be changed in python
tup=(10,20,30,'Asmita')
print(type(tup))
try :
    tup[2]=76
    print(tup)
except Exception as e :
    print(" Tuples are immutable ! We can not change value of it " , e)


# In[4]:


# 04. WAP to sum a list with 4 numbers.
list1=[10,20,30,40]
list2=[40,50,60,70]
print(list1+list2)

#sum of a list
print(list1[0]+list1[1]+list1[2]+list1[3])
print(list2[0]+list2[1]+list2[2]+list2[3])

print(sum(list1))
print(sum(list2))

print(list1[0]+list2[0],list1[1]+list2[1],list1[2]+list2[2],list1[3]+list2[3])


# In[7]:


# 05. WAP to count the number of zeros in the following tuple
tup=(10,2,3,0,0,45,67,70,67,56,0)
print(tup.count(0))
print(tup.index(2)) # searching value 2 is at which index

tup2=(7,0,8,0,0,9)
print(tup2.count(0))
print(tup2.index(8)) # searching value 8 is at which index
print(tup2.index(0))


# # Random interview question

# In[ ]:


#print every number between 1 and 100 as follows:
# * For every multiple of 3 print "Three".
# * For every multiple of 5 print "Five".
# * And for every multiple of both 3 and 5 print "ThreeFive"

i=1

while i<=100 :
    # For every multiple of both 3 and 5 print "ThreeFive"
    if i % 3 == 0 and i % 5 == 0 :
        print(" ThreeFive ")
        
    #  For every multiple of 3 print "Three" 
    elif i % 3 == 0 :
        print( " Three ")
        
    # For every multiple of 5 print "Five"
    elif i % 5 == 0 :
        print( " Five ")
        
    else:
        print( i )
    i += 1


# In[ ]:


# Determine whether a positive integer number is colorful or not.
#263 is a colorful number because [2, 6, 3, 2x6, 6x3, 2x6x3] are all different; whereas 236 is not colorful, because [2, 3, 6, 2x3, 3x6, 2x3x6] have 6 twice.
#So take all consecutive subsets of digits, take their product and ensure all the products are different.


# In[ ]:





# In[ ]:





# # Chapter 05 - Dictionary and Sets
# 

# In[8]:


# 01 WAP to create a dictionary of Hindi words with values as their english translation . Provide user with an option to look it up !
dict1={
    "Sapna" : "Dreams",
    "Khamoshi" : "silence",
    "Ghussa" : "Anger",
    "Sundar" : "Beautiful"
}
print(dict1)
print(" Options are :", dict1.keys())
a = input ( "Enter Hindi Word :")
try :
    print("English meaning of entered hindi word :",dict1[a])
except Exception as e :
    print("Sorry your entered hindi word is not available !",e)


# In[9]:


# 01 WAP to create a dictionary of Hindi words with values as their english translation . Provide user with an option to look it up !
dict1={
    "Sapna" : "Dreams",
    "Khamoshi" : "silence",
    "Ghussa" : "Anger",
    "Sundar" : "Beautiful"
}
print(dict1)
print(" Options are :", dict1.keys())
a = input ( "Enter Hindi Word :")
print("English meaning of entered hindi word :",dict1.get(a)) # Not through any error


# In[10]:


# 02 WAP to input eight numbers from the user and display all the unique numbers (once)
unique_set = set()
i=0
while i<8 :
    unique_set.add(input("Enter number :"))
    i += 1
print(unique_set)    


# In[11]:


# 03 Can we have a set with 18(int) and "18"(str) as a value in it
sett=set()
sett.add(18)
sett.add("18")
print(sett)
print(type(list(sett)[0]))
print(type(list(sett)[1]))


# In[12]:


# 04 what will be the length of following set s
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
len(s)
print(type(list(sett)[1]))


# In[13]:


a=20.0
type(a)


# In[17]:


# 05 check type of s={}
s={}
print(type(s))
s1 = set()
type(s1)


# In[18]:


# 06 Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names. assume that the names are unique.
fav_lan={}
i=0
while i<4 :
    frd={input("Enter name :") : input("Enter favourite language :")}
    fav_lan.update(frd)
    i += 1
print(fav_lan)


# In[ ]:


fav_lan={}
a=input("\n Enter Your Faourite language Divya :")
b=input("\n Enter Your Faourite language Onkar :")
c=input("\n Enter Your Faourite language Sakshi :")
d=input("\n Enter Your Faourite language Pooja :")
fav_lan["Divya"]=a
fav_lan["Onkar"]=b
fav_lan["Sakshi"]=c
fav_lan["Pooja"]=d
print(fav_lan)


# In[19]:


my_dict={
    "sanket" : "435",
    "Sanket" : "435"
}
print(my_dict)    


# In[20]:


# What happen if names (keys) are same
fav_lan={}
a=input("\n Enter Your Faourite language Divya :")
b=input("\n Enter Your Faourite language Divya :")
c=input("\n Enter Your Faourite language Sakshi :")
d=input("\n Enter Your Faourite language Pooja :")
fav_lan["Divya"]=a
fav_lan["Divya"]=b
fav_lan["Sakshi"]=c
fav_lan["Pooja"]=d
print(fav_lan)


# In[21]:


# What if values are same
fav_lan={}
a=input("\n Enter Your Faourite language Divya :")
b=input("\n Enter Your Faourite language Onkar :")
c=input("\n Enter Your Faourite language Sakshi :")
d=input("\n Enter Your Faourite language Pooja :")
fav_lan["Divya"]=a
fav_lan["Onkar"]=b
fav_lan["Sakshi"]=c
fav_lan["Pooja"]=d
print(fav_lan)


# In[ ]:


# Can you change the value inside a list which is contained inside in set s
# s={ 8, 7,12 , "Harry" , [1,2]}
Ans - - > Set is hashable so we can't change the value of it 


# # Chapter 06 Conditional Expressions

# In[ ]:


# 01 wap TO find greatest user entered number from 4 numbers

i = 0
a = 0
b = 0 
c = 0 
d = 0
while i<4 :
    temp = input("Enter the number :")
    if a == 0 :
        a = temp
    elif b == 0 :
        b = temp
    elif c == 0 :
        c = temp
    else :
        d = temp
    i += 1
    
if a > b and a > c and a > d :
    print ( a , " IS a largest number ")
elif b > a and b > c and b > d :
    print ( b , " Is a largest number ")
elif c > a and c > b and c > d :
    print( c , " Is a largest number ")
elif d > a and d > b and d > c :
    print ( d , " Is a largest number ")
else :
    print (" All are equal")
    
    


# In[ ]:


num1 = int(input("\nEnter Number 1 :"))
num2 = int(input("\nEnter Number 2 :"))
num3 = int(input("\nEnter Number 3 :"))
num4 = int(input("\nEnter Number 4 :"))

if num1 > num2 :
    f1 = num1
else :
    f1 = num2
    
if num3 > num4 :
    f2 = num3
else:
    f2 = num4
    
if f1 > f2 :
    print(str(f1), " Is greatest number ")
else :
    print(str(f2), " Is greatest number ")


# In[ ]:


a = None
type(a)
a=1
type(a)


# In[23]:


# 02 WAP to find out whether the student is pass or fail , in total 40 % marks needed and atleast 33 % require in each subject
i = 1
sub1 = 0
sub2 = 0
sub3 = 0
count1=0
count2=0
while i < 4 :
    temp = int(input(f"Enter the marks of subject {i} :"))
    if temp < 0 or temp > 100 :
        i -= 1
        temp = 0
        print(" Please enter valid marks in between 0 to 100 ")
    
    if sub1 == 0 :
        sub1 = temp
        if sub1 > 33 :
            print(" Pass in subject 1")
            count1 += 1
        else :
            print(" Fail in subject 1")
            count2 += 1
    elif sub2 == 0 :
        sub2 = temp 
        if sub2 > 33 :
            print(" Pass in subject 2")
            count1 += 1
        else :
            print(" Fail in subject 2")
            count2 += 1
    else :
        sub3 = temp
        if sub3 > 33 :
            print(" Pass in subject 3")
            count1 += 1
        else :
            print(" Fail in subject 3")
            count2 += 1
    i += 1
sum = sub1 + sub2 + sub3
if sum > 40 and count1 == 3 :
    print(" You are pass ! ")
elif sum > 40 and count1 == 2 :
    print(" ATKT ")
elif count2== 3 :
    print(" Fail & Year down !")
else:
    print(" Fail !")

# 03 A spam comment is defined as a text containing following passwords :
# " make a lot of money " , " buy now " , " subscribe this " , " Click this " WAP to detect these spams

text = input(" Enter the text : ")
text=text.lower()
spam = False 

if "make a lot of money" in text :
    spam = True
elif "buy now" in text :
    spam = True
elif "subscribe this" in text :
    spam = True
elif "click this" in text :
    spam = True
else :
    spam = False

if(spam):
    print("Stay alert ! Spam detected !")
else :
     print(" Relax there is no spam ! You are safe ! ")
    
# In[25]:


# 04 WAP to find whether a given username contains less than 10 characters or not 
username = input( "Enter the username :")
count=len(username)
if count < 10 :
   print(" Username contains less than 10 characters that is ", count)
elif count == 10 :
   print(" Username contains exact 10 characters !")
else :
   print( " Username contains more than 10 characters that is ", count)


# In[ ]:


# 05 WAP which finds out whether a given name is present in a list or not
name_list = ['Divya' , 'Tanuja' , 'Sai' , 'Pankaj' , 'Trupti' , 'Sonali']
print(type(name_list))
name = input (" Enter the name :")
name = name.capitalize()
if name in name_list :
    print(f"Entered name {name} is present in a list ")
else :
    print(f"Entered name {name} is not present in a list")


# In[ ]:


# 06 WAP to calculate the grade of a student from his marks from the following scheme :
# 90-100 -> Ex
# 80-90 - > A
# 70-80 -> B
# 60-70 - > C
# 50-60 -> D
# <50 - > F
marks = int(input("Enter the marks in between 0 to 100 :"))
if marks < 0 or marks > 100 :
    print (" Invalid marks !")
elif marks > 90 and marks <= 100 :
    grade = "Excellent !"
elif marks > 80 and marks <= 90 :
    grade = "A"
elif marks > 70 and marks <= 80 :
    grade = "B"
elif marks > 60 and marks <= 70 :
    grade = "C"
elif marks >= 50 and marks <= 60 :
    grade = "D"
else :
    grade = "F"
print(" Your grade is :", grade)


# In[ ]:


# 07 WAP to find out whether a given post is talking about " harry " or not ?
post = input ("Enter the text :")
post = post.lower()
if "harry" in post :
    print ( " Post is talking about Harry !")
else :
    print ( " Post is not talking about Harry !")


#  # Chapter 07 Conditional Expressions

# In[26]:


# using while print elements from the list

fruits = [' Watermelon ' , ' Grapes ' , ' Apple ' , ' Banana ' , ' Kiwi ']
i = 0
while i < len(fruits) :
    print (fruits[i])
    i += 1
    


# In[ ]:


fruits = [' Watermelon ' , ' Grapes ' , ' Apple ' , ' Banana ' , ' Kiwi ']
for i in fruits :
    print(i)


# In[27]:


for i in range(1,8,2) :
    print(i)


# In[ ]:


# 01 wap to print multiplication table of a given number using for loop

num = int(input(" Enter the number : "))
for num in range (num , num*10+num , num) :
    print( num )


# In[ ]:


num = int(input(" Enter the number : "))
for i in range (1 , 11) :
    print( str(num)+" X "+ str(i)+" = "+ str(num*i) )
    print(f" {num} X {i} = {num*i}")


# In[28]:


# 02 wap to greet all the person names stored in a list l1 and which starts with s
l1 = ['Sadhana' , 'Sushma ' , 'Sakshi ' , ' Pranali' , ' Nakukl ' ]
for name in l1 :
    if name.startswith('S') :
        print(f"Hello {name} !")
    else:
        continue
        


# In[ ]:


# 03 Attempt problem 1 using while loop

num = int( input( " Enter the number : "))
i=1
while i<=10 :
    print(f"{num} X {i} = {num*i}")
    i += 1


# In[ ]:


# 04 WAP to find whether a given number is prime or not
num = int(input(" Enter the number : "))
prime = True

for i in range(2,num) :
    if num % i == 0 :
        prime = False
        break
        
if prime :
    print ( " Given number is prime number ! ")
else :
    print ( " Given number is not prime number ! ")


# In[29]:


num= 5.6
print(type(num))
num=round(5.6)
print(num)


# In[ ]:


# 05 WAP to find the sum of first n natural numbers using while loop

num = int ( input ( " Enter the number : "))
i = 1
sum = 0
while i <= num :
    sum = i + sum
    i += 1
print( f" The sum of first {num} natural numbers is : ", sum)


# In[ ]:


# 06 WAP to calculate the factorial of a given number using for loop

num = int ( input ( " Enter the number : "))
fact = 1

for i in range ( 1, num+1) :
    fact = fact * i
    i += 1
    
print ( f" The factorial of {num} : " , fact )


# In[ ]:


num = int ( input ( "Enter the number : "))
fact = 1
i = num

while i > 0 :
    fact = fact * i
    i -= 1

print ( f"The factorial of {num} : " , fact )


# In[ ]:


# WAP to print the following star pattern
#     *
#   * * *
#  * * * * *  for n = 3

n = 3

for i in range ( 3 ) :
    print (" " * (n-i-1) , end = " ")
    print (" * "* (2*i+1) , end =" ")
    print (" " * (n-i-1))


# In[ ]:


# WAP to print the following star pattern
# *
# * * 
# * * *   for n = 3

n = 3

for i in range ( 3 ) :
    print ( " * " * ( i + 1 ))


# In[ ]:


# WAP to print the following star pattern
# * * *
# *   *
# * * *   for n = 3

n = 3
for i in range ( 3 ) :
    if i == 1:
        print( )
    print ( " * " * n end = "")
    


# In[ ]:


# WAP to print multiplication table of n using for loop in reversed order

num = int( input(" Enter the number : "))
for i in range ( 10 , 0 , -1 ) :
    print ( f" {num} X {i} = {num*i}")


# In[ ]:


num = int( input(" Enter the number : "))
List = []
j = 0
for i in range ( 1 , 11 ) :
    List.insert(j,num*i)
    j += 1
    
print(List[:-1])
print(List[::-1])


# 
# # Chapter 08 Functions and Recursions
# 
# 

# In[ ]:


# 01 WAP using function to find greatest of three numbers

def greatest(num1 ,num2 ,num3 = 7): # num3 it is dafault argument
    if num1 > num2 and num1 > num3 :
        return num1
    
    elif num2 > num1 and num2 > num3 :
        return num2
    
    else :
        return num3
    
num1 = int( input(" Enter the number 1 : "))
num2 = int( input(" Enter the number 2 : "))
num3 = int( input(" Enter the number 3 : "))
temp = greatest(num1 , num2 , num3 )
print(" The greatest number is : ", temp)

print("The greatest number is :" , greatest(3,6,7))

s = greatest(8 , 9 )
print(" The greatest number is : ", s)


# In[ ]:


# 02 write a python program to convert celsius to fehreinheit

def temp_convert(temp = 45) :
    return (temp * 9/5) + 32
    
    
    
temp = int ( input (" Enter the temperature in celcius : "))
result = temp_convert(temp)
print(f" The temprature {temp} celcius to fahrenheit : " , result )

print(f" The temprature celcius to fahrenheit : " , temp_convert() )


# In[ ]:


# 03 How do you prevent a python print() function to print a new line at the end 
# Note - In Python, the print() function automatically appends a newline character (\n) at the end of the printed output by default. If you want to prevent the print() function from adding a newline, you can use the end parameter.
print("The line" , end="No new line here")
print(" 5")


# In[ ]:


# 04 Write a recursive function to calculate the sum of first n natural numbers

def sumof( num ) :
    sum = 0
    if num == 1:
        return 1
    else :
        return num + sumof(num - 1)

num = int ( input ( " Enter the number : "))
s = sumof(num)
print ( f" The sum of first {num} natural numbers is : ", s)


# In[ ]:


# 05 Write a python function to print first n lines of the following pattern
# * * *
# * *
# *           ---> for n = 3

def pattern( n ) :
    for i in range (n , 0, -1) :
        print(" * "* i , end=" ")
        print("\n")
    
n = 3
pattern(n)


# In[ ]:


# 06 WAP function which converts inches to cms.

def conversion( len ) :
    return len * 2.54
    
    
len = int ( input( " Enter the length in inches : "))
print (f" The length {len} inches is in cm : ", conversion(len))


# In[ ]:


# 07 Write a python function to remove a given word from a string and strip it at the same time

def rem_strip_word( str , word ) :
    new_str=str.replace(word, " ")
    print(new_str)
    print(new_str.strip())
    
str = "     Aisha Tanu Madhu     "
print(str)
word = input (" Enter the word : ")
rem_strip_word( str, word)


# In[31]:


# 08 Write a python function to print multiplication table of a given number 

def table( num ) :
    for i in range (1 ,11) :
        print(f"{num} X {i} = {num*i}")

num = int ( input (" Enter the number : "))
table(num)


# In[30]:


n = 3
for i in range (n ,0 ,-1) :
    print(" * " * i )
    print("\n")


# In[32]:


print (0.1 + 0.2 == 0.3)


#  # Chapter 09 File I/O

# In[ ]:


# 01.WAP to read the text from a given file 'poem.txt' and find out whether it contains the word 'twinkle'.
import os
f = open('C:\\Interviewpreparatiion\\Program practice\Python\\file handling\\poems.txt','r')
t = f.read()
if 'twinkle' in t :
    print(" 'Twinkle' Word is found ! ")
else :
    print("'Twinkle' word is not found !  ")
f.close()


# In[ ]:


# 02.The game() function in a program lets a user play a game and returns the score as an integer . You need to read a file 'History.txt' 
# which is either blank or contains the previous Hi-score . You need to write a program to update the hi-score whenever game()breaks the hi-score.
import os
def game() :
    return 45043

with open('C:\\Interviewpreparatiion\\Program practice\Python\\file handling\\history.txt') as f :
    hiscore = f.read()
score = game()

if hiscore =='' :
    with open('C:\\Interviewpreparatiion\\Program practice\Python\\file handling\\history.txt','w') as f :
        f.write(str(score))
    print(" Score added successfully !")

elif int(hiscore) < score :
    with open('C:\\Interviewpreparatiion\\Program practice\Python\\file handling\\history.txt','w') as f :
        f.write(str(score))
    print(" Score updated successfully !")




# In[ ]:


#03.WAP to generate multiplication table from 2 to 20 and write it to the different files. Place these files in a folder for a 13 year old.

with open('C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\table\\multiplication.txt','w') as f :
    for i in range ( 2, 21) :
        f.write(f"Multiplication table of {i}\n")
        for j in range (1 , 11) :
            f.write(f"{i} X {j} = {i*j}\n")
    
    



# In[ ]:


# 04. A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updates the same file.
with open('C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\poem.txt') as f :
        content = f.read()
content = content.replace('Donkey','#####')

with open('C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\poem.txt','w') as f :
    f.write(content)


# In[34]:


# 05.Repeat program 4 for a list of such words to be censored.
with open('C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\list.txt','w') as f :
    f.write(" Bitch , Pagal Those word are very bad Don't use it and also avoid saying Boolshit")
with open('C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\list.txt') as f :
    content = f.read()
List = ['Bitch' , 'Pagal' , 'Boolshit' ]
for i in List :
    content = content.replace(i , "\t #%*!?#! ")
    with open('C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\list.txt','w') as f :
        f.write(content)
        f.write(" Updated !")
#with open('C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\list.txt') as f :
#    f.write(content)


# In[ ]:


# 06.Write a program to mine a log file and find out whether it contains 'python'.
with open('C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\log.txt') as f :
    content = f.read()
    
if 'python' in content.lower() :
    print ( ' Python word is present !')
else :
    print ( ' Python word is not present !')


# In[ ]:


# 07.WAP to find out the line number where python is present from Que.6

content = True
i = 1
with open('C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\log.txt') as f :
    while content :
        content = f.readline()
        if 'python' in content.lower() :
            print(f" 'python' word present at line number : {i}")
        i+=1


# In[ ]:


# 08.WAP to make a copy of a text file "this.txt".

with open('C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\this.txt') as f :
    content = f.read()
    
with open('C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\copy.txt','w') as f:
    f.write(content)


# In[ ]:


# 09.WAP to find out whether a file is identical & matches the content of another file.

file1 = 'C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\this.txt'
file2 = 'C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\copy.txt'

with open(file1) as f :
    f1 = f.read()

with open(file2) as f :
    f2 = f.read()

if f1 == f2 :
    print (" Files are identical !")
else :
    print (" Files are not identical !")


# In[ ]:


# 10.WAP to wipe out the contents of a file using python.

filename = 'C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\history.txt'
with open(filename,'w') as f :
    f.write(" ")


# In[ ]:


# 11.Write a python program to rename a file to "record_by_python.txt".

import os
oldname = "C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\sample.txt"
newname = "C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\record_by_python.txt"

with open (oldname) as f:
    content = f.read()
with open (newname,'w') as f:
    f.write(content)
    
os.remove(oldname)


# 
# # Chapter 10 OOP
# 

# In[ ]:


# 01. Create a class programmer for storing information of few programmers working at microsoft.

class programmer :
    company = "Microsoft"
    def programmer_info(self , name , salary , age ):
        self.name = name
        self.salary = salary
        self.age = age
        print(f"""Name :{self.name}
                  Salary :{self.salary}  
                  Age :{self.age}""")

# object creation        
obj1 = programmer()        
obj2 = programmer()
obj3 = programmer()

# method call and passing arguments
obj1.programmer_info('Pankaj' , 50000 , 23)
obj2.programmer_info('Divya' , 67000 , 22)
obj3.programmer_info('Rudra' , 69885 , 28)


# In[ ]:


# 02. Write a class calculator capable of finding square , cube and squareroot of a number.
import math

class calculator :
    def __init__(self,num) :
        self.num = num
        
    def square(self) :
        return self.num ** 2
    
    def cube(self) :
        return self.num ** 3
    
    def square_root(self) :
        return math.sqrt(self.num)
    
obj = calculator(int(input("Enter the number :")))
print(f" Square :",obj.square())
print(f" Cube :",obj.cube())
print(f" Square Root :",obj.square_root())


# In[ ]:


# 04. Add a static method in problem 02 to greet the user with " Hello ! "

import math

class calculator :
    def __init__(self,num) :
        self.num = num
        
        
    def square(self) :
        return self.num ** 2
    
    def cube(self) :
        return self.num ** 3
    
    def square_root(self) :
        return math.sqrt(self.num)
    
    @staticmethod
    def greet (name):
        print(f" Hello {name} ! Have a great day :)")
    
obj = calculator(int(input("Enter the number :")))
name = input("Enter user name :")
calculator.greet(name)
print(f" Square :",obj.square())
print(f" Cube :",obj.cube())
print(f" Square Root :",obj.square_root())


# In[ ]:


# 03. Create a class with a class attribute a ; create an object from it and set a directly using object.a = 0. 
# Does this change the class attribute ?

class sample :
    a = 1
    
obj = sample()
print(" Print value of a before modification : ",sample.a)
print(" Print value of a before modification : ",obj.a)


obj.a = 0
print(" Print value of a After modification : ",sample.a) # class attribute obj.a = 0. However,this does not change the class attribute itself
print(" Print value of a After modification : ",obj.a) # instance attribute


# In[35]:


# 05. Write a class Train which has methods to book a ticket , get status (no. of seats) and 
# get fare information of trains running under Indian Railways.

class Train :
    def __init__(self ,name,seats,fare,num,total):
        self.name = name
        self.seats = seats
        self.fare = fare
        self.num = num
        self.total = total
    
    def ticket_booking(self):
        if self.seats > 0 and self.seats >= self.num :
            print( f" Your seat is successufully booked ! Your seat number is {self.seats} - {self.seats - self.num} ")
            self.seats = self.seats - self.num
            self.fare_info()
            print(f" Your total seats are {self.num} and your total amount is : {self.total}")
        else :
            print(" Sorry No seats are available ! Try in 'Tatkal'")
    
    def get_status(self):
        print(f" In {self.name} Railway There are available seats are : {self.seats}")
    
    def fare_info(self):
        option = int(input("Choose which kind of seat you want AC(1) , Non-AC(2) , First-class(3) , General(4) "))
        if option == 1 :
            self.total = (self.fare + 500) * self.num
            return total
        elif option == 2 :
            self.total = (self.fare + 300) * self.num
            return total
        elif option == 3 :
            self.total = (self.fare + 450) * self.num
            return total
        elif option == 4 :
            self.total = self.fare * self.num
            return total
        else :
            print(" Please kindly choose correct option in between 1 to 4 :")
            self.fare_info()   
        #print(f" Your total seats are {self.num} and your total amount is : {total}")
        
name = " Jhelam "
seats = 30 # Available seats are
fare = 340
num = int (input(" Enter how many seats you want to book : "))
total = 0
obj = Train( name , seats , fare , num, total)
obj.ticket_booking()
#obj.fare_info()
obj.get_status()



# In[ ]:


# 06. Can you change the self parameter inside a class to something else (say 'harry') . Try changing self to 'slf' or 'harry'
# and set the effects.

class sample :
    def __init__(slf,name) :
        slf.name = name
        print(slf.name)
        
obj = sample(' Divya ')

# Yes we can change self parameter by any name 


# In[ ]:


#In Python, constructor overloading is not directly supported as it is in some other programming languages like C++ or Java. 
#In Python, a class can have only one constructor, which is the __init__ method.
#However, you can achieve similar functionality by using default parameter values and 
#providing multiple ways to instantiate your class.

#Here's an example to demonstrate constructor overloading-like behavior in Python:

class MyClass:
    def __init__(self, param1=None, param2=None):
        if param1 is not None and param2 is not None:
            # Constructor with two parameters
            self.param1 = param1
            self.param2 = param2
        elif param1 is not None:
            # Constructor with one parameter
            self.param1 = param1
            self.param2 = "default_value"
        else:
            # Default constructor
            self.param1 = "default_value"
            self.param2 = "default_value"

# Creating objects using different constructors
obj1 = MyClass()
print(obj1.param1, obj1.param2)  # Output: default_value default_value

obj2 = MyClass("value1")
print(obj2.param1, obj2.param2)  # Output: value1 default_value

obj3 = MyClass("value1", "value2")
print(obj3.param1, obj3.param2)  # Output: value1 value2
#In this example, the __init__ method takes two parameters, param1 and param2, with default values set to None. 
#Depending on the values passed during the object creation, different constructors are simulated.

#While this approach provides some flexibility, 
#it's essential to document the intended use of each parameter to avoid confusion for users of your class.


# # Chapter 11 Inheritance
# 

# In[ ]:


# 01. Create a class c2dvector and use it to create another class representing a 3-d vector.

class c2dvector :
    def __init__(self,i,j) :
        self.icap = i
        self.jcap = j
        
    def __str__(self) :
        return f"{self.icap}i + {self.jcap}j "
    
class c3dvector(c2dvector) :
    def __init__(self,i,j,k) :
        super().__init__(i,j)
        self.kcap = k
        
    def __str__(self) :
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
d2cev = c2dvector(3,6)
d3vec = c3dvector(4,8,7)
print(d2cev)
print(d3vec)


# In[ ]:


# 02. Create a class pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog.

class Animals :
    def __init__(self,name) :
        self.name = name
        print(" Animals are loyal ! Animals have 2 types Wild and Pet animals ")
        if self.name == 'cat' :
            print('Myav Myav')
        elif self.name == 'dog' :
            print("Bhav Bhav")
        else :
            print(f"no sound information of {self.name}")

class Pets(Animals):
    def __init__(self,name) :
        super().__init__(name)
        print(" Pets are loving nature and nurturing ")

class Dog(Pets) :
    def __init__(self,name) :
        super().__init__(name)
    def bark(self) :
        print(" The sound of Dog known as 'Barking '")
obj1 = Animals('cat')
obj2 = Pets('dog')
obj3 = Dog('dog')


obj3.bark()


# In[ ]:


# 03. Create a class Employee and add salary and increment properties to it. Write a mothod SalarayAfterIncrement() method
# with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee :
    salary = 50000
    increment = 1.5
    
    @property
    def salaryAfterIncrement(self) :
        return self.salary * self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai) : # sai = salary after increment
        self.increment = sai / self.salary
        
emp = Employee()
print( emp.increment)
emp.salaryAfterIncrement = 20000
print( emp.salaryAfterIncrement)
print( emp.increment)
print( emp.salary)


# In[36]:


# 04. Write a class complex to represent complex numbers , along with overloaded operators + and * operator which adds and 
# multiplies them.

class complex :
    def __init__(self , r, i) :
        self.real = r
        self.imaginary = i
        
    def __add__(self,c) :
        return complex(self.real + c.real , self.imaginary + c.imaginary ) 
    
    def __mul__(self , c) :
        mulreal = self.real * c.real - self.imaginary * c.imaginary
        mulimg = self.real * c.imaginary + self.imaginary * c.real
        return complex(mulreal , mulimg)
    
    def __str__(self) :
        if self.imaginary < 0 :
            return f"{self.real} - {-self.imaginary}i"
        else :
            return f"{self.real} + {self.imaginary}i"
        
c1 = complex(3,2)
c2 = complex(1,7)
print(c1 + c2)
print(c1*c2)


# In[ ]:


# 05. Write a class vector representing a vector of n dimension. Overload the + and * operator which calculates the sum and 
# the dot product of them. 

class vector :
    def __init__(self , vec) :
        self.vec = vec
        
    def __str__(self) :
        str1 = ""
        index = 0
        for i in self.vec :
            str1 += f"{i}a{index} +"
            index += 1
        return str1[:-1]
    
    def __add__(self,vec2) :
        newlist = []
        for i in range (len(self.vec)) :
            newlist.append(self.vec[i] + vec2.vec[i])
        return vector(newlist)
    
    def __mul__(self,vec2) :
        sum = 0
        for i in range (len(self.vec)) :
            sum += self.vec[i] + vec2.vec[i]
        return sum
        
        
v1 = vector([2,4,5,6,8])
v2 = vector([3,9,4,1,5])
print(v1 + v2)
print(v1 * v2)


# In[ ]:


# 06. Write __str__() method to print the vector as follows : 
# 7i(cap) + 8j(cap) + 10k(cap)  Assume vector of dimension 3 for this problem.

class vector :
    def __init__(self , vec) :
        self.vec = vec
        
    def __str__(self) :
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v1 = vector([1,3,5])
v2 = vector([2,4,6])
print(v1)
print(v2)


# In[ ]:


# 07. Override the __len__() method on vector of problem 05 to display the dimension of vector.

class vector :
    def __init__(self , vec) :
        self.vec = vec
        
    def __str__(self) :
        str1 = ""
        index = 0
        for i in self.vec :
            str1 += f"{i}a{index} +"
            index += 1
        return str1[:-1]
    
    def __add__(self,vec2) :
        newlist = []
        for i in range (len(self.vec)) :
            newlist.append(self.vec[i] + vec2.vec[i])
        return vector(newlist)
    
    def __mul__(self,vec2) :
        sum = 0
        for i in range (len(self.vec)) :
            sum += self.vec[i] + vec2.vec[i]
        return sum
        
    def __len__(self) :
        return len(self.vec)
        
v1 = vector([2,4,5,6,8])
v2 = vector([3,9,4,1,5])
print(v1 + v2)
print(v1 * v2)
print(len(v1))
print(len(v2))


# # Chapter 12 Advance Python ~ 01

# In[ ]:


# 01. Write a python program to open three files 1.txt 2.txt and 3.txt . If any of these files are not present , 
# a message without exiting the program must be printed prompting the same.
  
try :
    with open("C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\1.txt","r") as f:
        f1 = f.read()
            
    with open("C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\2.txt","r") as f:
        f2 = f.read()
    
    with open("C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\3.txt","r") as f:
        f3 = f.read()
        
#except Exception as e :
 #   print(e)
    
except FileNoFoundError :
    raise FileError(" File not exist ! ")
        
finally :
    print(" Program executed successfully ! ")


# In[ ]:


def FileRead( FileName ) :
    try :
        with open(FileName , "r") as f :
            print(f.read())
    except FileNotFoundError :
        print(f" File {FileName} Not Found ! ")
        
FileRead("C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\1.txt")
FileRead("C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\2.txt")
FileRead("C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\3.txt")


# In[37]:


# 02. Write a program to print third , fifth and seventh element from a list using enumerate function.

list = [2,3,4,"Divya","Era","Rudra","Nakul",87,45]
for i,item in enumerate(list) :
    if i == 3 or i == 5 or i == 7 :
        print(item , i)



# In[ ]:


list = [2,3,4,"Divya","Era","Rudra","Nakul",87,45]
for i,item in enumerate(list) :
    lst =[3,5,7]
    for j in lst :
        if i == j :
            print()


# In[39]:


# 03. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

num = int(input("Enter the number :"))
list1 = [20,3,4,15,6,7,8,91,50,22,34,15,16,18,9]
list2 = []
table = []

for i in range (1, 101) :
    table.append(num * i)
#print(table)

for i in table :
    for j in list1 :
        if i == j :
            list2.append(i)
            
print( list2 )


# In[ ]:


i = 1
print(i)


# In[ ]:


# 04. Write a program to display a/b when a and b are integers. If b = 0 , display infinite by handling the ZeroDivisionError.

a = int ( input(" Enter the dividend : "))
b = int ( input(" Enter the divisor : "))
try :
    print( a/b )
    
except ZeroDivisionError as e :
    print( e )


# In[40]:


# 05. Store the multiplication tables generated in Problem 03 in a file named Tables.txt .

num = int(input("Enter the number :"))
list1 = [20,3,4,15,6,7,8,91,50,22,34,15,16,18,9]
list2 = []
table = []

for i in range (1, 101) :
    table.append(num * i)
#print(table)

for i in table :
    for j in list1 :
        if i == j :
            list2.append(i)
            
print( list2 )
with open("C:\\Interviewpreparatiion\\Program practice\\Python\\file handling\\Tables.txt","w") as f :
    f.write("List2 - The values which are multiplied by user entered number \n")
    f.write(str(list2))
    f.write("\n")
    f.write("Multiplication table of user entered number \n")
    f.write(str(table))



# # Chapter 03 Advance python ~ 02

# In[ ]:


# 01. create a two virtual environments , installs few packages in the first one. How do you create a similar environment
# in the second one.

01 . pip install virtualenv

02. virtualenv env1
    
03. virtualenv env1

04. .\env1\Scripts\activate.ps1     

05. pip freeze > requirements.txt

06. pip install -r requirements.txt   # env2


# In[ ]:


# 02. Write a program to input name , marks and phone number of a student and format it using the format function like below
# " The name of the student is Harry , his marks are 72 and phone number is 99999888 "

name = input( " Enter the name : ")
marks = int(input(" Enter the marks : "))
phone_no = input(" Enter the phone number : ")

data = " Name Of Student :{} \n Marks Obtained : {} \n Phone Number : {} ".format(name,marks,phone_no)

print( data )


# In[ ]:


name = input( " Enter the name : ")
marks = int(input(" Enter the marks : "))
phone_no = input(" Enter the phone number : ")

data = " Name Of Student :{1} \n Marks Obtained : {2} \n Phone Number : {0} ".format(phone_no,name,marks)

print( data )


# In[42]:


# 03. A list contains the multiplication table of 7 . Write a program to convert it to a vertical string of same numbers 
# ( 7 14 ...)

list = [ str(i*7) for i in range(1 , 11 ) ]
print( list )

table = "\n".join(list)
print(table)


# In[43]:


# 04. Write a program to filter a list of numbers which are divisible by 5.

def divisible(num) :
    if num % 5 == 0 :
        return True
    else :
        return False 
    
l = [3,5,6,45,67,60,80,23,13,15,30]
result = list(filter(divisible,l))

print(result)


# In[ ]:


l = [3,5,6,45,67,60,80,23,13,15,30]

result = filter(lambda x : x % 5 == 0 , l)
print(list(result))


# In[44]:


# 05. Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

list = [3,67,45,43,23,91,58,76]

result = reduce(max , list)
print(result)


# In[ ]:


# 06. Run pip freeze for the system interpreter. Take the contents and create a similar virtual environment.

04. .\env1\Scripts\activate.ps1     

05. pip freeze > requirements.txt

06. pip install -r requirements.txt   # env2



# In[ ]:


# 07. Explore the Flask module and create a web server using flask and python.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'


# In[ ]:


# Project 01 Snake , Water , Gun Game

import random

def gamewin( comp , player ) :
    if comp == player :
        print(" Tie ! ")
    elif comp == 's' :
        if player == 'g' :
            return True 
        else :
            return False
    elif comp == 'w' :
        if player =='g' :
            return False
        else :
            return True
    elif comp == 'g' :
        if player == 's' :
            return False
        else :
            return True



print (" Computer Turn : Choose Snake(s)  Water(w) or Gun(g) ?")
randomno = random.randint(1,3)
if randomno == 1 :
    comp = 's'
elif randomno == 2 :
    comp = 'w'
elif randomno == 3 :
    comp = 'g'

player = input ( " It's Your turn : Choose Snake(s)  Water(w) or Gun(g) ? :" )
player_name = input(" Enter your name : ")
gamewin_arg = gamewin( comp , player )


# To show what choose by whom 
print(" Computer Choose : ", comp)
print(" Player Choose : ", player)


if gamewin_arg :
    print ( f" {player_name} You Win !")
else :
    print ( f" {player_name} You lose !")


# In[45]:


# Project 02 . The Perfect Guess
# We are going to write a program that generates a random number and asks the user to guess it.
# If the player's guess is higher than the actual number, the program displays "Lower number please".
# Similarly if the user's guess is too low , the program prints "higher number please" . When the user guesses the player used
# to arrive at the number .

# Hint : use the random module 

import random

ranNumber = random.randint(1,100)
guess = 0
userguess = None

while( userguess != ranNumber ) :
    userguess = int(input(" Enter your guess in between 1 to 100 : "))
    
    if userguess == ranNumber :
        print (" Your guess in correct ! ")
    else :
        if userguess < ranNumber :
            print(" Higher number please ! ")
        else :
            print(" Lower number please ! ")
        guess += 1
print (f" You guess correct at {guess} time")
with open("C:\\Interviewpreparatiion\\Program practice\\Python\\hiscore.txt","r") as f :
    hiscore = int(f.read())
    
if hiscore > guess :
    with open("C:\\Interviewpreparatiion\\Program practice\\Python\\hiscore.txt","w") as f :
        f.write(str(guess))
    print("You've just broken the previous record ! ")
    


# In[ ]:


# Projecct 03- Implement a student library system using OOP's where students can borrow a book from the list of books .
# Create a separate Library and student class . Your program must be menu driven .You are free to choose methods and attributes
# of your choice to implement this functionality .

class library :
    def __init__(self,book) :
        self.books = book
    def bookavailable(self) :
        for book in self.books :
            print("\t * "+book)       
    def borrowbook(self,bookname) :
        self.bookname = bookname
        if bookname in self.books :
            print(f"You are successfully borrowed Book {bookname}")
            self.books.remove(bookname)
        else :
            print("Sorry currently this Book is not available ! Soon you will get this book !")

    def returnbook(self,bookname) :
        self.bookname = bookname 
        self.books.append(self.bookname)
        


if __name__ == "__main__" :
    obj = library(["Algorithms","DSA","Java","Python","C","CPP"])
    while (True) :
        """\n *** Welcome To Central Library ! ***
        Choose Your option wisely
        01 . To check available books 
        02 . To Borrow Book 
        03 . To Add/Return Book
        04 . Exit """
        choice = int(input(" Enter Option : "))
        if choice == 1 :
            obj.bookavailable()
        elif choice == 2 :
            obj.borrowbook(input("Enter Add/Return book name : "))
        elif choice == 3 :
            obj.returnbook(input("Enter Add/Return book name : "))
        elif choice == 4 :
            break
        else :
            print(" Invalid Opt")


# In[ ]:


x = "22_22"
print(float(x))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




