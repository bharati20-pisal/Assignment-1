'1. Write a Python program to reverse a number without converting it into a string.'
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)

'2. Write a program to check whether a number is a palindrome.'
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")

'3. Write a program to check whether a number is an Armstrong number.'
num = int(input("Enter a number: "))
original = num
digits = len(str(num))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10
if original == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

'4. Write a program to find the factorial of a number using a loop.'
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial =", fact)

'5. Write a program to generate the Fibonacci series up to N terms.'
n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

'6. Write a program to check whether a number is prime.'

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")

'7. Write a program to print all prime numbers between 1 and 100.'

print("Prime numbers between 1 and 100 are:")

for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

'8. Write a program to find the GCD and LCM of two numbers.'

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while b != 0:
    temp = b
    b = a % b
    a = temp

gcd = a
lcm = (x * y) // gcd

print("GCD =", gcd)
print("LCM =", lcm)


'9. Write a program to reverse a string without using slicing.'

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)


'10. Write a program to check whether a string is a palindrome.'

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome string")
else:
    print("Not a palindrome string")


'11. Write a program to count vowels, consonants, digits and special characters in a string.'

text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

    elif ch.isdigit():
        digits += 1

    elif not ch.isspace():
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)


'12. Write a program to find the frequency of each character in a string.'

text = input("Enter a string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:")

for ch, count in freq.items():
    print(ch, "=", count)


'13. Write a program to find the first non-repeating character in a string.'

text = input("Enter a string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")


'14. Write a program to remove duplicate characters from a string.'

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result = result + ch

print("String after removing duplicates:", result)


'15. Write a program to check whether two strings are anagrams.'

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")

'16. Write a program to find the longest word in a sentence.'

sentence = input("Enter a sentence: ")

words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
print("Length:", len(longest))


'17. Find the second-largest element in a list without using sort().'

numbers = [10, 20, 5, 8, 15]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("Second largest element does not exist")
else:
    print("Second largest element:", second_largest)

'18. Remove duplicate elements from a list without using set().'

numbers = [1, 2, 2, 3, 4, 4, 5]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List after removing duplicates:", result)


'19. Find the common elements between two lists.'

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for num in list1:
    if num in list2:
        if num not in common:
            common.append(num)

print("Common elements:", common)


'20. Move all zeros to the end of a list without changing the order of other elements.'

numbers = [0, 1, 0, 3, 12]

result = []

for num in numbers:
    if num != 0:
        result.append(num)

for num in numbers:
    if num == 0:
        result.append(num)

print("List after moving zeros:", result)


'21. Find the missing number in a list containing numbers from 1 to N.'

numbers = [1, 2, 4, 5, 6]

n = 6

total = n * (n + 1) // 2

missing = total - sum(numbers)

print("Missing number:", missing)


'22. Find the maximum difference between two elements where the larger element appears after the smaller element.'

numbers = [2, 3, 10, 6, 4, 8, 1]

min_element = numbers[0]
max_diff = numbers[1] - numbers[0]

for i in range(1, len(numbers)):
    diff = numbers[i] - min_element

    if diff > max_diff:
        max_diff = diff

    if numbers[i] < min_element:
        min_element = numbers[i]

print("Maximum difference:", max_diff)

'23. Rotate a list to the right by K positions.'

numbers = [1, 2, 3, 4, 5]

k = 2

n = len(numbers)

k = k % n

rotated = numbers[n-k:] + numbers[:n-k]

print("Rotated list:", rotated)

'24. Find all pairs in a list whose sum equals a given target.'

numbers = [2, 4, 3, 5, 7, 8, 1]

target = 9

print("Pairs whose sum equals", target, ":")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])

'25. Write a program to count the frequency of each word in a paragraph.'

paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word frequency:")

for word, count in freq.items():
    print(word, "=", count)

'26. Write a program to merge two dictionaries. If a key exists in both, add their values.'

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 40}

result = dict1.copy()

for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print("Merged dictionary:", result)

'27. Write a program to sort a dictionary based on its values.'

my_dict = {'a': 30, 'b': 10, 'c': 20}

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print("Sorted dictionary:", sorted_dict)

'28. Given a list of student dictionaries containing name and marks, find the student with the highest marks.'

