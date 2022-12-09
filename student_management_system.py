class Student:
    
    def __init__(self,student_id,name,date_of_birth,home_town,major,layer):
        self.student_id = student_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.home_town = home_town
        self.major = major
        self.layer = layer
        
    def print_student_info(self):
        
        print("ID           : ",self.student_id )
        print("Name         : ",self.name)
        print("Date of birth: ",self.date_of_birth)
        print("Home town    : ",self.home_town)
        print("Major        : ",self.major)
        print("Class        : ",self.layer)
        print()
        
class Student_List:
    
    def __init__(self):
        self.student_list = []
        
    def find_student_index(self,seach_id):
        index = -1
        for i in range(self.student_list):
            if student_list[i].student_id == seach_id:
                index = i
        return index
    
    def seach_student_info(self):
        seach_id = int(input("Input student ID : "))
        found_index = self.find_student_index(seach_id)
        if found_index == -1:
            print("Your ID not found")
        else:
            self.student_list[found_index].print_student_info()
    
    def add_student(self):
        student_id = int(input("Input student ID : "))
        name = input("Input student name : ")
        date_of_birth = input("Input student date of birth : ")
        home_town = input("Input student home town :")
        major = input("Input major : ")
        layer = input("Input layer : ")
        
        
        student = Student(student_id,name,date_of_birth,home_town,major,layer)
        self.student_list.append(student)
     
    
    def display_student_list(self):
        for item in self.student_list:
            item.print_student_info()
            
    def delete_student_info(self):
        seach_id = int(input("Input student ID : "))
        found_index = find_student_index(self,seach_id)
        if found_index == -1:
            print("Your ID not found")
        else:
            del self.student_list[found_index]
     
    def update_student_info(self):
        seach_id = int(input("Input student ID : "))
        found_index = find_student_index(self,seach_id)
        if found_index == -1:
            print("Your ID not found")
        else:
            del self.student_list[found_index]
            
    def sort_student_list(self):
        sorted(self.student_list,key=lambda student: student.student_id)
        
        
#main

student_list = Student_List()

while True:
    
    #print("Input your option : |n
     #     1: display student info |n
      #    2: seach student info |n
       #   3: add student |n
        #  4: delete student info |n
         # 5: update student info |n
          #6: sort student")
          
    option = int(input())
    if option ==1 :
          student_list.display_student_list()
    elif option ==2:
          student_list.seach_student_info()
    elif option ==3:
          student_list.add_student()
    elif option ==4:
          student_list.delete_student_info()
    elif option ==5:
          student_list.update_student_info()
    elif option ==6:
          student_list.sort_student_list()
    else:
          print("your option is not exis")
          
    choise = int(input("press 0 to continue :"))
    if choise:
          break
          

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        