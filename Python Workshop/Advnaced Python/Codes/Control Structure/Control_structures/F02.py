'''
Write a python program to print a lower triangle of stars
'''

for row in range(0,5):
  for col in range(0, row):
  	print(" ", end='')
  for col in range(row, 5):
    print("*", end='')
  print("")


