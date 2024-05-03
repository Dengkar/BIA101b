class person :
    def _int_(self,name ,age,cid):
      self.name = name 
      self.age = age
      self.cid = cid  
def walk(self):
    print(self.name,"is walking")
def talk(self):
    print(self.name,"is talking")
def sleep(self):
    print(self.name,"is sleeping")
def eat(self):
    print(self.name,"is eating")
class Teacher(person):
    def __init__(self,name,age,cid,subject,salary,department,designation):
        super().__init__(name,age,cid) # in order to avoid writing self.name 
        self.subject = subject
        self.salary = salary
        self.departmant = department
        self.desigantion = designation
    def teach(self):
      print(self.name,"is teaching")
    def grade_student(self):
        print(self.name,"is grading")
    def attend_meeting(self):
        print(self.name,"is attending meeting")
t1 = Teacher("tashi",30,1225,"physic",3000,"science","assistant") 
t2 = Teacher("dorji",31,1234,"managemnt",2000,"commerce","full teacher")
class Student(Teacher):
    def _init_(self,name,age,cid,std_id,course,year,gpa):
        super().__init_(name,age,cid)
        self.std_id = std_id
        self.course = course
        self.year = year
        self.gpa = gpa
    def study(self):
        print(self.name,"is studing")


s1= Student("penjor",18,1111,12345,"bbi",1,2)
s2 = Student("Karma",19,1234,12345,"bbi",2,4)
if s1.gpa > s2.gpa:
    print(s1.name,"is better than",s2.name)
    student_infroamtion = "year:"+s1.year +"course: " + s1.course
    print(student_infroamtion)
else:
    print(s2.name,"is better than",s1.name)
    student_infroamtion = "year:"+s2.year +"course: " + s2.course
    print(student_infroamtion)


student_storage = [s1,s2]
for std in student_storage:
    print(std.name)
    print(std.course)
    print(std.gpa)
    print("=========")






