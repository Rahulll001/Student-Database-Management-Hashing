
class StudentDatabase:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, roll_no):
        return roll_no % self.size

    def add_student(self, roll_no, name, marks):
        index = self.hash_function(roll_no)

        for i in range(self.size):
            position = (index + i) % self.size

            if self.table[position] is None:
                self.table[position] = {
                    "roll_no": roll_no,
                    "name": name,
                    "marks": marks
                }
                print("Student added successfully!")
                return

            if self.table[position]["roll_no"] == roll_no:
                print("Roll number already exists!")
                return

        print("Database is full!")

    def search_student(self, roll_no):
        index = self.hash_function(roll_no)

        for i in range(self.size):
            position = (index + i) % self.size
            student = self.table[position]

            if student is None:
                print("Student not found!")
                return

            if student["roll_no"] == roll_no:
                print("\nStudent Found")
                print("Roll Number:", student["roll_no"])
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                return

        print("Student not found!")

    def display_students(self):
        print("\nStudent Database")
        print("-" * 40)

        found = False

        for student in self.table:
            if student is not None:
                found = True
                print(
                    "Roll No:", student["roll_no"],
                    "| Name:", student["name"],
                    "| Marks:", student["marks"]
                )

        if not found:
            print("Database is empty!")


def main():
    db = StudentDatabase()

    while True:
        print("\n===== Student Database Management =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                roll_no = int(input("Enter roll number: "))
                name = input("Enter student name: ").strip()
                marks = float(input("Enter marks: "))

                if roll_no < 0 or not name or not 0 <= marks <= 100:
                    print("Enter valid roll number, name, and marks (0-100).")
                    continue

                db.add_student(roll_no, name, marks)

            except ValueError:
                print("Invalid input! Enter numeric roll number and marks.")

        elif choice == "2":
            try:
                roll_no = int(input("Enter roll number to search: "))
                db.search_student(roll_no)
            except ValueError:
                print("Please enter a valid roll number.")

        elif choice == "3":
            db.display_students()

        elif choice == "4":
            print("Exiting Student Database Management System.")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
