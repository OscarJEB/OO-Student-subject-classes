class Person:
    def __init__(self, firstName, lastName)
    self.firstName = firstName
    self.lastName = lastName

    #print full name method
    def PrintFullName(self):
        print(f(self.firstName, self.lastName))

    #student class
    class Student(Person):
        def __init__(self, firstName, lastName, studentID, houseG, subjects)
            super __init__(firstName, lastName)
            self.studentID = studentID
            self.houseG = houseG
            self.subjects = []
    
        #enrol in class method
        def EnrolClass(self, subjectName):
            s1 = Subject(subjectName, self.studentID)
            self.subjects.append.input("")
            return("Enrolled.")
    
    #subject class
    class Subject:
         def __init__(self, subjectName, studentID)
            self.subjectName = subjectName
            self.studentID = studentID
            self.enrolledStudentsList = []

        #student list method
        def PrintStudentList(self):
            print(f(self.enrolledStudentsList, sep =', '))


    #parent class
    class Parent(Person):
        def __init__(self, firstName, lastName, occupation, alumni)
            super __init__(firstName, lastName)
            self.occupation = occupation
            self.alumni = False

Oscar_Burge = student("Oscar", "Burge", 122333, "Barker")
Oscar_Burge.EnrolClass()