from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from . import crud, models, database

# Create all database tables
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="KPA Form Data API",
    description="Implementation of the KPA backend assignment.",
    version="1.0.0",
)

@app.post("/api/forms/wheel-specifications", status_code=201)
def create_wheel_spec(spec: models.WheelSpecCreate, db: Session = Depends(database.get_db)):
    # Check if form number already exists
    db_spec = crud.get_wheel_specification_by_form_number(db, form_number=spec.formNumber)
    if db_spec:
        raise HTTPException(status_code=400, detail="Form number already registered")
    
    # Create the wheel specification
    crud.create_wheel_specification(db=db, spec=spec)
    
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": spec.formNumber,
            "submittedBy": spec.submittedBy,
            "submittedDate": spec.submittedDate,
            "status": "Saved"
        }
    }

@app.get("/api/forms/wheel-specifications")
def read_wheel_specs(
    formNumber: Optional[str] = None,
    submittedBy: Optional[str] = None,
    submittedDate: Optional[str] = None,
    db: Session = Depends(database.get_db)
):
    specs = crud.get_wheel_specifications(
        db, formNumber=formNumber, submittedBy=submittedBy, submittedDate=submittedDate
    )
    if not specs:
        raise HTTPException(status_code=404, detail="No forms found with the given criteria")
        
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": [
            {
                "formNumber": spec.formNumber,
                "submittedBy": spec.submittedBy,
                "submittedDate": spec.submittedDate,
                "fields": spec.fields
            } for spec in specs
        ]
    }

@app.get("/")
def root():
    return {"message": "KPA API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "API is running successfully"}
