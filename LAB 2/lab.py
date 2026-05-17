# problem 01
a,b = 10,20 
print("a is",a )
print("b is",b)

#problem 02
roll_number = 101
name = "Naveen "
percentage = 90.5
print ("Roll number :",roll_number)
print("Name : ", name )
print( " Pertencage : ", percentage )

#problem 03
name = "Naveen " 
age = 19 
city = "Sikar"
print("Name:",name)
print("age:",age)
print("City: ",city)


#problem 04
name,age,city = str,int,str
input("name : ")
input("age :")
input("city :")

#problem 05
num = 10 
print( "Value of num initially :" ,num)
num = 20
print("Value of num after change:" , num)

#problem 06
name = input("Enter yor name:")
print("HELLO ", name)


#problem 07
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
print("Sum:",a+b)
print("Difference:", a-b)
print("Product:",  a*b)
print("Quotient:",  a/b)
print("Remainder:" , a%b)

#problem 08
item1 = int(input("Enter price of item1:"))
item2 = int(input("Enter price of item2:"))
item3 = int(input("Enter price of item3:"))
Total = item1 +item2+item3
print("Total Bill:",Total)

#problem 09 
a = int(input("Enter a number:"))
print(a**2)
print(a**3)

#problem 10
Celsicus =float(input("Enter Temp in celsicus"))
Fahrenheit= (Celsicus*9/5)+ 32
print("temp in fahrenheit:",Fahrenheit)

#problem 11
hindi,math,science,english,it = 84,25,95,45,34
total =hindi+math+science+english+it
print("The total marks is :",total)

#problem 12
word1,word2,word3 ="Python \t","is\t","fun\t"
print(word1+word2+word3)

#problem 13
side = int(input("Enter side of square :"))
perimeter = 4*side
print("perimeter of square:",perimeter)

#problem 14
P = int(input("Enter price:"))
R = int(input("Enter rate:"))
T = int(input("Enter time:"))
SI = (P*R*T)/100
print("The value of SI is :",SI)

#problem 15 
name = "Naveen khandal"
age = 19
gender = "Male "
college = "CU Jammu "
course = " B tech cyber security"
roll_number = "25BECCS49"
contract_no = 9461396384
address =  "Sikar,Rajasthan(India)"
print("\n")
print(".........STUDENT CARD..........")
print("NAME :",name)
print("AGE :",age)
print("GENDER:",gender)
print("COLLEGE:",college)
print("COURSE:",course)
print("ROLL NUMBER:",roll_number)
print("ADDRESS",address)

#problem 16
num = int(input("Enter a number"))
if num >0:
    print("Postive")
elif num < 0 :
    print("Negative")
else:
    print("Zero")


#problem 17
age = int(input("Enter your age :"))
if (age >18):
    print("You eligible for vote ")
else:
    print("You can not vote :")

# problem 18
marks = int(input("Enter marks"))
if marks >= 40 :
    print("Pass")
else:
    print("Fail")


#problem 19
num = int(input("Enter a number "))
if num % 3 ==0 and num %5==0:
    print("Divisible by both 3 and 5")
else :
    print("Not divisible by both 3 and 5")

#problem 20

ch = input("Enter a character :")
if ch.lower() in ['a','e','i','o','u']:
    print("Vowel")

else:
    print("Consonant")


# problem 21 
num = int(input("Enter a number :"))
if num%2 == 0 :
    print(num , " is even")
else :
    print(num," is odd")

#problem 22
marks = int(input("Enter marks (outof 100):"))
if marks >=90:
    print ("Grade : A+")
elif marks >=80:
    print("Grade :A")
elif marks >=70 :
    print("Grade :B")
elif marks >=60 :
    print("Grade :C")
elif marks >= 50 :
    print('Grade :D')
else:
    print("Gade :Fail")    


#problem 23
a= int(input("Enter 1 st side:"))
b = int(input("Enter 2nd side "))
c =int(input("Enter 3rd side "))
if a+b >c and a+c >b and b+c >a :
 print ("Not a triangle")
if a== b==c:
    print ("equilateral")
elif a ==b or b==c or a ==c :
    print ("Isoceles")
else :
    print("Scalene")

   

#problem 24
username = input("Enter username")
if username == "admin":
    print("welcome Admin !")
elif username =="User":
    print("welcome User !")
elif username == "Guest":
    print("Welcome Guest")
else:
    print("Access denied")

#problem 25
year = int (input("Enter a year"))
if (year %400 ==0) or (year %4 == 0 and year%100!=0):
    print(year,"is a leap year")
else :
    print(year, "is not a leap year")