"""
Use for loops. Ask the user how many numbers N  they will insert. The user will insert N amount of integers. Your program will count how many numbers are less than or equal to 100. 
"""
print("I will count how many numbers given are under 1")
numOfNums = int(input("How many numbers do you want to input? "))
count = 0
for i in range(numOfNums):
  x = int(input("give me a number "))
  if x <=100:
    count += 1
print(f"{count} numbers are under or equal to 100")
#checks if a number is under 100 and adds it up to variable count