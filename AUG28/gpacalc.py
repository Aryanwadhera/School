def calculate_gpa():
    total_points = 0

    for i in range(1, 6):
        grade = input(f"Enter grade {i}: ").strip().upper()
        points = 69 - ord(grade)
        total_points += points

    gpa = total_points / 5
    print(f"Your GPA is {gpa:.2f}")

if __name__ == "__main__":
    calculate_gpa()