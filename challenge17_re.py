import re
l = "The ghost that says boo haunts the loo"
matches = re.findall(".oo",l,re.IGNORECASE)

print(matches)
