from core.config import settings
from sqlalchemy import Column,INTEGER,String

class CavaleirosModel(settings.DBBaseModel):
    __tablename__ ='Cavaleiros_Zodiaco'
    
    id: int = Column(INTEGER(), primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    signo: str = Column(String(50))
    armadura: str = Column(String(50))
    poder_especial: str = Column(String(50))
    url : str = Column(String(255))
    
    
    
    