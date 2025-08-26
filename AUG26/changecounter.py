def calculate_change(amount):
    denominations = [
        (25, 'quarter'),
        (10, 'dime'),
        (5, 'nickel'),
        (1, 'penny')
    ]
    
    change = {}
    remaining = int(amount * 100)  
    
    for value, name in denominations:
        if remaining >= value:
            count = remaining // value  
            change[name] = count
            remaining -= count * value
    
    return change

def main():
    amount = float(input("Enter the amount of change to give (in dollars): "))
            
    total_coins = 0
    change = calculate_change(amount)
    
    print("\nChange to give:")
    for coin, count in change.items():
        plural = 's' if count != 1 else ''
        print(f"{count} {coin}{plural}")
        total_coins += count 

    print(f"\nTotal coins used: {total_coins}")

if __name__ == "__main__":
    main()
    