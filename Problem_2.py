
import random
global tries
tries = 4
class Picknumber:
  import random
  global tries
  tries = 4
  number = random.randint(1,10)
  for i in range(0,2):
    user = int(input('Pick any number between 1 and 10:'))
    if user == number:
      print('Congradulations, you got it right!!')
      print(f'{number} Is correct')
    if user != number:
      print(f'{number} : Number is invalid, try again' + "You have" + str(tries) + "try left")
  
  