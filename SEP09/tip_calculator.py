bill = float(input("Enter your total bill: "))
service = input("How was the service? (good, fair, or bad): ")

if service == "good":
    tip = bill * 0.20
elif service == "fair":
    tip = bill * 0.15
else:
    tip = bill * 0.10

total = bill + tip

print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")