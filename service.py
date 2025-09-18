from repository import ClientRepository
from flight import Client

class ClientService:
    def __init__(self,repository:ClientRepository):
        self.repository = repository

    def create_flight(self, flight:Client):
        """Добавление клиента"""
        return self.repository.create_client(flight)
    
    def get_all(self):
        '''Получить всех клиентов'''
        return self.repository.get_all()
        
    def get_by_id(self,client_id:int):
        '''Получить полёт по id'''
        return self.repository.get_by_id(client_id)
    
    def update_client(self, flight:Client):
        """Изменить существующего клиента. 
            Если клиента не существует, ничего не делать."""
        return self.repository.update_client(flight)
    
    def delete_client(self,Client_id:int):
        """Удалить существующего клиента.
            Если клиента не существует, ничего не делать."""
        return self.repository.delete_client(Client_id)