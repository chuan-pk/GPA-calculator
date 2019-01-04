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

def grade_to_number(letter):
    grades = {
        "A": 4, "B+": 3.5, "B": 3, "C+": 2.5, "C": 2, "D+": 1.5, "D": 1, "F": 0,
    }
    return grades[letter]

def calculate_GPA(subjects):
    sumproduct = 0
    sumcredit = 0
    for subject in subjects:
        sumcredit += subject.credit
        sumproduct += subject.credit * grade_to_number(subject.grade)
    return str(sumproduct / sumcredit)[:4]

def filter_subjects(subjects, term):
    this_term_subjects = []
    for subject in subjects:
        if subject.term == term:
            this_term_subjects.append(subject)
    return this_term_subjects

def calculator_mode(subjects):
    print("--- calculator mode ----")
    term = str(input("Enter term: "))
    GPA = calculate_GPA(filter_subjects(subjects, term))
    return GPA

while True:
    subjects = read_csv('grade.csv')
    print_subjects(subjects)
    mode = input("1: for edit mode, 2: for GPA calculator mode>> ")
    if mode == "1":
        print("Edit mode")
        # call function for CRUD and write file then start loop again
        break
    elif mode == "2":
        GPA = calculator_mode(subjects)
        print("GPA: {}".format(GPA))
        break
    else:
        print("Error")
        break
