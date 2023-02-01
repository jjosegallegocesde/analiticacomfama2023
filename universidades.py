#importo a pandas
import pandas as pd 

#traigo la fuente de datos
edadesCasa1=[25,25,25,25,25]
edadesCasa2=[1,4,24,27,70]

# genero lo dataframes
dataframe1=pd.DataFrame(edadesCasa1)
dataframe2=pd.DataFrame(edadesCasa2)

#analisis descriptivo de los datos
analisis1=dataframe1.describe()
analisis2=dataframe2.describe()

#mostrar resultados
print(analisis1)
print(analisis2)


