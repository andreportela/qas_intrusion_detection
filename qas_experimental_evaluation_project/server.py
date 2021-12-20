import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import datetime


class MedicalRecord(BaseModel):
    name: str
    blood_pressure: int
    sugar_level: int

app = FastAPI()

@app.post("/")
def upload_medical_record(record: MedicalRecord) -> MedicalRecord:
    folder_prefix = "medical_records/"
    file_name = "".join([folder_prefix, str(datetime.datetime.now())])
    with open(file_name, mode='w') as f:
        content = str(record.dict())
        f.write(content)
    return record

def start():
    uvicorn.run("qas_experimental_evaluation_project.server:app", host="0.0.0.0", port=8000, reload=True)
