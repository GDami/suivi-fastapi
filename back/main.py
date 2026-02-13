from datetime import datetime
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
    applications: list["Application"] = Relationship(back_populates="offer")

class Application(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    date: datetime
    offer_id: int | None = Field(default=None, foreign_key="offer.id")
    offer: Offer = Relationship(back_populates="applications")
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

## Offers

# Create a new offer
@app.post("/offers/", response_model=Offer)
async def create_offer(
    offer: Offer,
    session: Session = Depends(get_session)
):
    session.add(offer)
    session.commit()
    session.refresh(offer)
    return offer

# Read all offers
@app.get("/offers/")
async def get_offers(
    skip: int = 0,
    limit: int = 10,
    session: Session = Depends(get_session)
):
    offers = session.exec(select(Offer).offset(skip).limit(limit)).all()
    return offers

# Read a single offer
@app.get("/offers/{offer_id}", response_model=Offer)
async def get_offer(
    offer_id: int,
    session: Session = Depends(get_session)
):
    offer = session.get(Offer, offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer

# Update an offer
@app.put("/offers/{offer_id}", response_model=Offer)
async def update_offer(
    offer_id: int,
    offer_data: Offer,
    session: Session = Depends(get_session)
):
    offer = session.get(Offer, offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    
    for key, value in offer_data.model_dump().items():
        setattr(offer, key, value)
    
    session.commit()
    session.refresh(offer)
    return offer

# Delete an offer
@app.delete("/offers/{offer_id}")
async def delete_offer(
    offer_id: int,
    session: Session = Depends(get_session)
):
    offer = session.get(Offer, offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    
    session.delete(offer)
    session.commit()
    return offer

## Applications

# Create a new application
@app.post("/applications/", response_model=Application)
async def create_application(
    application: Application,
    session: Session = Depends(get_session)
):
    application.date = datetime.now()
    session.add(application)
    session.commit()
    session.refresh(application)
    return application

# Read all applications
@app.get("/applications/")
async def get_applications(
    skip: int = 0,
    limit: int = 10,
    session: Session = Depends(get_session)
):
    applications = session.exec(select(Application).offset(skip).limit(limit)).all()
    return applications

# Read a single application
@app.get("/applications/{application_id}", response_model=Application)
async def get_application(
    application_id: int,
    session: Session = Depends(get_session)
):
    application = session.get(Application, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

# Update an application
@app.put("/applications/{application_id}", response_model=Application)
async def update_application(
    application_id: int,
    application_data: Application,
    session: Session = Depends(get_session)
):
    application = session.get(Application, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    for key, value in application_data.model_dump().items():
        setattr(application, key, value)
    
    session.commit()
    session.refresh(application)
    return application

# Delete an application
@app.delete("/applications/{application_id}")
async def delete_application(
    application_id: int,
    session: Session = Depends(get_session)
):
    application = session.get(Application, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    session.delete(application)
    session.commit()
    return application

## CVs

# TODO : CRUD for CVs
# Read should return the file path to the CV, and the name of the CV. The file itself will be stored in a folder on the server, and the path will be used to access it. The name will be used to display the CV in the frontend.