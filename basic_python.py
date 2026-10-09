#1.Check if a number is positive, negative or zero.
num=int(input("Enter a number:"))
if(num>0):
    print("Number is Positive")
elif(num<0):
    print("Number is Negative")
else:
    print("Number is zero")


#2.Check whether a number is even or odd.
    num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

#3. Find the greater of two number.
    num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater")
elif num2 > num1:
    print(f"{num2} is greater")
else:
    print("Both numbers are equal")

#4. Find the greatest of three numbers.
    a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the greatest")
elif b >= a and b >= c:
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")

#5. Check if a person is eligible  to vote (age >=18)
    age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#6. Check whether a year is a leap year.
    year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#7. Check if a character is a vowel or consonant.
    char = input("Enter a single character: ").lower()

if char.isalpha() and len(char) == 1:
    if char in 'aeiou':
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")
else:
    print("Please enter a valid single alphabetical character.")

#8. Check whether a number is divisible by 5 and 11.
    num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11")
else:
    print(f"{num} is not divisible by both 5 and 11")

#9. Check if a number is a multiple of both 3 and 7.
    num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is a multiple of both 3 and 7")
else:
    print(f"{num} is not a multiple of both 3 and 7")

#10. Assign grades based  on marks: a. 90-100:A b.80-89:B c.70-79:C d.60-69:D e.Below 60:F
    marks = float(input("Enter marks (0-100): "))

if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks < 90:
    print("Grade: B")
elif 70 <= marks < 80:
    print("Grade: C")
elif 60 <= marks < 70:
    print("Grade: D")
elif 0 <= marks < 60:
    print("Grade: F")
else:
    print("Invalid marks entered")

#11. Check if a character is uppercase or lowercase.
    char = input("Enter a character: ")

if char.isupper():
    print(f"{char} is an uppercase letter")
elif char.islower():
    print(f"{char} is a lowercase letter")
else:
    print(f"{char} is not an alphabetical letter")

#12. Find whether the entered alphabet is a vowel using if-elif.
    char = input("Enter an alphabet: ").lower()

if char == 'a':
    print("It is a vowel")
elif char == 'e':
    print("It is a vowel")
elif char == 'i':
    print("It is a vowel")
elif char == 'o':
    print("It is a vowel")
elif char == 'u':
    print("It is a vowel")
else:
    print("It is not a vowel")

#13. Check if three sides can form a triangle 
    s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
s3 = float(input("Enter side 3: "))

if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2):
    print("These sides can form a triangle")
else:
    print("These sides cannot form a triangle")

#14. Determine the type of triangle (Equilateral,Isosceles,Scalene)
    s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
s3 = float(input("Enter side 3: "))

if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2):
    if s1 == s2 == s3:
        print("Equilateral Triangle")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")

#15. Find the largest among four numbers.
    n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
n4 = float(input("Enter fourth number: "))

largest = n1
if n2 > largest:
    largest = n2
if n3 > largest:
    largest = n3
if n4 > largest:
    largest = n4

print(f"The largest number is {largest}")

#16. Check a whether a number is a three digit number.
num = int(input("Enter an integer number: "))

if 100 <= abs(num) <= 999:
    print(f"{num} is a three-digit number")
else:
    print(f"{num} is not a three-digit number")

#17. Calculate electricity bill using slab rates.
    units = float(input("Enter units consumed: "))
bill = 0

if units <= 100:
    bill = units * 4  # $4 per unit for first 100 units
elif units <= 300:
    bill = (100 * 4) + ((units - 100) * 6)  # $6 per unit for next 200 units
else:
    bill = (100 * 4) + (200 * 6) + ((units - 300) * 9)  # $9 per unit above 300 units

print(f"Total Electricity Bill: ${bill:.2f}")

#18. Calculate income tax based on income slabs.
income = float(input("Enter your annual income: "))
tax = 0

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + ((income - 500000) * 0.20)
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + ((income - 1000000) * 0.30)

print(f"Total Income Tax Payable: ${tax:.2f}")

