import pulp as lp

m = lp.LpProblem("Fertilizacion", lp.LpMinimize)

x1 = lp.LpVariable("Avicompost",0,None,cat= lp.LpContinuous)
x2 = lp.LpVariable("TripleNPK",0,None,cat= lp.LpContinuous)

m += x1 >= 1500, "MinCompost"
m += 0.0147*x1 + 0.18*x2 >= 150, "Nitrogeno"
m += 0.0436*x1 + 0.18*x2 >= 90, "Fosforo"
m += 0.0307*x1 + 0.18*x2 >= 200, "Potasio"

m += 280*x1 + 1820*x2 

m.writeLP("Fertilizantes.lp")
m.solve()

print("Status:", lp.LpStatus[m.status])

for v in m.variables():
	print(v.name, "=", v.varValue)

