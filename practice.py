name = input('What is your name? ')
print('Good Morning ' + name)
#new practice

birth_year = input('What is your birth year? ')
age =  2023 - int(birth_year)
print(age)

#practice 2 using float and strings

#first_number = input("First number: ")
#second_number = input("Second number: ")
#sum_number = float(second_number) + float(first_number)
#print('The sum is: ' + str(sum_number))

#practice3 using upper or lowercase and multiple/divide:

weight = float(input('Weight: '))
metrics = input("(K)g or (L)bs: ")
if metrics.upper == "K":
    converted = weight / 0.45
    print("Weight in Lbs is: " + str(converted))
else:
    converted = weight * 0.45 
    print("Weight in Kg is: " + str(converted))

#practice 4 making a list and fixing typos in list

favorite_food = ["jollorf rice", "eggs", "fried rice", "tea cake", "plantains", "efor riro"]
favorite_food [0] = "jollof rice"
favorite_food [5] = "efo riro"
print(favorite_food [0:6])
print(favorite_food)
print('plantains' in favorite_food)
print(len(favorite_food))


