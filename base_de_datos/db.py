#Conexion a la base de datos
import mysql.connector
import datetime
from .config import DB_HOST,DB_USER,DB_PASSWORD,DB_NAME

# Conexion a la base de datos
def conection_db():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error de conexion:{err}")

# Obtencion del año en tiempo real
def get_year_now():
    now = datetime.datetime.now()
    return str(now.year)


def create_database():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conexion.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        print(f"Base de datos '{DB_NAME}' creada exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al crear la base de datos: {err}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def create_table_estudiantes():
    conexion = conection_db()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(50) NOT NULL,
        year VARCHAR(10),
        date_of_birth VARCHAR(50),
        age VARCHAR(10) NOT NULL,
        document VARCHAR(20) UNIQUE,
        document_type VARCHAR(20),
        grade VARCHAR(50) NOT NULL,
        blood_type VARCHAR(10) NOT NULL,
        eps VARCHAR(50) NOT NULL,
        allergy VARCHAR(50),
        emergency_number VARCHAR(20),
        father VARCHAR(50),
        father_profession VARCHAR(50),
        father_number VARCHAR(20),
        father_address VARCHAR(30),
        father_cc VARCHAR(20),
        mother VARCHAR(50),
        mother_profession VARCHAR(50),
        mother_number VARCHAR(20),
        mother_address VARCHAR(30),
        mother_cc VARCHAR(20),
        guardian VARCHAR(50),
        guardian_profession VARCHAR(50),
        guardian_number VARCHAR(20),
        guardian_address VARCHAR(30),
        guardian_cc VARCHAR(20)
    );
    ''')
    conexion.commit()
    conexion.close()


def add_student(name, year,age,  date_of_birth, blood_type, eps, document, document_type, grade, allergy, emergency_number, father, father_profession, father_number, father_address, father_cc, mother, mother_profession, mother_number, mother_address, mother_cc, guardian, guardian_profession, guardian_number, guardian_address, guardian_cc):
    conexion = conection_db()
    cursor = conexion.cursor()
    year_now = get_year_now()
    consulta = '''
    INSERT INTO estudiantes (name, year,age, date_of_birth, blood_type, eps, document, document_type, grade, allergy, emergency_number, father, father_profession, father_number, father_address, father_cc, mother, mother_profession, mother_number, mother_address, mother_cc, guardian, guardian_profession, guardian_number, guardian_address, guardian_cc)
    VALUES (%s, %s,%s,%s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    '''
    datos = (name, year_now,age,  date_of_birth, blood_type, eps, document, document_type, grade, allergy, emergency_number, father, father_profession, father_number, father_address, father_cc, mother, mother_profession, mother_number, mother_address, mother_cc, guardian, guardian_profession, guardian_number, guardian_address, guardian_cc)
    cursor.execute(consulta, datos)
    conexion.commit()
    conexion.close()


def get_all_students():
    conexion = conection_db()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM estudiantes')
    estudiantes = cursor.fetchall()
    conexion.close()
    return estudiantes

estudiantes = get_all_students()
for estudiante in estudiantes:
    print(estudiante)


# ------------------------------- Revisar por validacion-----------------------
# def edit_student(id_student, name, year):
#     conexion = conection_db()
#     cursor = conexion.cursor()
#     consulta = "UPDATE estudiantes SET name= %s, year= %s WHERE id=%s"
#     datos = (name, year, id_student)
#     cursor.execute(consulta,datos)
#     conexion.commit()
#     conexion.close()

def delet_student(id_student):
    conexion = conection_db()
    cursor = conexion.cursor()
    consulta = "DELETE FROM estudiantes WHERE id=%s"
    datos = (id_student,)
    cursor.execute(consulta,datos)
    conexion.commit()
    conexion.close()

def filter_year(year):
    conexion = conection_db()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM estudiantes WHERE year=%s"
    datos=(year,)
    cursor.execute(consulta,datos)
    estudiantes = cursor.fetchall()
    conexion.close()
    return estudiantes

def filter_name(name):
    conexion = conection_db()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM estudiantes WHERE name LIKE %s"
    datos = ("%" + name + "%",)
    cursor.execute(consulta,datos)
    estudiantes = cursor.fetchall()
    conexion.close()
    return estudiantes





# ----------- Mensualidades ------------------------------
def create_table_mensualidades():
    conexion = conection_db()
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mensualidades (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_estudiante INT,
        mes VARCHAR(20),
        monto DECIMAL(10, 2),
        FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id)
    )
    ''')
    conexion.commit()
    conexion.close()


def add_mensualidad(id_estudiante, mes, monto):
    conexion = conection_db()
    cursor = conexion.cursor()
    consulta = '''
    INSERT INTO mensualidades (id_estudiante, mes, monto)
    VALUES (%s, %s, %s)
    '''
    datos = (id_estudiante, mes, monto)
    cursor.execute(consulta, datos)
    conexion.commit()
    conexion.close()

# Todas las mensualidades---------------------------------------------------
def get_all_mensualidades():
    conexion = conection_db()
    cursor = conexion.cursor()
    consulta = '''
    SELECT m.id, e.name AS student_name, m.mes, m.monto
    FROM mensualidades m
    JOIN estudiantes e ON m.id_estudiante = e.id
    '''
    cursor.execute(consulta)
    mensualidades = cursor.fetchall()

    conexion.close()
    return mensualidades

# Traer las mensualidades segun id
def get_mensualidad(id_estudiante):
    conexion = conection_db()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM mensualidades WHERE id_estudiante = %s"
    datos = (id_estudiante,)
    cursor.execute(consulta, datos)
    mensualidades = cursor.fetchall()
    conexion.close()
    return mensualidades

def edit_mensualidad(id_pago, mes, monto):
    conexion = conection_db()
    cursor = conexion.cursor()
    consulta = "UPDATE mensualidades SET mes = %s, monto = %s WHERE id = %s"
    datos = (mes, monto, id_pago)
    cursor.execute(consulta, datos)
    conexion.commit()
    conexion.close()

def delete_mensualidad(id_pago):
    conexion = conection_db()
    cursor = conexion.cursor()
    consulta = "DELETE FROM mensualidades WHERE id = %s"
    datos = (id_pago,)
    cursor.execute(consulta, datos)
    conexion.commit()
    conexion.close()