students = [
    {'name': 'Amit', 'marks': 85},
    {'name': 'Rahul', 'marks': 92},
    {'name': 'Priya', 'marks': 78},
    {'name': 'Sneha', 'marks': 95}
]

highest = students[0]

for student in students:
    if student['marks'] > highest['marks']:
        highest = student

print("Student with highest marks:", highest['name'])
print("Highest marks:", highest['marks'])

'29. Group words from a list based on their first character using a dictionary.'

words = ["apple", "ant", "banana", "ball", "cat", "car", "dog"]

groups = {}

for word in words:
    first_char = word[0]

    if first_char not in groups:
        groups[first_char] = []

    groups[first_char].append(word)

print(groups)

'30. Convert two lists into a dictionary, where the first list contains keys and the second contains values.'

keys = ["name", "age", "city"]
values = ["Rahul", 21, "Pune"]

result = dict(zip(keys, values))

print(result)

'31. Write a recursive function to calculate the factorial of a number.'

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = 5

result = factorial(num)

print("Factorial of", num, "is:", result)

'32. Write a recursive function to find the sum of digits of a number.'

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)


num = 1234

result = sum_of_digits(num)

print("Sum of digits:", result)

'33. Implement your own map() function without using Pythons built-in map().'

def my_map(function, items):
    result = []

    for item in items:
        result.append(function(item))

    return result


def square(n):
    return n * n


numbers = [1, 2, 3, 4, 5]

output = my_map(square, numbers)

print("Original List:", numbers)
print("Squared List:", output)

'34. Implement a function that accepts a list and returns a new list containing only even numbers.'

