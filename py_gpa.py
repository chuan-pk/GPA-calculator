import csv

class Subject:
    def __init__(self, term, title, credit, grade):
        self.term = term
        self.title = title
        self.credit = int(credit)
        self.grade = grade

def read_csv(file):
    with open(file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        subjects = []
        for row in reader:
            subject = Subject(row["term"], row["subject"], row["credit"], row["grade"])
            subjects.append(subject)

    return subjects

def print_subjects(subjects):
    print("{:8} {:40} {:8} {:8}".format("term", "subject", "credit", "grade"))
    for subject in subjects:
        print("{:8} {:40} {:8} {:8}".format(subject.term, subject.title, str(subject.credit), subject.grade))

while True:
    subjects = read_csv('grade.csv')
    print_subjects(subjects)
    mode = input("1: for edit mode, 2: for GPA calculator mode>> ")
    if mode == "1":
        print("Edit mode")
        # call function for CRUD and write file then start loop again
        break
    elif mode == "2":
        print("calculator mode")
        # call function for calculate grade
        break
    else:
        print("Error")
        break
