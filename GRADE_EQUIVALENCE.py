def assign_grde():
    score = int(input("Enter ang grade ng estudyanteng pasaway:"))
    
    if score < 0 or score> 100:
        print("Invalid score! Please enter a value between 0-100")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score>= 60:
        print("Grade: D")
    else:
        print("Grade: F")
assign_grde()        
