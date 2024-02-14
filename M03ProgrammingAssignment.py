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
  for num in range(1, 10, 2):
    yield num

count = 0
for num in get_odd():
  count += 1
  if count == 3:
    print("3rd odd number": num)
    break


list2 = []
list2 = get_odds()

print("\nThird value generated is: ", list2[2], "\n")
