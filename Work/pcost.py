# pcost.py
#
# Exercise 1.27
cost = 0.0
f = open("./Data/portfolio.csv", "rt")
next(f)

for line in f:
    cost = cost + ( int((line.split(","))[1]) * float(line.split(",")[2]) )

print (cost)
