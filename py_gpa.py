import csv

FILENAME = 'grade.csv'

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

def write_csv(file, subjects):
    with open(file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['term', 'subject', 'credit', 'grade'], delimiter=',')
        writer.writeheader()
        for subject in subjects:
            writer.writerow({
                'term': subject.term,
                'subject': subject.title,
                'credit': subject.credit,
                'grade': subject.grade,
            })

def print_subjects(subjects):
    print("-"*70)
    print("{:4}|{:8}|{:40}|{:8}|{:8}".format("ID", "term", "subject", "credit", "grade"))
    print("-"*70)
    for index, subject in enumerate(subjects):
        print("{:4} {:8} {:40} {:8} {:8}".format(str(index), subject.term, subject.title, str(subject.credit), subject.grade))

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
    print("------------ calculator mode ------------")
    term = str(input("term: "))
    GPA = calculate_GPA(filter_subjects(subjects, term))
    return GPA

def edit_mode(subjects):
    print("------------ edit mode ------------")
    mode = str(input("1: edit, 2: add, 3: delete > "))
    if mode == "1":
        print("------ edit ------")
        edit_subject(subjects)
    elif mode == "2":
        print("------ add ------")    
        add_subject(subjects)
    elif mode == "3":
        print("------ delete ------")
        delete_subject(subjects)
    else :
        print("Error")

def subject_form():
    valid_grades = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
    valid_credit = [1, 2, 3]
    term = str(input("term: "))
    subject_title = str(input("title: "))
    credit = int(input("credit: "))
    while not(credit in valid_credit):    
        print("Invalid credit, credit should be {}".format(valid_credit))
        credit = int(input("enter subject credit: "))

    grade = str(input("grade: "))
    while not(grade in valid_grades):
        print("Invalid grade, grade should be {}".format(valid_grades))
        grade = str(input("enter subject grade: "))
    return (term, subject_title, credit, grade)

def add_subject(subjects):
    subject_detail = subject_form()
    subject = Subject(subject_detail[0], subject_detail[1], subject_detail[2], subject_detail[3])
    subjects.append(subject)
    write_csv(FILENAME, subjects)

def delete_subject(subjects):
    index = int(input("subject id: "))
    while  not(index in list(range(0, len(subjects)))):
        print("Invalid index, index should be: 0 to {}".format(len(subjects)-1))
        index = int(input("subject id: "))
    del subjects[index]
    write_csv(FILENAME, subjects)
    
def edit_subject(subjects):
    index = int(input("subject id: "))
    while  not(index in list(range(0, len(subjects)))):
        print("Invalid index, index should be: 0 to {}".format(len(subjects)-1))
        index = int(input("subject id: "))
    subject = subjects[index]
    print("""old details
    term: {}
    title: {}
    credit: {}
    grade: {}""".format(subject.term, subject.title, subject.credit, subject.grade))
    subject_detail = subject_form()
    subject.term = subject_detail[0]
    subject.title = subject_detail[1]
    subject.credit = subject_detail[2]
    subject.grade = subject_detail[3]
    write_csv(FILENAME, subjects)

while True:
    subjects = read_csv(FILENAME)
    print_subjects(subjects)
    mode = input("1: for edit mode, 2: for GPA calculator mode > ")
    if mode == "1":
        edit_mode(subjects)
    elif mode == "2":
        GPA = calculator_mode(subjects)
        print("GPA: {}".format(GPA))
        input("press Enter to continue > ")
    else:
        print("Error")