#19. Check if a student passes (minimum 35 marks in each subject)
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

if sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")

#20. Find whether a number is within a given range.
    num = float(input("Enter the number to check: "))
lower = float(input("Enter lower limit of range: "))
upper = float(input("Enter upper limit of range: "))

if lower <= num <= upper:
    print(f"{num} is within the range [{lower}, {upper}]")
else:
    print(f"{num} is outside the range")

#21. Build a simple calculator using if-elif-else(+,-,*,/)
n1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
n2 = float(input("Enter second number: "))

if op == '+':
    print(f"Result: {n1 + n2}")
elif op == '-':
    print(f"Result: {n1 - n2}")
elif op == '*':
    print(f"Result: {n1 * n2}")
elif op == '/':
    if n2 != 0:
        print(f"Result: {n1 / n2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")

#22.Check if a year is a century leap year.
year = int(input("Enter a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is a century leap year")
    else:
        print(f"{year} is a century year but not a leap year")
else:
    print(f"{year} is not a century year")

#23. Determine the season based on month number.
month = int(input("Enter month number (1-12): "))

if month in[12,1,2]:
    print("Season: Winter")
elif month in[3,4,5]:
    print("Season: Spring")
elif month in[6,7,8]:
    print("Season: Summer")
elif month in[9,10,11]:
    print("Season: Autumn / Fall")
else:
    print("Invalid month number")

#24. Find the number of days in a month.
month = int(input("Enter month number (1-12): "))

if month in[1,3,5,7,8,10,12]:
    print("31 days")
elif month in[4,6,9,11]:
    print("30 days")
elif month == 2:
    year = int(input("Enter year to check for leap year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29 days (Leap Year)")
    else:
        print("28 days")
else:
    print("Invalid month number")

#25. Check whether a password meets mininum conditions(length,digits, etc.)
password = input("Enter password to evaluate: ")
has_digit = any(char.isdigit() for char in password)

if len(password) >= 8 and has_digit:
    print("Password strength: Valid")
else:
    print("Password invalid. Must be at least 8 characters long and contain at least 1 digit.")
#26. Determine ticket price based on age category.
age = int(input("Enter age: "))

if age < 5:
    print("Ticket Price: Free")
elif age <= 12:
    print("Ticket Price: $5 (Child)")
elif age <= 60:
    print("Ticket Price: $10 (Adult)")
else:
    print("Ticket Price: $7 (Senior Citizen)")

#27. Calculate discount based on purchase amount.
amount = float(input("Enter purchase amount: "))
discount = 0

if amount >= 5000:
    discount = 0.20  # 20% discount
elif amount >= 2000:
    discount = 0.10  # 10% discount
elif amount >= 1000:
    discount = 0.05  # 5% discount

final_price = amount - (amount * discount)
print(f"Discount applied: {discount * 100}%")
print(f"Final payable amount: ${final_price:.2f}")

#28. Check if a person is eligible for a driving license(age and eyesight condition)
age = int(input("Enter age: "))
eyesight = input("Is your eyesight condition pass? (yes/no): ").lower()

if age >= 18 and eyesight == 'yes':
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

#29. Create a login system with username and password validation.
stored_username = "admin"
stored_password = "password123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("Login successful! Welcome.")
else:
    print("Login failed. Invalid credentials.")

#30. Create a menu-driven program using if-elif-else with options like: a. Addition  b. Substraction c.Multiplication d.Division e. Exit.
print("--- Menu ---")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")
print("e. Exit")

choice = input("Enter your choice (a/b/c/d/e): ").lower()

if choice == 'e':
    print("Exiting program. Goodbye!")
elif choice in ['a', 'b', 'c', 'd']:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    
    if choice == 'a':
        print(f"Result: {n1 + n2}")
    elif choice == 'b':
        print(f"Result: {n1 - n2}")
    elif choice == 'c':
        print(f"Result: {n1 * n2}")
    elif choice == 'd':
        if n2 != 0:
            print(f"Result: {n1 / n2}")
        else:
            print("Error: Division by zero")
else:
    print("Invalid option selected")

