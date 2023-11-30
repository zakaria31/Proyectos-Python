#Calculo de rentabilidad de un BAR dias de mayor ganancias y de peour ganancias

dia1=float(input("Introduce las ventas del MARTES: "))
dia2=float(input("Introduce las ventas del MIERCOLES: "))
dia3=float(input("Introduce las ventas del JUEVES: "))
dia4=float(input("Introduce las ventas del VIERNES: "))
dia5=float(input("Introduce las ventas del SABADO: "))
dia6=float(input("Introduce las ventas del DOMINGO: "))

ventas=[dia1,dia2,dia3,dia4,dia5,dia6]
dias=["MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO"]



medbool="NO"

vmax=max(ventas)
pmax=ventas.index(vmax)

vmin=min(ventas)
pmin=ventas.index(vmin)

mediasem=(dia1+dia2+dia3+dia4+dia5)/5

if(mediasem<ventas[5]):
    medbool="SI"
else:
    medbool="NO"

print(dias[pmax] +"  "+dias[pmin]+"  "+medbool )


