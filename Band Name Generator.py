def BandNameGenerator():
  print ("Hello! Welcome to the Band Name Generator.\n")
  city_name = input("What's the name of the city you grew up in?\n").capitalize()
  pet_name = input ("What's the name of your Pet?\n").capitalize()
  band_name = f'Your band name is {city_name} {pet_name}'
  return band_name

print(BandNameGenerator())