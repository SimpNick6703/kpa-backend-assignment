from sqlalchemy import Column, Integer, String, JSON
from pydantic import BaseModel
from typing import Optional, Dict, Any
from .database import Base

# SQLAlchemy model for the database table
class WheelSpecificationDB(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, index=True, nullable=False)
    submittedBy = Column(String, index=True)
    submittedDate = Column(String)
    fields = Column(JSON)

# Pydantic model for the POST request body fields
class WheelSpecFields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str

# Pydantic model for the POST request body
class WheelSpecCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: WheelSpecFields

# Pydantic model for the GET response
class WheelSpecOut(BaseModel):
    id: int
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: Dict[str, Any]

    class Config:
        from_attributes = True
