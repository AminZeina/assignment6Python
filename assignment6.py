# Created By: Amin Zeina
# Created On: Apr 2018
# Calculates Pi

answer = 0
times_calculated = -1
iterations_entered = input('Enter an integer: ')
# check if entry is an integer
try:
   iterations_entered_as_integer = int(iterations_entered)
except ValueError:
   print("Invalid Entry. Please only enter an integer.")

# allows loop when 0 is entered and makes calculations acurate to number entered, unlike in Corona
iterations_entered_as_integer = iterations_entered_as_integer + 1 

for times_calculated in range(0,iterations_entered_as_integer):
	# do calculation
	answer = answer + (((-1)**times_calculated) / ((2*times_calculated)+1))*4

print(answer)

input('Program End.')