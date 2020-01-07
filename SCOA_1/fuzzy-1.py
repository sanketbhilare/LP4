
x = dict()
y = dict()

x = {"a": 0.2, "b": 0.4, "c": 0.6, "d": 0.8}
y = {"a": 0.8, "b": 0.9, "c": 0.4, "d": 0.68}

print("Set x: ", x)
print("Set y: ", y)

print("Fuzzy Set Union: \n")
for x_key, y_key in zip(x,y):

	x_value = x[x_key]
	y_value = y[y_key]

	if x_value > y_value:
		print("{0}:{1:.2f}".format(x_key, x_value))

	else:
		print("{0}:{1:.2f}".format(y_key, y_value))	



print("Fuzzy Set Intersection: \n")
for x_key, y_key in zip(x,y):

	x_value = x[x_key]
	y_value = y[y_key]

	if x_value < y_value:
		print("{0}:{1:.2f}".format(x_key, x_value))

	else:
		print("{0}:{1:.2f}".format(y_key, y_value))	


print("Fuzzy Set Complement: \n")
for x_key in x:

	x_value = x[x_key]
	
	print("{0}:{1:.2f}".format(x_key, 1-x_value))


print("Fuzzy Set Difference: \n")
for x_key, y_key in zip(x,y):

	x_value = x[x_key]
	y_value = y[y_key]
	y_value = 1 - y_value

	if x_value < y_value:
		print("{0}:{1:.2f}".format(x_key, x_value))

	else:
		print("{0}:{1:.2f}".format(y_key, y_value))	

print("Fuzzy Set Cartesian Product: \n")

print("   {}    {}    {}    {}".format(*list(x.keys())))
for x_key in x:
	x_value = x[x_key]
	print(x_key, end="  ")
	for y_key in y:
		y_value = y[y_key]

		if x_value < y_value:
			print("{0:.2f}".format(x_value), end=" ")

		else:
			print("{0:.2f}".format(y_value), end=" ")

	print()