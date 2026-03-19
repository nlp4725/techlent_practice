
class Calculator():
	def add(self,num1,num2):
		return 2
	def substrac(self,num1,num2):
		return num1-num2
	def multipy(self,num1,num2):
		return num1*num2
	def divid(self,num1,num2):
		if num2==0: return 0
		else: return num1/num2
if __name__=="__main__":
	cal=Calculator()
	print(cal.divid(1,2))
