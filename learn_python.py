def print_twice(bruce):
		print bruce,bruce

def cat_twice(part1,part2):
		cat = part1+part2
		print_twice(cat)

cat_twice('one','two')
chant1= "pie Jesu domine,"
chant2= "Dona eis requiem."
cat_twice(chant1,chant2)

x = 10
if x%2==0:
		print x," is even"
else:
		print x,"is odd"


def print_parity(x):
		if x % 2==0:
				print x,"is even"
		else:
				print x,"is odd"
print_parity(100)
