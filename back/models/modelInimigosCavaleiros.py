from core.config import settings
from sqlalchemy import Column,INTEGER,String,ForeignKey
from sqlalchemy.orm import relationship

class InimigosCavaleirosModel(settings.DBBaseModel):
    __tablename__ ='Inimigos_Cavaleiros'

    id: int = Column(INTEGER, primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    signo: str = Column(String(50))
    armadura: str = Column(String(50))
    poder_especial: str = Column(String(50))
    url : str = Column(String(255))
    id_cavaleiro: int = Column(INTEGER,ForeignKey('Cavaleiros_Zodiaco.id'))
    
    # Relacionamento com a tabela CavaleirosModel
    cavaleiro = relationship("CavaleirosModel")