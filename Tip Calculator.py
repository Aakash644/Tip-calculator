# Tip Calculator
print("**Welcome to the Tip Calculator**")
bill=float(input("What was your total bill amount?\n")) 
tip=float(input("What Tip percentage would you like to give? 10 15 20?\n")) 
amt=bill+bill*(0.01*tip)
contri=float(input("How many people are paying?\n")) 
print(f"Each person has to pay:\n{round(amt/contri,2)}")
