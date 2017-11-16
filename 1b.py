# 1b.
# Write a temperature converter python program, 
# which is menu driven. 
# Each such conversion logic should be 
# defined in separate functions. 
# The program should call the respective 
# function based on the user’s requirement. 
# The program should run as long as the user wishes so. 
# Provide an option to view the conversions stored 
# as list of tuples with attributes - 
# from unit value , to unit value sorted by 
# the user’s choice (from-value or to-value).
#PART A: 1
import datetime

def to_degree(temp):
	return (float(temp)-32)*5/9
	
def to_fahre(temp):
	return (float(temp)*9/5) + 32
	
def display():

	print("\n1.Sort by from value")
	print("\n2.Sort by to value")
	c = int(input("\nEnter your choice : "))
	
	if c == 1:
		new = sorted(old, key=lambda x: x[2])
	else:
		new = sorted(old, key=lambda x: x[3])
		
	for i in new:
			print ("******************************************")
			print ("\nFROM : ",i[0])
			print ("\nTO   : ",i[1])
			if(i[0] in "Degree"):
				print ("\nDEG  : ",i[2])
				print ("\nFAHRENHEIT : ",i[3])
			else:
				print ("\nDEG  : ",i[3])
				print ("\nFAHRENHEIT : ",i[2])
			print ("******************************************")
	
old = []


while(1):
	print("-------------------------------------------------------------------------------")
	print("\n1.Degree to Fahrenheit")
	print("\n2.Fahrenheit to Degree")
	print("\n3.View previous conversions")
	print("\n4.Exit")
	
	ch = int(input("Enter your choice : "))
	
	if(ch == 1):
		
		deg = int(input("\nEnter in degrees : "))
		fahre = to_fahre(deg)
		print(" FAHRENHEIT : ",fahre)
		tup = ("Degree","Fahrenheit",deg,fahre)
		old.append(tup)
	elif(ch == 2):
		
		fahre = int(input("\nEnter in fahrenheit : "))
		deg = to_degree(fahre)
		print("DEGREE : ",deg)
		tup = ("Fahrenheit","Degree",fahre,deg)
		old.append(tup)
	elif(ch == 3):
		display()
		
	else:
		exit()

				

