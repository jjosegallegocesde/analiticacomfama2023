import pandas as pd

paciente1 = [45,280,124,250,79,300,26,59,200,60,210,39,110,59,69,54]
pasiente2 = [120,125,122,125,119,121,120,119,120,124,125,120,117,130,127,125]

p1 = pd.DataFrame(paciente1)
p2 = pd.DataFrame(pasiente2)

print(p1.describe())

print(p2.describe())
