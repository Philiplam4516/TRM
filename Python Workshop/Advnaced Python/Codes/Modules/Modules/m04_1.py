'''
Write a program to get a  circle radius from terminal, 
and then compute the area of the circle by a function 
'''
from m04_2 import compute_circle_area

def main():
  print("Enter a circle radius (m)")
  radius=input()
  radius = float(radius) # type cast from string to float

  area = compute_circle_area(radius=radius)
  print("area of the circle is {:.5f} m2".format(area))

  return

main()