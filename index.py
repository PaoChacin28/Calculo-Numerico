from sympy import symbols 
from sympy import lambdify
from sympy import simplify

print("")
x = symbols('x') 
fn = simplify(input("Ingrese la funcion: "))
f = lambdify(x, fn)

a = float(input("Valor inicial de a: "))
b = float(input("Valor inicial de b: "))
crit = float(input("criterio de parada "))
i = 0
error = 1
x_ant = 0

if f(a)*f(b)<0:
    
    
    print("")
    print("{:^60}".format("METODO DE BISECCION"))
    print("{:^10} {:^10} {:^10} {:^10}".format("i", "a", "b", "xr", "error(%)"))
    
    while error > crit:
        xr = (a+b)/2
        error = abs((xr-x_ant)/xr)
        
        if f(xr)*f(a)<0:
            b = xr
        else:
            a = xr
        
        x_ant = xr
        
        print("{:^10} {:^10f} {:^10f} {:^10f} {:^10}".format(i, a, b, xr, round(error * 100, 9)))
        i = i+1
        
    print("")
    print("el valor de x es ", round(xr, 9), "con un error de ", round(error *100, 9), "%")
    
else: 
    
    print("")
    print("la funcion no tiene una raiz en el intervalo de " + "x =" + str(a) + "a x = " + str(b))
    print("Ingresar otros valores iniciales")
    
        