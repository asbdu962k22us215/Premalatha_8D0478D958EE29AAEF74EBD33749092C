#to find leap year or not

def checkleap(year):
  if ((year%400==0)or(year%100!=0)and(year%4==0)):
    print("Given year is leap year")
  else:
    print("Given yearis not leap year")
year=int(input("Enter the year:"))
checkleap(year)