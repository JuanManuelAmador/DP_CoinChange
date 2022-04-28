import sys
from decimal import *


def main():
  
  if len(sys.argv) != 2:
      print('usage: python3 main.py [change]')
      exit(0)
    
  #validate for number
  try:
    changeToGive = Decimal(sys.argv[1])
  except ValueError:
    print("Only numbers accepted")
    exit(0)

  #If number multiply to get number of cents
  changeToGive = Decimal(sys.argv[1])
  changeToGive = int(changeToGive * 100)

  #validate for pos value
  if changeToGive <=0 :
    print('usage: only positive values accepted')
    exit(0)

  #hardcoded coins as in the problem, if needed this can be done dinamically  
  coins  = [1,5,10,25]
  

  #initialize array with max integer , pos 0 is the base case value is 0
  max = sys.maxsize
  memList = [max] * (changeToGive + 1)
  #print(memList)
  #print(len(memList))

  memList[0] = 0
  
  
  for i in range(1,len(memList)):
    for j in coins:
      #ugly debug tools, i developed in repl.it
      #print(j)
      #print(i)

      if i - j >= 0:
        #print('entro al if')
        memList[i] = min(memList[i],memList[i-j]+1)
        #print(memList[i])

  print ( 'Min change')  
  print (memList[len(memList)-1])

  
  
main()
