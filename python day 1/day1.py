#task 1
print("hello","world", sep=" ",end=" ")
print("welcome","python", sep=" ")
print("laptop","mouse","keyboard", sep="|")

#task 2
name="ravi"
age=22
city="chennai"
print(name,age,city,sep="-")

#task 3
s_name,s_age,student="meena",20,True
print(s_name,s_age,student)

#task 4
word="python"
print(word[0],word[2],word[5]) #ptn

#task 5
print(25+10) #35
print(50-20) #30
print(8*5) # 40
print(100/10) #10
print(10%3) #1
print(2**4) #16
print(20//3) #6

#task 6
"""
the answer will be 53. 
since, it will fistr calculate 5**2 then 25*2
and finally it will add 50+3
"""
print(3+2*5**2)

#task 7
num=50
num+=25
print(num) # num =75

number=100
number/=10
print(number) #number = 10

#task 8
print(10>5,20<5,5==5,10!=8,7>=7,6<=2) #true,false,true,true,true,false

#task 9
"""
they are not equal because it case sensitive so they 
will be treated as different characters.
"""
a="apple"
b="Apple"
print(a==b)

#task 10
print(10>5 and 5==5) #true
print(5>10 or 10==10) # true
print(not(5>2)) #false

#task 11
numbers=[10,20,30,40,50]
print(20 in numbers, 60 in numbers,30 not in numbers) # true,false,false

#task 12
c=10
d=20
c,d=d,c
print(c,d)
"""another way to do is simply using temp,
but to avoid error from same variable name i use e and f
"""
e=50
f=100
temp=e
e=f
f=temp
print(e,f)

#task 13
"""
6=110
3=011
now,

110
^ 011
-------
   101
   after this,we again convert result as decimal.
   answer will be 5
"""
ab=6
cd=3
print(ab^cd)
