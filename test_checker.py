# code for a simple test checker if passed or failed 

name = input("Enter the student's name: ")
score = int(input("Enter the student's score: "))
pass_grade = 50
has_passed = (score >= pass_grade)
if has_passed == True:
	print("{} passed their test with a score of {}.".format(name, score))
else:
	print("{} failed their test with a score of {}.".format(name, score))


#Reverse application.
print("-----Enter the students tests scores to see whether how they performed------")
name = input("Enter the student's name: ")
score = int(input("Enter the student's score: "))
pass_mark = 50
has_failed = (score < pass_mark)

if has_failed == True:
	print("{} has failed their test with a score of {}.".format(name, score))
else:
	print("{} has passed their test with a score of {}.".format(name, score))
