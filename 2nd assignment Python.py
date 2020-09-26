#!/usr/bin/env python
# coding: utf-8

# # 2 Nd assignment #
# 

# In[2]:


#Mailing Address#
FirstName="Saunak"
LastName="Banerjee"
Domain="@gmail.com"
ename=".Banerjee"

print(FirstName, LastName)
print(FirstName+ename+Domain)


# In[3]:


#Hello#
Name=input("Enter your name:")
print("Hello %s!" %Name)


# In[1]:


#Area of a Room#
W=float(input("Enter the width:"))
L=float(input("Enter the length:"))
unit = input("Enter the measure unit (e.g. in, cm) : ")
Area=W*L
print("Area is %s" %Area,unit+"2")


# In[3]:


#Area of a Field#
W=float(input("Enter the width:"))
L=float(input("Enter the length:"))
factor=43560
unit = input("Enter the measure unit in feet: ")
areaunit = input("Enter the measure unit in acres: ")
Area=W*L
Converunit=Area/factor
print("Width is %s" %W,unit)
print("Length is %s" %L,unit)
print("Converunit is %s" %Converunit,areaunit)


# In[26]:


#Bottle Deposits#
Container=int(input("Enter the number of containers used:"))
ContainerLiters=int(input("Enter the how much liters containers(provide data in round figure like 1 or 2:"))
Total=Container*ContainerLiters
unit = input("Unit used(doller /$: ")
d1=0.10
d2=0.25
if Total<=1:
    deposit=d1
print("Total deposit %s" %deposit,unit)
   else:
    Total>=1
     deposit=d2*total
print("Total deposit %s" %deposit,unit)


        
    


# In[4]:


#Tax and Tip#
MC=int(input("Enter the cost of the meal:"))
Tax=11
CalcTax=11/100
Tip=round((MC*0.18),2)
TC=(MC*CalcTax)+Tip
unit=input("Enter in Rupees(rs): ")
unit1=input("Enter in percentage(%): ")
GrandTotal=round((MC+TC+Tip),2)
print("Tip %s" %Tip,unit)
print("Applied tax %s" %Tax,unit1)
print("Grand Total %s" %GrandTotal,unit)


# In[30]:


#Sum of the First n Positive Integers#
n=int(input("provide the integer positive value:"))
if (n>0):
    val=n
    print("User provides a positive number")
calculate=(val)((val+1)/2)
print("calculated value is %s" %calculate)


# In[15]:


#Widgets and Gizmos#
unit = input("Enter the weight units(in grm): ")
Rupee=str("Rs")
w=75
g=112
print("widgets weight %s" %w,unit)
print("gizmos weight %s" %g,unit)

Widgets=int(input("Enter the number of widgets:"))
Gizmos=int(input("Enter the number of gizmos:"))
wiz1=(w*Widgets)
giz1=(g*Gizmos)
Totalweight= (wiz1+giz1)
print("Final total price of the order %s" %Totalweight,Rupee)


# In[3]:


#Compound Interest#
D=int(input("Provide the diposite amount:"))
Rupee=str("Rs")
Percentage=str("%")
IR=4/100
Y=int(input("Provide the year upto which user wants to keep the amount:"))
Interest=D*IR*Y
Totalamountataccount= D+Interest
print("Deposited amount %s" %D,Rupee)
print("Percentage of interest %s" %IR,Percentage)
print("Calculated interest %s" %Interest,Rupee)
print("Sum assured %s" %Totalamountataccount,Rupee)


# In[5]:


#Arithmetic#
a=int(input("Provide an intiger number:"))
b=int(input("Provide an intiger number:"))
sum=a+b
Substraction=a-b
product=a*b
quotent=a//b
remainder=a%b
print("sum %s" %sum)
print("Substraction %s" %Substraction)
print("product %s" %product)
print("quotent %s" %quotent)
print("remainder %s" %remainder)



# In[ ]:




