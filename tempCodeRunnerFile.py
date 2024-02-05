def get_odds():
  for i in range(10):
    if i%2 != 0:
      yield i

odds = get_odds()

for i in range(3):
  if odds[i] == odds[2]:
    print(i)