health = 40

if health == 100:
	print('You are at full health.')
elif health >= 40:
	print('You have taken some minor damage. Health at ' + str(health))
elif health >= 1:
	print('You only have ' + str(health) + ' health. Critical warning!')
elif health == 0:
	print('You have died :(')