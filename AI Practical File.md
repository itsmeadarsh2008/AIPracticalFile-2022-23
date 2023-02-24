- [Objective 1: Write a program to print average of five subjects.](#objective-1-write-a-program-to-print-average-of-five-subjects)
- [Objective 2: Write program to find area of a circle.](#objective-2-write-program-to-find-area-of-a-circle)
- [Objective 3: Write a program to find larger among three numbers.](#objective-3-write-a-program-to-find-larger-among-three-numbers)
- [Objective 4: Write a program to create a list and sort the elements in descending order.](#objective-4-write-a-program-to-create-a-list-and-sort-the-elements-in-descending-order)
- [Objective 5: Write a program to concatenate two strings.](#objective-5-write-a-program-to-concatenate-two-strings)
- [Objective 6: Write a program to create dictionary and access its elements using key values.](#objective-6-write-a-program-to-create-dictionary-and-access-its-elements-using-key-values)
- [Objective 7: Write a program to take input and print multiplication table.](#objective-7-write-a-program-to-take-input-and-print-multiplication-table)
- [Objective 8: Write a program to generate the following pattern](#objective-8-write-a-program-to-generate-the-following-pattern)
- [Objective 9: Write a program to print simple interest.](#objective-9-write-a-program-to-print-simple-interest)
- [Objective 10: Write a program to print compound interest.](#objective-10-write-a-program-to-print-compound-interest)
- [Objective 11: Write a program to check whether a number is prime or not.](#objective-11-write-a-program-to-check-whether-a-number-is-prime-or-not)
- [Objective 12: Write a program to check whether a person is eligible for voting or not.](#objective-12-write-a-program-to-check-whether-a-person-is-eligible-for-voting-or-not)
- [Objective 13: Write a program to check whether a number is even or odd.](#objective-13-write-a-program-to-check-whether-a-number-is-even-or-odd)
- [Objective 14: Write a program to create two lists and add them & print the final one.](#objective-14-write-a-program-to-create-two-lists-and-add-them--print-the-final-one)
- [Objective 15: Write a program to add natural numbers upto 10.](#objective-15-write-a-program-to-add-natural-numbers-upto-10)

#### Objective 1: Write a program to print average of five subjects.



```python
Marks = [39, 39, 34, 36, 32]


# Method 1: we need to create a function for dry code
def avg(subjects: list):
    return sum(subjects) / len(subjects)


print(avg(Marks))

# Method 2: We need to loop over the list and add them
FinalValue = 0
for i in Marks:
    FinalValue += i
print(FinalValue / len(Marks))

```

    36.0
    36.0
    

#### Objective 2: Write program to find area of a circle.



```python
radius = float(input("Enter the radius of the circle: "))
# Method 1: Use pi from math module
import math

print("The area of the circle is: ", math.pi * radius**2, " units squared.") # The value can be rounded off.

# Method 2: Define 22/7 as pi
pi = 22 / 7
print("The area of the circle is: ", pi * radius**2, " units squared.")

```

    Enter the radius of the circle: 14
    The area of the circle is:  615.7521601035994  units squared.
    The area of the circle is:  616.0  units squared.
    

#### Objective 3: Write a program to find larger among three numbers.



```python
ListOfNum = [56, 73, 89]
# Method 1: Use max function
print(max(ListOfNum))
# Method 2: Use sorted and refer last index
print(sorted(ListOfNum)[-1])

# Method 3: (Not recommended)
# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the largest number among the three
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Displaying the largest number
print("The largest number among the given inputs is ", largest)

```

    89
    89
    Enter the first number: 56
    Enter the second number: 73
    Enter the third number: 89
    The largest number among the given inputs is  89.0
    

#### Objective 4: Write a program to create a list and sort the elements in descending order.



```python
Array = [344, 29, 330, 339, 6839, 69]


# With function
def reverse_sort(array: list):
    return list(reversed(sorted(array)))


print(reverse_sort(Array))
# With lambda
rev_sort = lambda array: list(reversed(sorted(array)))
print(rev_sort(Array))

```

    [6839, 344, 339, 330, 69, 29]
    [6839, 344, 339, 330, 69, 29]
    

#### Objective 5: Write a program to concatenate two strings.



```python
# Use + operator
print("The speed of light is " + "299,792,458 meters per second.")

```

    The speed of light is 299,792,458 meters per second.
    

#### Objective 6: Write a program to create dictionary and access its elements using key values.



```python
# StudentsData is a dictionary whereas keys are the names of students and values are other information
StudentsData = {
    "Adarsh": "Least popularly known Napoleon",
    "Aryanshu": {"passed": False},
    "Thomas": {"mad_person": True},
    "Light": 299792458,
}
# Can be accessed by indexing
print(StudentsData["Adarsh"])
print(StudentsData["Aryanshu"]["passed"])

# Can be accessed by get method
print(StudentsData.get("Light"))

```

    Least popularly known Napoleon
    False
    299792458
    

#### Objective 7: Write a program to take input and print multiplication table.



```python
# Take input
number_to_multiply = int(input("Enter your number: "))
for i in range(1, 11):
    print(number_to_multiply, " × ", i, " = ", number_to_multiply * i)

```

    Enter your number: 43
    43  ×  1  =  43
    43  ×  2  =  86
    43  ×  3  =  129
    43  ×  4  =  172
    43  ×  5  =  215
    43  ×  6  =  258
    43  ×  7  =  301
    43  ×  8  =  344
    43  ×  9  =  387
    43  ×  10  =  430
    

#### Objective 8: Write a program to generate the following pattern

```
*
**
***
```



```python
# Use for loop
for i in range(1, 4):
    print("*" * i)

```

    *
    **
    ***
    

#### Objective 9: Write a program to print simple interest.



```python
Principal = int(input("Enter your principal amount: "))
Rate = int(input("Enter your rate (omit % sign): "))
Time = int(input("Enter your time (in years): "))
print("S.I is $", Principal * Rate * Time / 100)

```

    Enter your principal amount: 10000
    Enter your rate (omit % sign): 14
    Enter your time (in years): 5
    S.I is $ 7000.0
    

#### Objective 10: Write a program to print compound interest.



```python
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period (in years): "))

compoundInterest = principal * (1 + rate / 100) ** time - principal

# print the compound interest rounded to 2 decimal places
print(f"The compound interest is: ${compoundInterest}")
# Round it off
print(f"The compound interest is: ${round(compoundInterest,2)}")

```

    Enter the principal amount: 10000
    Enter the rate of interest: 14
    Enter the time period (in years): 5
    The compound interest is: $9254.14582400001
    The compound interest is: $9254.15
    

#### Objective 11: Write a program to check whether a number is prime or not.



```python
# define a function because DRY code is the best principle. 
def isPrime(number: int):
    if number <= 1:
        return False

    for i in range(2, int(number**1/2)+1):  # Check Factor
        if number % i == 0:
            return False
        
    return True

print(isPrime(int(input("Enter your number: "))))

```

    Enter your number: 24
    False
    

#### Objective 12: Write a program to check whether a person is eligible for voting or not.



```python
# Let's start with a function that takes age
def isEligibleForVote(age:int):
    if age >= 18:
        return True
    else:
        return False

print(isEligibleForVote(int(input('Enter your age: '))))
```

    Enter your age: 18
    True
    

#### Objective 13: Write a program to check whether a number is even or odd.



```python
def checkNumber(number:int):
    if number%2 == 0:
        return "Number you provided is Even"
    else:
        return "Number you provided is Odd"

print(checkNumber(int(input("Enter your number: "))))
```

    Enter your number: 88
    Number you provided is Even
    

#### Objective 14: Write a program to create two lists and add them & print the final one.



```python
List1 = [1,3,5,7,9]
List2 = [0,2,4,6,8]

# Method 1: Use + operator
print(List1+List2)

#Method 2: Use extend method to append new elements
List1.extend(List2)
print(List1)
```

    [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    

#### Objective 15: Write a program to add natural numbers upto 10.



```python
# One Liner
print(sum([i for i in range(1,11)]))
# sum() is an universal function.

# Another Technique
SumList = []
total =0
for i in range(1,11): # 1 is not required really but added.
    SumList.append(i)
for number in SumList:
    total += number
print(total)

# Yet Another Technique
SumListYet = []
for i in range(1,11): # 1 is not required really but added.
    SumListYet.append(i)

print(sum(SumListYet))
```

    55
    55
    55
    
