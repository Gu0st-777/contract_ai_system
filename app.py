
from fastapi import FastAPI, UploadFile
import shutil, os
from agents.coordinator import CoordinatorAgent

app = FastAPI()
coordinator = CoordinatorAgent()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/review_contract")
async def review_contract(file: UploadFile):
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = coordinator.run(file_path)
    return {"status": "success", "result": result}
