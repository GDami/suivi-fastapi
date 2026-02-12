from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select, Relationship

# Define models
class Company(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    name: str
    link: str | None = None
    offers: list["Offer"] = Relationship(back_populates="company")

class Offer(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    link: str
    titre: str
    description: str
    company_id: int | None = Field(default=None, foreign_key="company.id")
    company: Company = Relationship(back_populates="offers")
    application_id: int | None = Field(default=None, foreign_key="application.id")

class Application(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    date: str
    offer_id: int | None = Field(default=None, foreign_key="offer.id")
    cv_id: int | None = Field(default=None, foreign_key="cv.id")
    cv: "CV" = Relationship(back_populates="applications")

class CV(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    name: str
    path: str
    applications: list[Application] = Relationship(back_populates="cv")


# FastAPI app
app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(engine)

# Dependency to get DB session
def get_session():
    with Session(engine) as session:
        yield session

### Endpoints

## Companies

# Create a new company
@app.post("/companies/", response_model=Company)
async def create_company(
    company: Company,
    session: Session = Depends(get_session)
):
    session.add(company)
    session.commit()
    session.refresh(company)
    return company

# Read all companies
@app.get("/companies/")
async def get_companies(
    skip: int = 0,
    limit: int = 10,
    session: Session = Depends(get_session)
):
    companies = session.exec(select(Company).offset(skip).limit(limit)).all()
    return companies

# Read a single company
@app.get("/companies/{company_id}", response_model=Company)
async def get_company(
    company_id: int,
    session: Session = Depends(get_session)
):
    company = session.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

# Update a company
@app.put("/companies/{company_id}", response_model=Company)
async def update_company(
    company_id: int,
    company_data: Company,
    session: Session = Depends(get_session)
):
    company = session.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    for key, value in company_data.model_dump().items():
        setattr(company, key, value)
    
    session.commit()
    session.refresh(company)
    return company

# Delete a company
@app.delete("/companies/{company_id}")
async def delete_company(
    company_id: int,
    session: Session = Depends(get_session)
):
    company = session.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    session.delete(company)
    session.commit()
    return company