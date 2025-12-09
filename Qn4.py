def get_grade(student_grades, student_name):
    try :
        return student_grades[student_name]
    except Exception:
        return "student not found in the system"

grades= {"abebe":90, "Selam":50 , "Kidus" : 95} 
print (get_grade(grades , "abebe"))
print (get_grade(grades , "Azeb"))
