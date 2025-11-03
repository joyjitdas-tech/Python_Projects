class Classroom:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = []
            print(f"{name} added to the class!")
        else:
            print(f"{name} already exists!")

    def remove_student(self, name):
        if name in self.students:
            del self.students[name]
            print(f"{name} removed from the class.")
        else:
            print(f"{name} not found!")

    def mark_attendance(self, name):
        if name in self.students:
            self.students[name].append("Present")
            print(f"Attendance marked for {name}")
        else:
            print(f"{name} not found!")

    def show_students(self):
        if not self.students:
            print("\n No students in the class yet!")
        else:
            print("\n Classroom Students:")
            for name, record in self.students.items():
                print(f"- {name}: {len(record)} days present")

    def view_attendance(self, name):
        if name in self.students:
            record = self.students[name]
            print(f"\n{name}'s Attendance Record: {record}")
        else:
            print(f"{name} not found!")

    def clear_attendance(self, name):
        if name in self.students:
            self.students[name].clear()
            print(f"Cleared attendance for {name}")
        else:
            print(f"{name} not found!")

    def total_students(self):
        print(f"\n Total Students: {len(self.students)}")

# --- Menu ---
room = Classroom()

while True:
    print("\n====== Classroom App ======")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Mark Attendance")
    print("4. Show All Students")
    print("5. View Individual Attendance")
    print("6. Clear Attendance for a Student")
    print("7. Total Students Count")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        room.add_student(input("Enter student name: "))
    elif choice == '2':
        room.remove_student(input("Enter student name: "))
    elif choice == '3':
        room.mark_attendance(input("Enter student name: "))
    elif choice == '4':
        room.show_students()
    elif choice == '5':
        room.view_attendance(input("Enter student name: "))
    elif choice == '6':
        room.clear_attendance(input("Enter student name: "))
    elif choice == '7':
        room.total_students()
    elif choice == '8':
        print("Goodbye! (Data will be lost after exit)")
        break
    else:
        print(" Invalid choice, please try again.")

