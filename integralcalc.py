def integrate(f,a,b,n,method):
    dx = (b-a) / n 
    if method == "simpson":

        total = 0
        x = a
        for i in range(n):
            total = total + dx/6 * (f(x) + 4*f(x + dx/2) + f(x + dx))
            x = x + dx
        return total

    elif method == "trapezoid":
        total = 0
        x = a
        for i in range(n):
            total = total + 0.5 * (f(x) + (f(x + dx))) * dx
            x = x + dx
        return total
    else:
        total = 0
        x = a
        for i in range(n):
            total = total + f(x)* dx
            x = x + dx
        return total
        
def f(x):
    return x**2

print(integrate(f, 0, 2, 1000, 'simpson'))
print(integrate(f, 0, 2, 1000, 'trapezoid'))
print(integrate(f, 0, 2, 1000, 'left'))
