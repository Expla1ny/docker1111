from flight import Client
from database import DatabaseConnection


class ClientRepository:
    '''Класс-репозиторий для доступа к БД'''

    def __init__(self,connection: DatabaseConnection):
        self.connection=connection

    def create_flight(self, flight:Client):
        """Добавление клиента"""

        conn = self.connection.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO clients
                        (name,passnum)
                        VALUES (%s,%s)
            ''',(flight.name,flight.passnum))
        conn.commit()

        cursor.close()
        conn.close()

        return flight
    
    def get_all(self):
        conn = self.connection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients ORDER BY id")
        rows = cursor.fetchall()

        Clients = []
        for row in rows:
            Clients.append(Client(
                row[0],
                row[1],
                row[2]
            ))
              
        cursor.close()
        conn.close()
        return Clients
        
    def get_by_id(self,client_id:int):
        """Получить клиента по идентификатору"""
        conn = self.connection.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM clients WHERE id = %s",(client_id,))
        row = cursor.fetchone()
        
        cursor.close()
        conn.close()

        if row:
            return Client(
                row[0],
                row[1],
                row[2]
            )
        return None
    
    def update_client(self, flight:Client):
        """Изменить существующего клиента. 
            Если клиента не существует, ничего не делать."""
        conn = self.connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE clients
            SET name = %s, passnum = %s
            WHERE id = %s
            ''',(flight.name, flight.passnum, flight.id))
        
        result = cursor.fetchone()
        flight.id = result[0]
        conn.commit()

        cursor.close()
        conn.close()

        return flight
    
    def delete_client(self,client_id:int):
        """Удалить существующего клиента.
            Если клиента не существует, ничего не делать."""
        conn = self.connection.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM clients WHERE id = %s
            ''',(client_id,))
        conn.commit()
        deleted = cursor.rowcount

        cursor.close()
        conn.close()

        return deleted >0

