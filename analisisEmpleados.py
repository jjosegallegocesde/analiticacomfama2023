import pandas as pd

empleados=pd.read_csv("./empleados.csv")

analistasBajoCosto=empleados[(empleados["salario"]<=5000000) & (empleados["cargo"]=="analista1")].head(20)

#Exportando un dataframe hacia HTML
archivoHTML=analistasBajoCosto.to_html()
archivoGenerado=open("bajocosto.html", "w", encoding="utf-8")
archivoGenerado.write(archivoHTML)
archivoGenerado.close()