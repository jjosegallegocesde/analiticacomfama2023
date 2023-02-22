import pandas as pd

empleados = pd.read_csv("./empleados.csv")

empleadoBajoCosto = empleados[(empleados["salario"] < 4000000) & (empleados["cargo"] == "analista1")].head(20)
print(empleadoBajoCosto)

archivoHTML = empleadoBajoCosto.to_html()
archivoGenerado = open("bajocosto.html", "w", encoding="utf-8")

archivoGenerado.write("<!DOCTYPE html>\n")
archivoGenerado.write("<html>\n")
archivoGenerado.write("<head>\n")
archivoGenerado.write('<meta charset="UTF-8">\n') # Incluir la codificación aquí
archivoGenerado.write("<title>Analisis Empleados</title>\n")
archivoGenerado.write("</head>\n")
archivoGenerado.write("<body>\n")
archivoGenerado.write(archivoHTML)
archivoGenerado.write("</body>\n")
archivoGenerado.write("</html>\n")
archivoGenerado.close()
