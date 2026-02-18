
from datetime import datetime
from enum import Enum
from sqlmodel import Field, Relationship, SQLModel


# Define models
class Company(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    name: str
    link: str | None = None
    offers: list["Offer"] = Relationship(back_populates="company")

class Offer(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    link: str
    title: str
    description: str
    company_id: int | None = Field(default=None, foreign_key="company.id")
    company: Company = Relationship(back_populates="offers")
    applications: list["Application"] = Relationship(back_populates="offer")

class ApplicationStatus(Enum):
    APPLIED = "Applied"
    INTERVIEWING = "Interviewing"
    REJECTED = "Rejected"
    ACCEPTED = "Accepted"

class Application(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    date_applied: datetime
    status: ApplicationStatus = Field(default=ApplicationStatus.APPLIED)
    notes: str | None = None
    offer_id: int | None = Field(default=None, foreign_key="offer.id")
    offer: Offer = Relationship(back_populates="applications")
    cv_id: int | None = Field(default=None, foreign_key="cv.id")
    cv: "CV" = Relationship(back_populates="applications")

class CV(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    name: str
    path: str
    applications: list[Application] = Relationship(back_populates="cv")

class ApplicationListResponse():
    id: int
    date_applied: datetime
    status: ApplicationStatus
    notes: str | None
    offer_id: int | None
    offer_title: str | None
    company_name: str | None
