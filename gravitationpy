# Basic calcs for gravitational force, acceleration, and escapevelocity. Sample variables used.


import math

G = 6.674*10**-11
EarthMass = 5.972 * 10**24 #kg
EarthRadius = 6.371 * 10**6 #m
MoonMass = 7.3 * 10**22

def gravitationalforce (m1,m2,d):
    x = ((m1 * m2) / d **2)* G
    return x

def acceleration(m1,d):
    a = m1/d**2 * G
    return a

def escapevelocity(m1,d):
    ev = math.sqrt((2*G*m1)/d)
    return ev


print("Gravitational force is: ", gravitationalforce(EarthMass, MoonMass, 3.8 * 10**8))
print("Acceleration is: ", acceleration(EarthMass, EarthRadius))
print("Escape velocity is: ", escapevelocity(EarthMass, EarthRadius))
