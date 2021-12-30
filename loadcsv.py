import pandas as pd
import pymysql as mysql

path = 'C:/Users/Gorka/Downloads/casos_tecnica_ccaa.csv'
data = pd.read_csv(path)

print("CSV Data: \n")
print(type(data))
# print(data.shape[0])
for act in data:
    print(act)

# ccaa_iso,fecha,num_casos,num_casos_prueba_pcr,num_casos_prueba_test_ac,num_casos_prueba_ag,num_casos_prueba_elisa,num_casos_prueba_desconocida


try:
    conexion = mysql.connect(host='localhost',
                             user='root',
                             password='Ikerbasauri0718',
                             db='covid')
    try:
        with conexion.cursor() as cursor:
            for i in data.index:
                act = data.iloc[i]

                query = "INSERT INTO `covid`.`datos` (`ccaa_iso`, `fecha`, `num_casos`, `num_casos_prueba_pcr`, `num_casos_prueba_test_ac`, `num_casos_prueba_ag`, `num_casos_prueba_elisa`, `num_casos_prueba_desconocida`) VALUES ('"+str(act['ccaa_iso'])+"', '"+str(act['fecha'])+"', '"+str(act['num_casos'])+"', '"+str(act['num_casos_prueba_pcr'])+"', '"+str(act['num_casos_prueba_test_ac'])+"', '"+str(act['num_casos_prueba_ag'])+"', '"+str(act['num_casos_prueba_elisa'])+"', '"+str(act['num_casos_prueba_desconocida'])+"');"
                cursor.execute(query)

        conexion.commit()
    finally:
        conexion.close()
except (mysql.err.OperationalError, mysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)
