name=input("what is your name: ")
lab=float(input("what is your lab grade: "))
midterm=float(input("what is your midterm grade: "))
final=float(input("what is your final grade: "))
Last_score=(lab * 0.25) + (midterm * 0.35) + (final * 0.4)

print("your name: " + name)
print("your lab score is: ",lab)
print("your midterm score is: ",midterm)
print("your final score is: ",final)
print("Last score : ",Last_score)