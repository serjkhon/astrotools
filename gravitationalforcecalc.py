# Gravitational force calculator

def gravitationalforce (m1,m2,d):
 x = ((m1 * m2) / d **2)* 6.674*10**-11
 return x

print(gravitationalforce(6 * 10**24,7.3 * 10**22,3.8 * 10**8))
