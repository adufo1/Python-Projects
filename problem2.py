def main():
  string = open('info.txt', 'r')
  for word in string:
    print(word)
  #read_Names = 'info.txt'
  for word in string:
    if word in 'AEIOU':
      print('V')
    else:
      print(word, end='')
  
main()
