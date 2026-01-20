from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "AI CRM Backend is running"}

@app.post("/chat", response_model=schemas.ChatResponse)
def chat(request: schemas.ChatRequest, db: Session = Depends(get_db)):
    interaction = models.Interaction(
        hp_name=request.hp_name,
        specialty=request.specialty,
        notes=request.notes
    )
    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    reply = f"Logged interaction with {request.hp_name} ({request.specialty}): {request.notes}"
    return {"reply": reply}

@app.get("/interactions", response_model=list[schemas.InteractionOut])
def get_interactions(db: Session = Depends(get_db)):
    return db.query(models.Interaction).all()
