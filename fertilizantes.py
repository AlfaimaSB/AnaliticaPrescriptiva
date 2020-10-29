#-----------------
# Modelo
#-----------------
m = lp.LpProblem(
                "Fertilizacion", #Nombre 
                 lp.LpMinimize    #Sentido     
                 )
#-----------------
# Variables
#----------------- 
#Avicompost
x1 = lp.LpVariable("Avicompost", #Nombre
                   0,            #Valor mínimo
                   None,         #Valor máximo
                   cat= lp.LpContinuous #naturaleza
                  )
#TripleNPK
x2 = lp.LpVariable("TripleNPK",0,None,cat= lp.LpContinuous)
                 
#-----------------
# Restricciones
#----------------- 
m += x1 >= 1.5, "MinCompost"
m += 0.0147*x1 + 0.18*x2 >= 0.15, "Nitrogeno"
m += 0.0436*x1 + 0.18*x2 >= 0.09, "Fosforo"
m += 0.0307*x1 + 0.18*x2 >= 0.20, "Potasio"
                 
#-----------------
# Función objetivo
#-----------------

m += 280*x1 + 1820*x2 
                 
#-----------------
# Archivo de optimización
#-----------------

m.writeLP("Fertilizantes.lp")
m.solve(lp.PULP_CBC_CMD(msg=0))
                 
#-----------------
# Solución
#-----------------
print("Status:", lp.LpStatus[m.status])

print("Recomendación de fertilización")
for v in m.variables():
	print(v.name, "=", v.varValue, "kg")