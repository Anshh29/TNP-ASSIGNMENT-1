#File Name: [0157EC231005]
# Name: [Ansh Jain]
# Enrollment: [0157EC231005]
# Batch: [6 (MTF)]
# Batch Time: [12:10]
 
# Conditional statement:
 
# Basic If–Else Problems:
 
# Q1. Write a program to check whether a number is positive, negative, or zero.
# Solution
num = float(input("Enter a number: "))
if num > 0:
   print("Positive")
elif num < 0:
   print("Negative")
else:
   print("Zero")
 
# Q2. Write a program to check whether a number is even or odd.
# Solution
num = int(input("Enter a number: "))
if num % 2 == 0:
   print("Even")
else:
   print("Odd")
 
# Q3. Write a program to check if a given year is a leap year or not.
# Solution
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
   print("Leap year")
else:
   print("Not a leap year")
 
# Q4. Write a program to find the greatest of two numbers.
# Solution
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
   print(f"{a} is greater")
elif b > a:
   print(f"{b} is greater")
else:
   print("Both are equal")
 
# Q5. Write a program to check whether a person is eligible to vote (age >= 18).
# Solution
age = int(input("Enter age: "))
if age >= 18:
   print("Eligible to vote")
else:
   print("Not eligible to vote")
 
# Q6. Write a program to check whether a given character is a vowel or consonant.
# Solution
char = input("Enter a character: ").lower()
if char in 'aeiou':
   print("Vowel")
else:
   print("Consonant")
 
# Q7. Write a program to check if a number is divisible by 5.
# Solution
num = int(input("Enter a number: "))
if num % 5 == 0:
   print("Divisible by 5")
else:
   print("Not divisible by 5")
 
# Q8. Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number.
# Solution
num = int(input("Enter a number: "))
if 0 <= num < 10:
   print("Single-digit")
elif 10 <= num < 100:
   print("Two-digit")
else:
   print("More than two-digit")
 
# Q9. Write a program to check whether a student has passed or failed (passing marks = 40).
# Solution
marks = float(input("Enter marks: "))
if marks >= 40:
   print("Passed")
else:
   print("Failed")
 
# Q10. Write a program to find whether the entered number is a multiple of both 3 and 7.
# Solution
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
   print("Multiple of both 3 and 7")
else:
   print("Not a multiple of both 3 and 7")
 
# Ladder If & Nested If:
 
# Q1. Write a program to find the greatest among three numbers.
# Solution
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a > b and a > c:
   print(f"{a} is greatest")
elif b > c:
   print(f"{b} is greatest")
else:
   print(f"{c} is greatest")
 
# Q2. Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).
# Solution
age = int(input("Enter age: "))
if age < 13:
   print("Child")
elif 13 <= age <= 19:
   print("Teenager")
elif 20 <= age <= 59:
   print("Adult")
else:
   print("Senior")
 
# Q3. Write a program to assign grades based on marks: 90-100: A, 75-89: B, 50-74: C, 35-49: D, <35: Fail.
# Solution
marks = float(input("Enter marks: "))
if 90 <= marks <= 100:
   print("A")
elif 75 <= marks <= 89:
   print("B")
elif 50 <= marks <= 74:
   print("C")
elif 35 <= marks <= 49:
   print("D")
else:
   print("Fail")
 
# Q4. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.
# Solution
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a == b == c:
   print("Equilateral")
elif a == b or b == c or a == c:
   print("Isosceles")
else:
   print("Scalene")
 
# Q5. Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
# Solution
char = input("Enter a character: ")
if char.isupper():
   print("Uppercase")
elif char.islower():
   print("Lowercase")
elif char.isdigit():
   print("Digit")
else:
   print("Special symbol")
 
# Q6. Write a program to calculate electricity bill based on units: Up to 100 units: ₹5 per unit, 101–200 units: ₹7 per unit, Above 200 units: ₹10 per unit.
# Solution
units = float(input("Enter units: "))
if units <= 100:
   bill = units * 5
elif units <= 200:
   bill = 100 * 5 + (units - 100) * 7
else:
   bill = 100 * 5 + 100 * 7 + (units - 200) * 10
print(f"Bill: ₹{bill}")
 
# Q7. Write a program to determine the largest of four numbers using nested if.
# Solution
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))
if a > b:
   if a > c:
       if a > d:
           print(f"{a} is largest")
       else:
           print(f"{d} is largest")
   else:
       if c > d:
           print(f"{c} is largest")
       else:
           print(f"{d} is largest")
else:
   if b > c:
       if b > d:
           print(f"{b} is largest")
       else:
           print(f"{d} is largest")
   else:
       if c > d:
           print(f"{c} is largest")
       else:
           print(f"{d} is largest")
 
