from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CavaleirosSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    signo: str 
    armadura:str 
    poder_especial: str 
    url : str 
    
    class Config:
        orm_mode = True