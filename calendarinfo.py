print("----------------------------------CALENDAR INFO------------------------------------")
print("-------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------")
class Calendar:

    def __init__(self, day, month):
        self.day = day
        self.month = month
    def print(self):
        print("Day " + str(self.day) + " ) " + self.month + " " "INFO")
        print("--------------------------")
class January(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "JANUARY")
        self.major_holiday = "MLK"
        self.birth_stone = "Garnet"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")

class February(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "FEBRUARY")
        self.major_holiday = "Valentines Day"
        self.birth_stone = "Amethyst"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")

class March(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "MARCH")
        self.major_holiday = "St.Patricks Day"
        self.birth_stone = "Aquamarine"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")
            
class April(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "APRIL")
        self.major_holiday = "April Fools Day"
        self.birth_stone = "Diamond"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")
      
           
class May(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "MAY")
        self.major_holiday = "Cinco de Mayo"
        self.birth_stone = "Emerald"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")
            
class June(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "JUNE")
        self.major_holiday = "Fathers Day"
        self.birth_stone = "Pearl"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")
             
class July(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "JULY")
        self.major_holiday = "4th of July"
        self.birth_stone = "Ruby"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")
      
class August(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "AUGUST")
        self.major_holiday = "Left Handers Day"
        self.birth_stone = "Peridot"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")
            
class September(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "SEPTEMBER")
        self.major_holiday = "Labor Day"
        self.birth_stone = "Sapphire"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")
           
class October(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "OCTOBER")
        self.major_holiday = "Halloween"
        self.birth_stone = "Tourmaline"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")

class November(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "NOVEMBER")
        self.major_holiday = "Thanksgiving"
        self.birth_stone = "Topaz"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")
             
class December(Calendar):
    def __init__(self, day):
        Calendar.__init__(self, day, "DECEMBER")
        self.major_holiday = "Christmas"
        self.birth_stone = "Tanzanite"

    def print(self):
        Calendar.print(self)
        print("MAJOR HOLIDAY: " + self.major_holiday)
        print("BIRTHSTONE: " + self.birth_stone + "\n")

class Test:
    def __init__(self) -> None:
        self.days = []

    def read_file(self):
        with open("calendar.txt") as contents:
            for line in contents:
                for day in line.split():
                    self.days.append(int(day))
    def sort_day(self):
        for day in self.days:
            if day == 1 or day <= 31:
                month = January(day)
            elif day == 32 or day <= 59:
                month = February(day)
            elif day == 60 or day <= 90:
                month = March(day)
            elif day == 91 or day <= 120:
                month = April(day)
            elif day == 121 or day <= 151:
                month = May(day)
            elif day == 152 or day <= 181:
                month = June(day)
            elif day == 182 or day <= 212:
                month = July(day)
            elif day == 213 or day <= 243:
                month = August(day)
            elif day == 244 or day <= 273:
                month = September(day)
            elif day == 274 or day <= 304:
                month = October(day)
            elif day == 305 or day <= 334:
                month == November(day)
            elif day == 335 or day <= 364:
                month = December(day)

            month.print()

type_out = Test()
type_out.read_file()
type_out.sort_day()