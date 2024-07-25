a = int(input("enter temperature :"))

units = input("give ")

f = (a*(9/2)+32)
k = (273+a)
c = ((f - 32)*5/9)

if units == "c":
     print(f"temperature in fahreniet :({f})")
     print(f"temperature in kelvin : ({k})")
     
elif units == "k":
  print(f"temperature in fahreniet :({f})")
  print(f"temperature in fahreniet :({c})")
    
elif units == "f":
    print(f"temperature in fahreniet :({k})")
    print(f"temperature in fahreniet :({c})")

else :
  print ("coded")



















