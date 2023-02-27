marks=int(input("Enter your marks:"))
def GradingSystem(grade):
 if(grade<=100 and grade>=70):
  print("A")
 elif( grade<=69 and grade>=60):
  print("B")
 elif( grade<=59 and grade>=50): 
  print("C")
 elif( grade<=49 and grade>=40):
  print("D")
 elif( grade<=39 and grade>=30):
  print("E")
 else:
  print("Repeat")
GradingSystem(marks)
    
