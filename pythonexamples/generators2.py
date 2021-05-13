def first_n_values_generator(n):
	i=1
	while i<=n:
		yield i
		i=i+1
g=first_n_values_generator(10)
for x in g:
	print(x)
