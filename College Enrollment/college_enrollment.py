import getpass

# 🔐 Admin Login Credentials
admin_id = "collegeadmin"
admin_password = "college@123"

# Login Screen
print("=" * 60)
print("College Enrollment System - Admin Login".center(60))
print("=" * 60)

entered_id = input("Enter Admin ID: ").strip()
entered_pass = getpass.getpass("Enter Password: ").strip()

if entered_id != admin_id or entered_pass != admin_password:
    print("❌ Invalid credentials. Access denied.")
    exit()
else:
    print("✅ Login successful. Welcome Admin!")

# 🧠 Student Database: { roll_no: {name: str, courses: [list]} }
student_db = {}

# 📋 Menu Display
def show_menu():
    print("\n=== College Enrollment System Menu ===")
    print("1. Enroll New Student")
    print("2. Assign Courses to Student")
    print("3. View All Students")
    print("4. View Specific Student Details")
    print("5. Exit")

# 🌟 Main App Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        print("\n🧾 Enroll New Student")
        roll_no = input("Enter Roll Number: ").strip()
        if roll_no in student_db:
            print("⚠️ Student already enrolled.")
        else:
            name = input("Enter Student Name: ").strip().title()
            student_db[roll_no] = {"name": name, "courses": []}
            print(f"✅ Student {name} enrolled successfully.")

    elif choice == '2':
        print("\n📚 Assign Courses")
        roll_no = input("Enter Roll Number: ").strip()
        if roll_no not in student_db:
            print("⚠️ Student not found. Please enroll first.")
        else:
            course_list = input("Enter courses (comma-separated): ").strip().title().split(",")
            cleaned_courses = [course.strip() for course in course_list]
            student_db[roll_no]["courses"].extend(cleaned_courses)
            print(f"✅ Courses assigned to {student_db[roll_no]['name']}.")

    elif choice == '3':
        print("\n📋 All Enrolled Students")
        if not student_db:
            print("No students enrolled yet.")
        else:
            print("-" * 60)
            print(f"{'Roll No':<15}{'Name':<25}{'Courses Enrolled'}")
            print("-" * 60)
            for roll, data in student_db.items():
                courses = ", ".join(data['courses']) if data['courses'] else "None"
                print(f"{roll:<15}{data['name']:<25}{courses}")
            print("-" * 60)

    elif choice == '4':
        print("\n🔍 View Student Details")
        roll_no = input("Enter Roll Number: ").strip()
        if roll_no not in student_db:
            print("⚠️ Student not found.")
        else:
            data = student_db[roll_no]
            print(f"\nStudent Name   : {data['name']}")
            print(f"Roll Number    : {roll_no}")
            print(f"Courses Enrolled: {', '.join(data['courses']) if data['courses'] else 'None'}")

    elif choice == '5':
        print("👋 Exiting... Thank you!")
        break

    else:
        print("❌ Invalid choice. Please select between 1-5.")
