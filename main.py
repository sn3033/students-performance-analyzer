def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    return "F"


def main():
    print("STUDENT PERFORMANCE ANALYZER")
    print("-" * 30)

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    subjects = {}
    for i in range(1, 6):
        subject = input(f"Subject {i} name: ").strip()
        if not subject or subject in subjects:
            print("Subject names must be unique and non-empty.")
            return

        try:
            marks = float(input(f"Marks in {subject} (0-100): "))
            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                return
        except ValueError:
            print("Enter a valid numeric mark.")
            return

        subjects[subject] = marks

    total = sum(subjects.values())
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)

    print("\n--- PERFORMANCE REPORT ---")
    print("Student:", name)
    for subject, marks in subjects.items():
        print(f"{subject}: {marks:g}/100")

    print(f"Total: {total:g}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("Result:", "PASS" if percentage >= 40 else "FAIL")


if __name__ == "__main__":
    main()
