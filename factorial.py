n = int(input("Enter a number "))

count = 0
i=5
while (n/i>=1): 
    count += int(n/i) 
    i *= 5
  

print("Count of trailing 0s "+
    "in 100! is",count) 