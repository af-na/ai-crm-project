from pydantic import BaseModel

class ChatRequest(BaseModel):
    hp_name: str
    specialty: str
    notes: str

class ChatResponse(BaseModel):
    reply: str

class InteractionOut(BaseModel):
    id: int
    hp_name: str
    specialty: str
    notes: str

    class Config:
        orm_mode = True
