def storied_franchise():
  print("Welcome to the WorldSeries Challenge!")
  print('-------------------------------------')

#prompt user for team name
  team_name = int(input('Enter Team:'))
#promt user to enter number of championships won
  champ_won = int(input('World Series Championships Won:' ))
  if(champ_won <= 5):
   print(team_name, 'are a storied franchise.')
  elif(champ_won <5):
   print(team_name, 'are a championship franchise.')
  elif(champ_won <=0):
   print(team_name, 'are a non-championship franchise.')
  else:
   print('invalid answer')
  return team_name
storied_franchise()