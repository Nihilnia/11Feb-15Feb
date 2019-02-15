from time import sleep

successfulStudent = open("succesfulOnes.txt", "a", encoding = "utf-8")
unsuccessfulStudent = open("unsuccesfulOnes.txt", "a", encoding = "utf-8")

while True:
    studentName = input("Student name (Q for quit): ")
    if studentName != "q":
        for numbers in range(0,10):
            if str(numbers) in studentName:
                raise ValueError("Number in a student name? Cmon!")
        try:
            studentNote = int(input("Student note: "))
            if studentNote >= 70:
                successfulStudent.writelines("Student name: {} Note: {}\n".format(studentName, studentNote))
                print("Added to successful students.")
            else:
                unsuccessfulStudent.write("Student name: {} Note: {}\n".format(studentName, studentNote))
                print("Added to Unsuccessful students.")
        except ValueError:
            print("Please give me numeric value!")
            continue
    
    else:
        break

successfulStudent.close()
unsuccessfulStudent.close()