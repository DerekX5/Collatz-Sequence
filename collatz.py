'''
Derek Xu
dxu293@uwo.ca
251287715
This code continuously applies the collatz conjecture to an inputted integer until it reaches 1, creating a list of
numbers. Using said list, the program proceeds to figure out the amount of prime numbers,the amount of even
and odd numbers, the total number of outputs, and the maximum value in the list.
'''

#Prompts user to enter a number
initial_number = int(input("Enter a number:"))

#Sets the counters for variables
even_count = 0
odd_count = 0
total_count = 0
maximum_value = 0

#Checks if input is > 1
if initial_number <= 1:
    print("The value of n must be greater than 1")
    exit()

#Check if numbers are odd/even and applies equations. Updates even/odd number counters and remembers the
#maximum value
collatz = [initial_number]
maximum_value = initial_number
while initial_number > 1:
    if initial_number % 2 == 0:
        initial_number = initial_number // 2
        even_count += 1
        total_count += 1
        collatz.append(initial_number)
    else:
        initial_number = (3 * initial_number) + 1
        odd_count += 1
        total_count += 1
        collatz.append(initial_number)
    if initial_number > maximum_value:
        maximum_value = initial_number

#Checks if last number of list is 1, add to odd counter
if collatz[-1] == 1:
    odd_count += 1
    total_count += 1

#Format all numbers list
output_string_all_numbers = ""
for element in collatz:
    buffer = str(element)
    output_string_all_numbers = output_string_all_numbers + buffer + ","

#Checks list for prime numbers
prime_numbers = []
for x in collatz:
    if x > 1:
        is_prime = True
        for i in range(2, x):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(x)

#Format prime numbers list
output_string_prime_numbers = ""
for element in prime_numbers:
    buffer = str(element)
    output_string_prime_numbers = output_string_prime_numbers + buffer + ","

#Prints out results
print("All numbers:", output_string_all_numbers)
print("Prime numbers encountered:", output_string_prime_numbers)
print("Maximum number:", maximum_value)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Total numbers:", total_count)
