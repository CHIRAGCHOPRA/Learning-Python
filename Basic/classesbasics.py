class student:
	'''def __init__(self, roll, name): 
		self.roll=roll
		self.name=name'''
	def details(self):
		#print("student:	"+"rollno=",self.roll,"	name= "+self.name)
		print("details of student")
class subjectsOpt(student):
	# def __init__(self):
	# 	student.roll=roll
	# 	student.name=namef
	def name(self):
		print("name called")
'''emp1=student(1510991158,"chetanya")
emp2=student(1510991156,"chetab")

emp2.details()
emp1.details()'''
def factorial(num):
	fact=1;
	while num>0:
		if num==0:
			return fact
		fact=fact*num
		--num


st=subjectsOpt();
st.details();
st.name();
# print(factorial(5))