# Q8. Write a program to check if a given year is a century year and also a leap year.
# Solution
year = int(input("Enter year: "))
if year % 100 == 0:
   if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
       print("Century leap year")
   else:
       print("Century year but not leap")
else:
   print("Not a century year")
 
# Q9. Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).
# Solution
bmi = float(input("Enter BMI: "))
if bmi < 18.5:
   print("Underweight")
elif 18.5 <= bmi <= 24.9:
   print("Normal")
elif 25 <= bmi <= 29.9:
   print("Overweight")
else:
   print("Obese")
 
# Q10. Write a program to display the smallest number among three using nested if.
# Solution
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a < b:
   if a < c:
       print(f"{a} is smallest")
   else:
       print(f"{c} is smallest")
else:
   if b < c:
       print(f"{b} is smallest")
   else:
       print(f"{c} is smallest")
 
# Loops:
 
# For Loop Problems:
 
# Q1. Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number: sum of cubes of digits equals the number itself. Example: 153 => 1^3+5^3+3^3 = 153).
# Solution
for num in range(100, 1000):
   sum_cubes = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum_cubes += digit ** 3
       temp //= 10
   if sum_cubes == num:
       print(num)
 
# Q2. Write a program to generate and display the first n prime numbers using a for loop.
# Solution
n = int(input("Enter n: "))
count = 0
num = 2
while count < n:
   is_prime = True
   for i in range(2, int(num**0.5) + 1):
       if num % i == 0:
           is_prime = False
           break
   if is_prime:
       print(num)
       count += 1
   num += 1
 
# Q3. Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.
# Solution
for num in range(1, 501):
   if num % 3 == 0:
       sum_digits = 0
       temp = num
       while temp > 0:
           sum_digits += temp % 10
           temp //= 10
       if sum_digits <= 10:
           print(num)
 
# Q4. Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4: * *** ***** *******
# Solution
n = int(input("Enter n: "))
for i in range(1, n+1):
   print('*' * (2*i - 1))
 
# Q5. Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once) using a for loop.
# Solution
string = input("Enter string: ").lower()
alphabets = set()
for char in string:
   if char.isalpha():
       alphabets.add(char)
if len(alphabets) == 26:
   print("Pangram")
else:
   print("Not a pangram")
 
# Q6. Write a program using a for loop to print all twin primes between 1 and 100. (Twin primes: pairs of prime numbers with a difference of 2, e.g., (3,5), (11,13)).
# Solution
def is_prime(num):
   if num < 2:
       return False
   for i in range(2, int(num**0.5) + 1):
       if num % i == 0:
           return False
   return True
 
for num in range(2, 99):
   if is_prime(num) and is_prime(num + 2):
       print(f"({num}, {num+2})")
 
# Q7. Write a program that accepts a number from the user and prints whether it is a Harshad number (number divisible by the sum of its digits) using a for loop.
# Solution
num = int(input("Enter number: "))
sum_digits = 0
temp = num
while temp > 0:
   sum_digits += temp % 10
   temp //= 10
if num % sum_digits == 0:
   print("Harshad number")
else:
   print("Not a Harshad number")
 
