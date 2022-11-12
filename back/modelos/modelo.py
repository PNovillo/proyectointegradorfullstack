#SPRINT 2 BACKEND - OPERACIONES DE CRUD
 
import mysql.connector

class conectar():
    
    def __init__(self) -> None:
        
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port='3306',
                database='db_smartlab',
                user='root',
                password='',                                   
                
            )
        except  mysql.connector.Error as descripcionError:
            print("No se conecto",descripcionError)
            
     
#OPERACION DE CRUD: INSERT 
def insertValor(self,id, analisis,dni,hc,fecha_analisis,fecha_retiro):
            if self.conexion.is_connected():
                try:
                    cursor= self.conexion.cursor()
                    sentenciaSQL= "INSERT INTO tipo_analisis VALUES (%s, %s, %s, %s, %s, %s)"
                    data= (id, analisis, dni, hc, fecha_analisis, fecha_retiro)


                    cursor.execute(sentenciaSQL,data)
                    self.conexion.commit()
                    self.conexion.close
          
                except:
                    print("No se pudo conectar a la base de datos")

#SEGUNDA OPERACION DE CRUD: READ O LEER

def BuscarObjeto(self, fecha_analisis):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sentenciaSQL = "SELECT * from tipo_analisis where fecha_analisis like '%MAR%'"
                    cursor.execute(sentenciaSQL)
                    resultadoREAD = cursor.fetchall()
                  
               
            
                except:
                   print("No se pudo conectar a la base de datos")