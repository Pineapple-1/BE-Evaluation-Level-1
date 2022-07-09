# so map does raise error they are the toturial is bad it is saying that it does not give error it does give error.
# beginner gets stuckkkk !! :(
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 7)))
print(result)


my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)
