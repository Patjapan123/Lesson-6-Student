from code import Student

s123456 = Student(123456, "Billy", "Smith")

s123456.add_grade(86)
s123456.add_grade(82)
s123456.add_grade(83)
s123456.calculate_grade() #shouldnt do anything 
s123456.add_grade(85)
if s123456.calculate_grade() == 84:
	print("Test Case 1 Passed!")
else:
	print("Test Case 1 Failed! Expected grade 84, got", s123456.calculate_grade())

print("Transcript Expects: Smith, Billy : 123456; 84%")
print("Transcript Print  : ",end="");
s123456.print_transcript()