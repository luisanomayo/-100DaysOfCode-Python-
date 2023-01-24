
def TipCalculator():
  #print welcome/opening message
  print ("Hello! I'm Your Tip Calculator.\n")

  #ask user to input total bill
  bill = float(input(f"What was the total bill?\n$"))
  
  #ask user for number of people to split the bill
  split_number = int(input("How many people to split the bill?\n"))
  
  #ask for tip percentage
  tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15\n"))

  #calculate tip value
  tip_value = bill * (tip_percentage/100)
  
  #determine the total bill value, including the tip
  total_bill = bill + tip_value

  #determine the bill per person
  bill_per_person = total_bill/split_number
  
  return f'Each person should pay ${bill_per_person:,.2f}'

print (TipCalculator())