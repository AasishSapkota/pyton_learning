#today we are learning about variable and data types in python
a=5        # here we can see that we don't need to decleare data type
b="aasish" # here we can see that we have decleared variable b as string
print("THe value of a =",a)
print("Person behind the desk =",b)

#diffrent types of datastructure
c=1
d="somebody" 
e=True
f=None
print("the type of c=",type(c))
print("the type of d=",type(d))
print("the type of e=",type(e))
print("the type of f=",type(f))

#sequential order
#list is collection of diffrent types of data. that is changable
#tuple is collection of same type of data. It is non changable
list1 = ["aasish","sapkota"],[8,9,10],[1,2,3]  # it is changable
print(list1)
tuple1 = ("ashish","Dhakal"),("manisha","bhandari") # it is non changable
print(tuple1)

#dictionary 
exampledict={"name":"aasish","surname":"sapkota","dob":"2059/10/29"}
print(exampledict)            # to display whole value of dictionary
print("The value inside name:",exampledict["name"])    # just to display value of name from dictionary
