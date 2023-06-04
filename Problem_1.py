class RomanNumeral:
  def UserNum(self):
    self.i_to_r = int(input("Enter a number between 1 and 10: "))
  def ConvertNum(self):
    if self.i_to_r == 1:
      self.i_to_r = "I"
    elif self.i_to_r == 2:
      self.i_to_r = "II"
    elif self.i_to_r == 3:
      self.i_to_r = "III"
    elif self.i_to_r == 4:
      self.i_to_r = "IV"
    elif self.i_to_r == 5:
      self.i_to_r = "V"
    elif self.i_to_r == 6:
      self.i_to_r = "VI"
    elif self.i_to_r == 7:
      self.i_to_r = "VII"
    elif self.i_to_r == 8:
      self.i_to_r = "VIII"
    elif self.i_to_r == 9:
      self.i_to_r = "IX"
    elif self.i_to_r == 10:
      self.i_to_r = "X"
    else:
      print("You've either entered a number less than 1, greater than 10, or your input wasn't a number!")
  def GetNum(self):
    return self.i_to_r

def main():
  Num_to_Rom = RomanNumeral()
  print("You will now be prompted to input a number...")
  Num_to_Rom.UserNum()
  Num_to_Rom.ConvertNum()
  print("Your input as a Roman Numeral is ", Num_to_Rom.GetNum())
main()
  