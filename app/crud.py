from sqlalchemy.orm import Session
from . import models

def create_wheel_specification(db: Session, spec: models.WheelSpecCreate):
    db_spec = models.WheelSpecificationDB(
        formNumber=spec.formNumber,
        submittedBy=spec.submittedBy,
        submittedDate=spec.submittedDate,
        fields=spec.fields.dict()
    )
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec

def get_wheel_specification_by_form_number(db: Session, form_number: str):
    return db.query(models.WheelSpecificationDB).filter(models.WheelSpecificationDB.formNumber == form_number).first()

def get_wheel_specifications(db: Session, formNumber: str = None, submittedBy: str = None, submittedDate: str = None, skip: int = 0, limit: int = 100):
    query = db.query(models.WheelSpecificationDB)
    if formNumber:
        query = query.filter(models.WheelSpecificationDB.formNumber == formNumber)
    if submittedBy:
        query = query.filter(models.WheelSpecificationDB.submittedBy == submittedBy)
    if submittedDate:
        query = query.filter(models.WheelSpecificationDB.submittedDate == submittedDate)
    return query.offset(skip).limit(limit).all()
