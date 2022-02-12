# ===========class student=======================
class Student:
	def __init__ (self, first_assignment, second_assignment, first_cat, second_cat,final_mark):
		self.first_assignment = first_assignment
		self.second_assignment = second_assignment
		self.first_cat = first_cat
		self.second_cat = second_cat
		self.final_mark = final_mark
#================ cal culation of cat,ass and final exam ========================
	def total_Results(self,first_assignment, second_assignment, first_cat, second_cat, final_mark):
		total_mark_Ass = int(first_assignment + second_assignment)
#=====================total marks for cat============================================================
		total_Cat_Marks = int(first_cat+ second_cat)
		total_Results = int(final_mark + int((total_mark_Ass+total_Cat_Marks)/4))
		return total_Results
    
# ========== users inputs =============================================================
first_assignment  = int (input('enter student first Ass marks :'))
second_assignment = int (input('enter student second Ass marks:'))
first_cat = int(input('enter student fist cat: '))
second_cat = int(input('enter student second cat: '))
final_mark= int(input('enter the final exam marks: '))

#======================= creating object to class  =================================
p1 = Student(first_assignment, second_assignment, first_cat, second_cat, final_mark)
total_Results = p1.total_Results(first_assignment, second_assignment, first_cat, second_cat, final_mark)

# ========================= grading student results =================================
def grading(total_Results):
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
