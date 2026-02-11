t=f"Hello, Knovista!"
print(t)

# task2

t="Abhi"
print("Hello,",t)

# datatype tasks

# task 1
x=input("Enter anything ")
try:
    value=int(x)
    print("Number = ",value)
    print("datatype = ",type(value))
except ValueError:
    try:
        value=float(x)
        print("Number = ",value)
        print("datatype = ",type(value))

    except ValueError:
        print("Number = ",x)
        print("datatype = ",type(x))

# task 2


radius=int(input("Enter the radius : "))
area=3.14 * radius **2
print("Area of circle is : ",area)

#task 3

num=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
print(num//num2)
print(num%num2)
