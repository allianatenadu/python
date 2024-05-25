child = float(input("What is the price of a child's meal?"))
adult = float(input("What is the price of an adult's meal?"))
children = int(input("How many children are there?"))
adults = int(input("How many adults are there?"))

# this print gives space between 
print()
sum_1 = child *children
sum_2 = adult *adults 
subtotal = sum_1 + sum_2
print(f"Subtotal: ${subtotal:.2f}")

# this print gives space between
print()
rate = float(input("What is the sales tax rate?"))
sales = rate * subtotal / 100
print(f"Sales Tax: ${sales:.2f}")
total_price = subtotal + sales 
print(f"Total: ${total_price:.2f}")

#this print gives space between
print()
payment = float(input("What is the payment amount?"))
change = payment - total_price
print(f"Change: ${change:.2f}")
