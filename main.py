from database import DatabaseConfig, DatabaseConnection
from migrations import MigrationManager
from repository import ClientRepository
from service import ClientService
from fastapi import FastAPI, HTTPException
from client import Client

#Initialize
## DB config
db_config= DatabaseConfig(
    'flightsdb',
    'postgres',
    'postgres',
    '123Secret_a',
    5432
)
db_connection = DatabaseConnection(db_config)
## Migrations
migration_manager = MigrationManager(db_config)
migration_manager.create_tables()
# Repository and Service
repository = ClientRepository(db_connection)
service = ClientService(repository)

app = FastAPI(
    title="BankAPI"
)

@app.get("/")
async def root():
    return {"message":"Hello from FastAPI"}

@app.get("/clients")
async def get_clients():
    try:
        return service.get_all()
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Ошибка при получении клиентов: {str(e)}")

@app.post("/clients")
async def create_client(client_data: dict):
    try:
        #Validation
        required_fields = ["name","passnum"]
        for field in required_fields:
            if field not in client_data:
                raise HTTPException(status_code=400,detail=f"Отсутствует обязательное поле {field}")
        
        client = Client(
            name=client_data['name'],
            passnum=client_data['passnum']
        )

        created_client = service.create_client(Client)
        return created_client

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Ошибка при добавлении клиента: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0", port=8080)


