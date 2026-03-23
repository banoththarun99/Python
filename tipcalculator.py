print("wellcome to the tip calculator!")
bill = float(input("what was the total bill? :$"))
tip = int(input(("how much tip would you like to give? 10,12, or 15? :")))
people = int(input(("how many people split the bill : ")))

tip_cal = tip/100
bill_after_tip = bill * tip_cal
bill_amount = bill + bill_after_tip
bill_per_person = bill_amount / people
final_amount = round(bill_per_person,2)


print("each person should pay : $",final_amount)