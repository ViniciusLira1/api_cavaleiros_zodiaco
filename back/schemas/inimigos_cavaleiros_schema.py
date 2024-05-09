from typing import Optional
from pydantic import BaseModel as SCBaseModel

class InimigosCavaleirosSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    signo: str 
    armadura:str 
    poder_especial: str 
    url : str 
    id_cavaleiro: int
    
    
    class Config:
        orm_mode = True