def main():
  print("Hello learners!")

def addmultiplenumbers(num):
  return sum(num)

def multiplymultiplenumbers(num):
  result = 1
  for num in num:
      result = result * num
  return result

def isiteven(num):
    return num %2 == 0 and num % 1 == 0

def isitaninteger(num):
   return num % 1 == 0

if __name__=="__main__":
  main()    