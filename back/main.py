from datetime import datetime
from enum import Enum
from typing import Literal, Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlmodel import SQLModel, Session, create_engine, select

from models import ApplicationListResponse, Company, Offer, Application, CV, ApplicationStatus

# FastAPI app
app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Database setup
# DATABASE_URL = "sqlite:///./database.db"
DATABASE_URL = "postgresql+psycopg2://postgres:gregre123@localhost:5432/suivi-db"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine)

# Dependency to get DB session
def get_session():
    with Session(engine) as session:
        yield session

### Endpoints

class SortOrder(Enum):
    ASCENDING = 1
    DESCENDING = 2

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
    print(companies)
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
        if value is not None:
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

class ApplicationSortBy(str, Enum):
    OFFER_TITLE = "offer_title"
    COMPANY = "company"
    DATE_APPLIED = "date_applied"

def populate_application_response(application: Application) -> ApplicationListResponse:
    response: ApplicationListResponse = {
        **application.__dict__,
        "offer_title" : application.offer.title if application.offer else None,
        "offer_link" : application.offer.link if application.offer else None,
        "company_name" : application.offer.company.name if application.offer and application.offer.company else None
    }
    return response

# Get applications with filters and sorting
@app.get("/applications/")
async def get_applications(
    skip: int = 0,
    limit: int = 10,
    query: Optional[str] = None,
    # sort_by: Optional[ApplicationSortBy] = None,
    sort_by: Optional[ApplicationSortBy] = Query(None),
    sort_order: Optional[str] = "asc",
    session: Session = Depends(get_session)
):
    applications_query = select(Application)
    
    if query or sort_by == ApplicationSortBy.OFFER_TITLE:
        applications_query = applications_query.join(Offer)

    if query:
        applications_query = applications_query.where(
            Offer.title.contains(query) | Application.notes.contains(query)
        )
    
    if sort_by:

        match sort_by:
            case ApplicationSortBy.OFFER_TITLE:
                applications_query = applications_query.order_by(
                    Offer.title.asc() if sort_order == "asc" else Offer.title.desc()
            )
            case ApplicationSortBy.COMPANY:
                applications_query = applications_query.join(Company).order_by(
                    Company.name.asc() if sort_order == "asc" else Company.name.desc()
            )
            case ApplicationSortBy.DATE_APPLIED:
                applications_query = applications_query.order_by(
                    Application.date_applied.asc() if sort_order == "asc" else Application.date_applied.desc()
            )
    
    applications = session.exec(
        applications_query.offset(skip).limit(limit)
    ).all()
    applications = list(map(populate_application_response, applications))
    return applications
    

# Create a new application
@app.post("/applications/", response_model=Application)
async def create_application(
    application: Application,
    session: Session = Depends(get_session)
):
    application.date_applied = datetime.now()
    application.status = ApplicationStatus.APPLIED
    session.add(application)
    session.commit()
    session.refresh(application)
    return application

# Read all applications
# @app.get("/applications/")
# async def get_applications(
#     skip: int = 0,
#     limit: int = 10,
#     session: Session = Depends(get_session)
# ):
#     applications = session.exec(select(Application).offset(skip).limit(limit)).all()
#     return applications

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
        if value is not None:
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