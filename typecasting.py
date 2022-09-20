#TYPE CASTING IN PYTHON
num1=10.00
print(num1)
print(type(num1))# num1 is initially floatc
num2=int(num1)
print(num2)
print(type(num2))

#OUTPUT
'''
10.0
<class 'float'>
10
<class 'int'>
'''
------------------------------------------------------------------------------------------------------------

#TYPE CASTING WITH USER INPUTS
#EVERY INPUTS AS DEFAULTLY CONSIDERED AS STRING
 num1=(input("ENTER NUMBER 1:"))
num2=(input("ENTER NUMBER 2:"))
sum=num1+num2
print(sum)

'''
OUTPUT
ENTER NUMBER 1:12
ENTER NUMBER 2:12
1212
'''
-------------------------------------------------------------    
#DATATYPE STRING IS CONVERTED INTO INTEGER TYPE         
num1=int(input("ENTER NUMBER 1:"))
num2=int(input("ENTER NUMBER 2:"))
sum=num1+num2
print(sum)
'''
OUTPUT
ENTER NUMBER 1:12
ENTER NUMBER 2:12
24
'''