def even_numbers(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

output = even_numbers(my_list)

print("Original List:", my_list)
print("Even Numbers:", output)

'35. Write a function to flatten a nested list.'

def flatten_list(nested):
    result = []

    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


my_list = [[1, 2], [3, [4, 5]], [6, 7]]

output = flatten_list(my_list)

print("Original List:", my_list)
print("Flattened List:", output)


'''36. Student Management System

Create a console-based application with the following operations:
- Add student
- Display all students
- Search student by ID
- Update student details
- Delete student'''


students = []

def add_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    marks = input("Enter Student Marks: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def display_students():
    if not students:
        print("No student records found.")
    else:
        print("\n--- Student Records ---")
        for student in students:
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            print("-------------------")


def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("Student Found!")
            print(student)
            return

    print("Student not found!")


def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["marks"] = input("Enter New Marks: ")

            print("Student details updated successfully!")
            return

    print("Student not found!")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")



'''37. Bank Account Management

Create a bank account program with:
- Create account
- Deposit money
- Withdraw money
- Check balance
- Display account details'''


account = {}

def create_account():
    account["name"] = input("Enter Account Holder Name: ")
    account["number"] = input("Enter Account Number: ")
    account["balance"] = float(input("Enter Initial Deposit: "))

    print("Account created successfully!")


def deposit_money():
    if not account:
        print("Please create an account first.")
        return

    amount = float(input("Enter Deposit Amount: "))

    if amount > 0:
        account["balance"] += amount
        print("Money deposited successfully!")
    else:
        print("Enter a valid amount.")


def withdraw_money():
    if not account:
        print("Please create an account first.")
        return

    amount = float(input("Enter Withdrawal Amount: "))

    if amount <= 0:
        print("Enter a valid amount.")
    elif amount <= account["balance"]:
        account["balance"] -= amount
        print("Money withdrawn successfully!")
    else:
        print("Insufficient balance!")


def check_balance():
    if not account:
        print("Please create an account first.")
    else:
        print("Available Balance:", account["balance"])


def display_details():
    if not account:
        print("Please create an account first.")
    else:
        print("\n--- Account Details ---")
        print("Account Holder:", account["name"])
        print("Account Number:", account["number"])
        print("Balance:", account["balance"])


while True:
    print("\n===== BANK ACCOUNT MANAGEMENT =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if account:
            print("Account already exists!")
        else:
            create_account()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        check_balance()

    elif choice == "5":
        display_details()

    elif choice == "6":
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice! Please try again.")


'''38. Employee Salary Management

Create a program to:
- Add employee details
- Calculate gross salary
- Calculate deductions
- Calculate net salary
- Display employee salary details'''


employees = []

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")

    basic = float(input("Enter Basic Salary: "))
    hra = float(input("Enter HRA: "))
    da = float(input("Enter DA: "))
    bonus = float(input("Enter Bonus: "))

    pf = float(input("Enter PF Deduction: "))
    tax = float(input("Enter Tax Deduction: "))

    gross_salary = basic + hra + da + bonus
    deductions = pf + tax
    net_salary = gross_salary - deductions

    employee = {
        "id": emp_id,
        "name": name,
        "basic": basic,
        "hra": hra,
        "da": da,
        "bonus": bonus,
        "gross": gross_salary,
        "deductions": deductions,
        "net": net_salary
    }

    employees.append(employee)

    print("Employee added successfully!")


def display_salary():
    if not employees:
        print("No employee records found.")
        return

    for emp in employees:
        print("\n===== EMPLOYEE SALARY DETAILS =====")
        print("Employee ID:", emp["id"])
        print("Employee Name:", emp["name"])
        print("Basic Salary:", emp["basic"])
        print("HRA:", emp["hra"])
        print("DA:", emp["da"])
        print("Bonus:", emp["bonus"])
        print("Gross Salary:", emp["gross"])
        print("Total Deductions:", emp["deductions"])
        print("Net Salary:", emp["net"])


while True:
    print("\n===== EMPLOYEE SALARY MANAGEMENT =====")
    print("1. Add Employee Details")
    print("2. Calculate and Display Salary")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_salary()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")


'''39. Library Management System

Create a program to:
- Add books
- Display available books
- Issue a book
- Return a book
- Search books by title'''


books = []

def add_book():
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists!")
            return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    print("Book added successfully!")


def display_books():
    if not books:
        print("No books found.")
        return

    print("\n--- Available Books ---")

    found = False

    for book in books:
        if book["status"] == "Available":
            print("Book ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("-------------------")
            found = True

    if not found:
        print("No available books.")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
            return

    print("Book not found!")


def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                book["status"] = "Available"
                print("Book returned successfully!")
            else:
                print("This book was not issued.")
            return

    print("Book not found!")


def search_book():
    title = input("Enter Book Title to search: ").strip().lower()

    for book in books:
        if book["title"].lower() == title:
            print("\nBook Found!")
            print("Book ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            return

    print("Book not found!")


while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Available Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        search_book()

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")


'''40. Task Management Application

Create a console-based task manager with:
- Add task
- View all tasks
- Update task
- Delete task
- Mark task as completed
- Filter completed and pending tasks'''


tasks = []

def add_task():
    task_id = input("Enter Task ID: ")

    for task in tasks:
        if task["id"] == task_id:
            print("Task ID already exists!")
            return

    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")

    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "status": "Pending"
    }

    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- All Tasks ---")

    for task in tasks:
        print("Task ID:", task["id"])
        print("Title:", task["title"])
        print("Description:", task["description"])
        print("Status:", task["status"])
        print("-------------------")


def update_task():
    task_id = input("Enter Task ID to update: ")

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = input("Enter New Title: ")
            task["description"] = input("Enter New Description: ")

            print("Task updated successfully!")
            return

    print("Task not found!")


def delete_task():
    task_id = input("Enter Task ID to delete: ")

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return

    print("Task not found!")


def mark_completed():
    task_id = input("Enter Task ID to mark as completed: ")

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            print("Task marked as completed!")
            return

    print("Task not found!")


def filter_tasks():
    print("\n1. Completed Tasks")
    print("2. Pending Tasks")

    choice = input("Enter your choice: ")

    if choice == "1":
        status = "Completed"
    elif choice == "2":
        status = "Pending"
    else:
        print("Invalid choice!")
        return

    found = False

    print("\n---", status, "Tasks ---")

    for task in tasks:
        if task["status"] == status:
            print("Task ID:", task["id"])
            print("Title:", task["title"])
            print("Description:", task["description"])
            print("Status:", task["status"])
            print("-------------------")
            found = True

    if not found:
        print("No", status.lower(), "tasks found.")


while True:
    print("\n===== TASK MANAGEMENT SYSTEM =====")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Filter Tasks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        mark_completed()

    elif choice == "6":
        filter_tasks()

    elif choice == "7":
        print("Thank you for using Task Management System!")
        break

    else:
        print("Invalid choice! Please try again.")










