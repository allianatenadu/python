print("Enter a list of numbers, type 0 when finished.")

numbers = []
digits = -1

while digits != 0:  
    digits = int(input("Enter number: "))

    if digits != 0:  
        numbers.append(digits)


total_sum = 0

for digits in numbers:
    total_sum += digits

print(f"The sum is: {total_sum}")


#if len(numbers) > 0:
average = total_sum / len(numbers)
#else:
   # average = 0

print(f"The average is: {average:.2f}")


if len(numbers) > 0:
    largest_number = max(numbers)
else:
    largest_number = None

print(f"The largest number is: {largest_number}")

smallest_so_far = 999999

for digits in numbers:
    if digits > 0 and digits < smallest_so_far:
        smallest_so_far = digits

print(f"The smallest postive number is: {smallest_so_far}")

sorted_list = sorted(numbers)

print("The sorted list is:")
for digits in sorted_list:
  print(digits)

