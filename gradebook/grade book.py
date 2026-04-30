grade_book = {}

def add_student(name,):
    if name not in grade_book:
        grade_book [name] = []
        print(f"student '{name} added to the list")
    grade_book[name]= []
    print(f"added {name}")

def add_grade(name, grade):
    grade_book[name].append(grade)
    print(f"grade added, grade is now {grade} for {name}")


def show_grade_book():

    print("\n--- curent gradebook ---")
    if not grade_book:
        print(f"grade book is empty")
    else:
        for name,grade in grade_book.items():
            print(f"{name}: {grade}")
print("----------------------------------------")
