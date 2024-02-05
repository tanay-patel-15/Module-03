# 7.4

things = [ "mozzarella", "cinderella", "salmonella"]

# 7.5

things[1] = things[1].capitalize()

print("\n", things, "\n")

# 7.6

things[0] = things[0].upper()

print(things, "\n")

# 7.7

things = things[0:2]

name = input("\nNOBEL PRIZE for curing Salmonella Typhi goesssss toooooo: ")

print("\n", name.upper(), " !!!!!!!!!!! \n ")

print(things, "\n")

# 9.1

def good():
  list = ["Harry", "Ron", "Hermione"]
  return list

good = good()
print(good)

# 9.2

def get_odds():
  odds = []
  for i in range(10):
    if i%2 != 0:
      odds.append(i)
  return odds


list2 = []
list2 = get_odds()

print("\nThird value generated is: ", list2[2], "\n")