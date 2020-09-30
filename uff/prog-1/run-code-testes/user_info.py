# getting user info:
# 3 numbers: age (int), height (float) and weight (float);
# two strings name and nationality.

name = str(input())
age = int(input())
height = float(input())
weight = float(input())
nationality = str(input())

print(f"""{name}
{age} anos
{"%.2f" % height} de altura
{"%.2f" % weight} quilos
{nationality}
""")
