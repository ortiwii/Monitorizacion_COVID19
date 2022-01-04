import pymysql as mysql
try:
    conexion = mysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='covid')
    try:
        with conexion.cursor() as cursor:

                try:
                    query = "INSERT INTO `covid`.`datos` (`ccaa_iso`, `fecha`, `num_casos`, `num_casos_prueba_pcr`, `num_casos_prueba_test_ac`, `num_casos_prueba_ag`, `num_casos_prueba_elisa`, `num_casos_prueba_desconocida`) VALUES ('"+str(act['ccaa_iso'])+"', '"+str(act['fecha'])+"', '"+str(act['num_casos'])+"', '"+str(act['num_casos_prueba_pcr'])+"', '"+str(act['num_casos_prueba_test_ac'])+"', '"+str(act['num_casos_prueba_ag'])+"', '"+str(act['num_casos_prueba_elisa'])+"', '"+str(act['num_casos_prueba_desconocida'])+"');"
                    cursor.execute(query)
                except mysql.err.IntegrityError as e:
                    pass
        conexion.commit()
    finally:
        conexion.close()
except (mysql.err.OperationalError, mysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)
