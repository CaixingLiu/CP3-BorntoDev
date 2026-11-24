'''ถ้าเกิดคะแนน
มากกว่าหรือเท่ากับ 80 จะได้เกรด A
มากกว่าหรือเท่ากับ 75 จะได้เกรด B+
มากกว่าหรือเท่ากับ 70 จะได้เกรด B
มากกว่าหรือเท่ากับ 65 จะได้เกรด C+
มากกว่าหรือเท่ากับ 60 จะได้เกรด C
มากกว่าหรือเท่ากับ 55 จะได้เกรด D+
มากกว่าหรือเท่ากับ 50 จะได้เกรด D
น้อยกว่า         50 จะได้เกรด F'''
score = int(input("Enter your score: "))
if score >= 80:
    print("Your grade is A")
elif score >= 75:
    print("Your grade is B+")
elif score >= 70:               
    print("Your grade is B")
elif score >= 65:
    print("Your grade is C+")
elif score >= 60:
    print("Your grade is C")
elif score >= 55:
    print("Your grade is D+")
elif score >= 50:
    print("Your grade is D")
else:
    print("Your grade is F")