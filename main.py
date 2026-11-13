def main():
  print("Hello learners!")

def addmultiplenumbers(num):
  return sum(num)

#print(addmultiplenumbers([2, 3, 4]))

def multiplymultiplenumbers(num):
  result = 1
  for num in num:
      result = result * num
  return result
#print(multiplymultiplenumbers([2, 3, 4]))

def isiteven(num):
    return num %2 == 0 and num % 1 == 0

def isitaninteger(num):
   return num % 1 == 0

if __name__=="__main__":
  main()    