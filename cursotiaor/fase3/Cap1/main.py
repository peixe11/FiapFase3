import cx_Oracle
from datetime import datetime

dsn = cx_Oracle.makedsn("ORACLE.FIAP.COM.BR", 1521, service_name="ORCL")
connection = cx_Oracle.connect(user="RM560401", password="180206", dsn=dsn)

def inserir_leitura_sensor(tipo_sensor, valor):
    cursor = connection.cursor()
    sql = """
        INSERT INTO Sensores (tipo_sensor, valor)
        VALUES (:tipo_sensor, :valor)
    """
    cursor.execute(sql, [tipo_sensor, valor])
    connection.commit()
    print(f"Leitura do sensor {tipo_sensor} inserida com valor {valor}.")

def registrar_irrigacao(status):
    cursor = connection.cursor()
    sql = """
        INSERT INTO Irrigacao (status)
        VALUES (:status)
    """
    cursor.execute(sql, [status])
    connection.commit()
    print(f"Irrigação {status} registrada.")

def registrar_historico(id_sensor, id_irrigacao):
    cursor = connection.cursor()
    sql = """
        INSERT INTO Historico_Irrigacao (id_sensor, id_irrigacao)
        VALUES (:id_sensor, :id_irrigacao)
    """
    cursor.execute(sql, [id_sensor, id_irrigacao])
    connection.commit()
    print("Histórico de irrigação registrado.")

def consultar_historico():
    cursor = connection.cursor()
    sql = """
        SELECT h.data_registro, s.tipo_sensor, s.valor, i.status
        FROM Historico_Irrigacao h
        JOIN Sensores s ON h.id_sensor = s.id_sensor
        JOIN Irrigacao i ON h.id_irrigacao = i.id_irrigacao
        ORDER BY h.data_registro DESC
    """
    cursor.execute(sql)
    for row in cursor:
        print(f"Data: {row[0]}, Sensor: {row[1]}, Valor: {row[2]}, Status Irrigação: {row[3]}")
    cursor.close()

def atualizar_leitura_sensor(id_sensor, novo_valor):
    cursor = connection.cursor()
    sql = """
        UPDATE Sensores
        SET valor = :novo_valor
        WHERE id_sensor = :id_sensor
    """
    cursor.execute(sql, [novo_valor, id_sensor])
    connection.commit()
    print(f"Leitura do sensor ID {id_sensor} atualizada para valor {novo_valor}.")

def deletar_historico(id_historico):
    cursor = connection.cursor()
    sql = """
        DELETE FROM Historico_Irrigacao
        WHERE id_historico = :id_historico
    """
    cursor.execute(sql, [id_historico])
    connection.commit()
    print(f"Registro de histórico ID {id_historico} deletado.")



inserir_leitura_sensor("Umidade", 55)         

registrar_irrigacao("Ligado")

registrar_historico(id_sensor=1, id_irrigacao=1)

atualizar_leitura_sensor(1,60)

deletar_historico(1)

consultar_historico()



connection.close()
