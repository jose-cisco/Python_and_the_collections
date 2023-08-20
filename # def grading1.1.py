# def grading1.1
Midterm_Score             = eval(input('Enter Midterm Score:'))
Final_Score               = eval(input('Enter Final   Score:'))
Total_Score,Grade         = 40,F

def grading():
    Total_Score           = Midterm_Score + Final_Score
    if Total_Score >= 80.0:
        Grade = "A"

    elif Total_Score >= 75.0:
        Grade = "B+"

    elif Total_Score >= 70.0:
        Grade = "B"

    elif Total_Score >= 65.0:
        Grade = "C+"

    elif Total_Score >= 60.0:
        Grade = "C"

    elif Total_Score >= 55.0:
        Grade = "D+"

    elif Total_Score >= 50.0:
        Grade = "D"

    else:
        Grade = "F"
    return Total_Score,Grade

Total_Score,Grade     = grading()
print('in grading Total_Score ={} Grade:{}'.format(Total_Score,Grade))
