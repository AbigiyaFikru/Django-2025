scores={"selam":85,"abebe":92,"beti":78}
name=input("enter the student name")
try:
    print(scores[name])
except Exception:
    print("Student does not found in the system")