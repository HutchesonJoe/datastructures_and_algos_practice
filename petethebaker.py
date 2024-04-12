# take in a list of required ingredients; compare the list of available ingredients to discover how many you can make
# make sure there is a minimum available for all
# iterate through, making sure that the minimum is available; as you go, check how many can be made from that and keep track. If any available is less than the required, return zero.

def cakes(recipe, available):
  rv = 0
  for item, amount in recipe.items():
    if available[item] < amount:
      return 0
    else:
      if available[item] // amount < rv:
        rv = available[item] // amount
  return rv

