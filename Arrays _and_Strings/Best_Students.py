"""
Given the below students data, write a python script to return the name of the best student in each subject
"""

students = [
    {"name": "jayboi", "grade": 80, "subject": "maths"},
    {"name": "aliyah", "grade": 90, "subject": "science"},
    {"name": "fareedah", "grade": 87, "subject": "maths"},
    {"name": "jameelah", "grade": 95, "subject": "maths"},
    {"name": "jayboi", "grade": 100, "subject": "science"},
    {"name": "jameelah", "grade": 90, "subject": "science"},
    {"name": "fareedah", "grade": 97, "subject": "science"},
    {"name": "aliyah", "grade": 87, "subject": "maths"}
]

class BestStudent:
    def best_stud(students):
        #create a dictionary
        best_dict={}

        #Loop through the list of dict
        for s in students:
            subject = s["subject"]

            #fill empty dict with subject as keys and student data as values
            if subject not in best_dict.keys():
                best_dict[subject] = s

            else:
                #compare the grade of the current student with the grade of the student in the dict
                if s["grade"] > best_dict[subject]["grade"]:
                    best_dict[subject] = s


        # Return the names of the best students
        return {subject: student["name"] for subject, student in best_dict.items()}
    
#call the function and print the result
best_students = BestStudent.best_stud(students)
print(best_students)