# Q8. Write a program to generate Pascal’s Triangle up to n rows using a for loop.
# Solution
n = int(input("Enter n: "))
for i in range(n):
   row = [1]
   for j in range(1, i+1):
       row.append(row[j-1] * (i - j + 1) // j)
   print(' '.join(map(str, row)))
 
# Q9. Write a program using a for loop to display the sum of the series: 1^2 + 2^2 + 3^2 + ... + n^2
# Solution
n = int(input("Enter n: "))
sum_series = 0
for i in range(1, n+1):
   sum_series += i**2
print(f"Sum: {sum_series}")
 
# Q10. Write a program that accepts a number from the user and prints whether it is a Strong number (sum of factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145.
# Solution
import math
num = int(input("Enter number: "))
sum_fact = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum_fact += math.factorial(digit)
   temp //= 10
if sum_fact == num:
   print("Strong number")
else:
   print("Not a strong number")
 
# While Loop Problems:
 
# Q11. Write a program using a while loop to find the reverse of a number and check if the reversed number is prime. Example: Input = 73 → Reverse = 37 → Prime.
# Solution
num = int(input("Enter number: "))
rev = 0
temp = num
while temp > 0:
   rev = rev * 10 + temp % 10
   temp //= 10
print(f"Reverse: {rev}")
is_prime = True
if rev < 2:
   is_prime = False
else:
   i = 2
   while i * i <= rev:
       if rev % i == 0:
           is_prime = False
           break
       i += 1
if is_prime:
   print("Reversed number is prime")
else:
   print("Reversed number is not prime")
 
# Q12. Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.
# Solution
total_sum = 0
while total_sum <= 100:
   num = int(input("Enter number: "))
   temp = num
   digit_sum = 0
   while temp > 0:
       digit_sum += temp % 10
       temp //= 10
   total_sum += digit_sum
   print(f"Current total digit sum: {total_sum}")
print("Total digit sum exceeded 100")
 
# Q13. Write a program using a while loop to check whether a number is a Duck number (a number containing zero but not starting with zero, e.g., 202, 1203).
# Solution
num = input("Enter number: ")
is_duck = False
i = 0
while i < len(num):
   if num[i] == '0':
       if i != 0:
           is_duck = True
       break
   i += 1
if is_duck:
   print("Duck number")
else:
   print("Not a duck number")
 
# Q14. Write a program using a while loop to accept a number and check if it is a Happy number. (A number is happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a happy number.
# Solution
num = int(input("Enter number: "))
seen = set()
while num != 1 and num not in seen:
   seen.add(num)
   sum_sq = 0
   while num > 0:
       digit = num % 10
       sum_sq += digit ** 2
       num //= 10
   num = sum_sq
if num == 1:
   print("Happy number")
else:
   print("Not a happy number")
 
# Q15. Write a program using a while loop to find the largest prime factor of a given number.
# Solution
num = int(input("Enter number: "))
factor = 2
largest = 1
while num > 1:
   if num % factor == 0:
       largest = factor
       while num % factor == 0:
           num //= factor
   factor += 1
print(f"Largest prime factor: {largest}")
 
# Q16. Write a program to repeatedly accept a string from the user until the string entered is a palindrome.
# Solution
while True:
   string = input("Enter string: ")
   if string == string[::-1]:
       print("Palindrome entered")
       break
   else:
       print("Not a palindrome, try again")
 
# Q17. Write a program using a while loop to compute the sum of digits of a number until the result becomes a single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2.
# Solution
num = int(input("Enter number: "))
while num >= 10:
   sum_digits = 0
   while num > 0:
       sum_digits += num % 10
       num //= 10
   num = sum_digits
print(f"Digital root: {num}")
 
# Q18. Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even => n/2, if odd => 3n+1. Continue until n=1).
# Solution
num = int(input("Enter number: "))
while num != 1:
   print(num, end=' ')
   if num % 2 == 0:
       num //= 2
   else:
       num = 3 * num + 1
print(1)
 
# Q19. Write a program using a while loop to accept a number and check whether it is a Kaprekar number. (Kaprekar number: if square of the number can be split into two parts whose sum equals the number. Example: 45^2=2025 => 20+25=45).
# Solution
num = int(input("Enter number: "))
sq = num ** 2
sq_str = str(sq)
for i in range(1, len(sq_str)):
   left = int(sq_str[:i])
   right = int(sq_str[i:])
   if left + right == num and right != 0:
       print("Kaprekar number")
       break
else:
   print("Not a Kaprekar number")

   # Q20. Write a program to simulate an ATM machine using a while loop. The program should allow users to check balance, deposit money, withdraw money, and exit.
# Solution
import sys

def atm_simulation():
    """
    Simulates a simple ATM interface where users can check balance,
    deposit, withdraw, or exit using a while loop.
    """
    
    # Initialize starting balance
    balance = 1000.00
    
    print("Welcome to the Python ATM")
    
    while True:
        print("\n--------------------------------")
        print("Please select an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("--------------------------------")
        
        try:
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                # Check Balance
                print(f"\nYour current balance is: ${balance:.2f}")
                
            elif choice == '2':
                # Deposit Money
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    balance += amount
                    print(f"\nSuccessfully deposited ${amount:.2f}")
                    print(f"New balance: ${balance:.2f}")
                else:
                    print("\nError: Deposit amount must be positive.")
                    
            elif choice == '3':
                # Withdraw Money
                amount = float(input("Enter amount to withdraw: $"))
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"\nSuccessfully withdrew ${amount:.2f}")
                        print(f"Remaining balance: ${balance:.2f}")
                    else:
                        print(f"\nError: Insufficient funds. You only have ${balance:.2f}")
                else:
                    print("\nError: Withdrawal amount must be positive.")
                    
            elif choice == '4':
                # Exit
                print("\nThank you for using the Python ATM. Goodbye!")
                break
                
            else:
                print("\nInvalid choice. Please select 1, 2, 3, or 4.")
                
        except ValueError:
            print("\nError: Invalid input. Please enter numeric values for amounts.")

if __name__ == "__main__":
    atm_simulation()