'''
A python function can take none or mutiple inputs 
It can also return mutiple outputs
'''

PI = 3.14

def degree2Radius(degree1, degree2):

    radius1 =  degree1/180.0*PI
    radius2 =  degree2/180.0*PI

    return radius1, radius2

def main():

    degree1 = 180
    degree2 = 90

    radius1, radius2 = degree2Radius(degree1, degree2)
    print("converted values:", radius1, radius2)

    return

main()