from datetime import datetime

from fastapi import FastAPI, APIRouter, HTTPException
from configurations import collection
from src.database.schemas import all_data
from src.database.models import Incident
from bson.objectid import ObjectId
app= FastAPI()
router = APIRouter()




@app.get("/health")
async def health():
    return {"message": "our incidents api is working"}



@app.get("/")
async def get_all_incidents():
    data = collection.find({"is_deleted": False})
    return  all_data(data)


@router.post("/")
async def create_incident(new_incident: Incident):
    try:
        response  = collection.insert_one(dict(new_incident))
        return {"status_code": 200  , "message": "Incident created successfully", "id": str(response.inserted_id)}
    except Exception as error:
        return HTTPException(status_code=500, detail=f"Error creating incident: {error}")


@router.put("/{task_id}")
async def update_incident(task_id : str , updated_task:Incident):
    try:
        id = ObjectId(task_id)
        existing_incident = collection.find_one({"_id": id, "is_deleted": False})
        if not existing_incident:
            return HTTPException(status_code=404, detail="Incident not found in teh collections")
        updated_task.updated_at = int(datetime.timestamp(datetime.now()))
        response = collection.update_one({"_id": id }, {"$set" : dict(updated_task) })
        return {"status_code": 200, "message": "Incident updated successfully", "id": str(response.upserted_id)}

    except Exception as error:
        return HTTPException(status_code=500, detail=f"Error creating incident: {error}")

@router.delete("/{task_id}")
async def delete_incident(task_id: str ):
    try:
        id = ObjectId(task_id)
        existing_incident = collection.find_one({"_id": id, "is_deleted": False})
        if not existing_incident:
            return HTTPException(status_code=404, detail="Incident not found in teh collections")
        resp = collection.update_one({"_id": id}, {"$set": {"is_deleted" : True} })
        return {"status_code": 200, "message": "Incident - Soft deleted successfully", "id": str(resp.upserted_id)}
    except Exception as error:
        return HTTPException(status_code=500, detail=f"Error creating incident: {error}")

app.include_router(router)