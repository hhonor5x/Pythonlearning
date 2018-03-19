## If condition:
##    statement1
##    statement2
##    .
##    .

##nationality= input("please enter your nationality:")

##if nationality == "Indian" or nationality =="indian" :
##    print("You are from INDIA, you can speak Hindi")
    
    
# if .. elif ..else

##if nationality=="indian":
##    print('You are from India')
##elif nationality =="pakistani":
##    print("You are from Pakistan")
##elif nationality == "american":
##    print("You are from United States")
##else:
##    print("Thank you!, We need to add your nationality to our database, Kindly Bear with us")
    
# True or False in Python

##The following objects are evaluated by Python as False:
##
##    numerical zero values (0, 0.0, 0.0+0.0j),
##    the Boolean value False,
##    empty strings,
##    empty lists and empty tuples,
##    empty dictionaries.
##    plus the special value None. 

## The other values consider as True

##grade = eval(input("Please enter your marks:"))
##final_grade=0
##for value in grade.values():
##    final_grade +=value
##
##print("Total marks:", final_grade)
##final_grade*= 100/500
##print("percentage=", final_grade)
##
##
##if final_grade > 80 :
##    print("You passed in 1st class")
##elif final_grade > 70 and final_grade < 80 :
##    print("You passed in 2nd class")
##elif final_grade > 50 and final_grade < 70 :
##    print("You passed in 3rd class")
##else:
##    print("You Failed!!! ")
##    


# Terenary If

##max = a if (a > b) else b
##
##
### Break and continue
##
##break will use to come out of loop
##continue will be pass the control again to starting of loop
##
##Example
##
##for i in range(5):
##    if i > 3:
##        break
##    else:
##         print(i)
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
    
    


