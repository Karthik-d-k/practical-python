# bounce.py
#
# Exercise 1.5

height = 100   # in meters
n_bounces = 10 # no. of bounces

for i in range(n_bounces):
    height *= 3/5 
    print(i+1, round(height, 4))
