print ('this pseudocode allow lecture to input marks')
# inputting assignment marks 
first_assignment = int (input('enter student first Ass marks :'))
second_assignment = int (input('enter student second Ass marks:'))
#  inputting cat marks 
first_cat = int(input('enter student fist cat: '))
second_cat = int(input('enter student second cat: '))
# enter the final exam input
final_Exam_Marks = int(input('enter the final exam marks: '))
#  summation of assgnment 
total_mark_Ass = int(first_assignment + second_assignment)
# total marks for cat

total_Cat_Marks = int(first_cat+ second_cat)

# total results 

total_Results = int(final_Exam_Marks + int((total_mark_Ass+total_Cat_Marks)/4))

def grading(k):
	if total_Results >=70 or total_Results <= 100:
		print('Grade  A')
	elif total_Results >= 60 or total_Results <= 69:
		print ('Grade B')
	elif total_Results >=50 or total_Results <= 59:
		print('Grade C')
	elif total_Results >= 40 or total_Results <= 49:
		print('Grade D')
	elif total_Results >=0 or total_Results <= 39:
		print ('Grade E')
	else:
		print(' Invalid Grade')

grading(total_Results)
