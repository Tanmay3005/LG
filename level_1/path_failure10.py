import sys
from random import randint
number1=randint(1,15)
number2=randint(1,15) 
print("question 10")
print(number1,'X',number2)
correct_ans=int((number1*number2))
ans=int(input('ans'))
if ans==correct_ans:
   print("well done")
   print("next question")
   import projects.level_1.path_failure5 as path_failure5
 
  
  



else:
 sys.exit
 print("worng")