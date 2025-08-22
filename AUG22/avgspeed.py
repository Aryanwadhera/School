distance = float(input("Enter the distance traveled in miles or kilometers: "))
time_minutes = float(input("Enter the time taken (in minutes): "))
time_hours = time_minutes / 60
average_speed = distance / time_hours
print(f"The average speed is: {average_speed} units/hour")
