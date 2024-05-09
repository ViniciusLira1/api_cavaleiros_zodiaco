from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.modelCavaleiros import CavaleirosModel
from models.modelInimigosCavaleiros import InimigosCavaleirosModel
from schemas.cavaleiros_schema import CavaleirosSchema
from schemas.inimigos_cavaleiros_schema import InimigosCavaleirosSchema
from core.deps import get_session

router = APIRouter()

@router.get("/",response_model=List[CavaleirosSchema])
async def get_cavaleiros(db:AsyncSession = Depends(get_session)):
    async with db as session :
        query = select(CavaleirosModel)
        result = await session.execute(query)
        cavaleiros : list[CavaleirosModel] = result.scalars().all()
        return cavaleiros
    

@router.get("/{cavaleiro_id}",response_model=CavaleirosSchema,status_code=status.HTTP_200_OK)
async def get_cavaleiro(cavaleiro_id:int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CavaleirosModel).filter(CavaleirosModel.id==cavaleiro_id)
        result= await session.execute(query)
        cavaleiro = result.scalar_one_or_none()
        
        if cavaleiro:
            return cavaleiro
        else:
            raise HTTPException(detail="Cavaleiro nao encontrado",status_code=status.HTTP_404_NOT_FOUND)
        
        
@router.get("/cavaleiro-inimigo/{cavaleiro_id}",status_code=status.HTTP_200_OK,response_model=list[InimigosCavaleirosSchema])
async def get_inimigo_cavaleiro(cavaleiro_id:int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InimigosCavaleirosModel).filter(InimigosCavaleirosModel.id_cavaleiro==cavaleiro_id)
        result= await session.execute(query)
        inimigos: list[InimigosCavaleirosModel] = result.scalars().all()
        
        if inimigos:
            return inimigos
        else:
            raise HTTPException(detail="Cavaleiro nao encontrado",status_code=status.HTTP_404_NOT_FOUND)
        
        
        
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=CavaleirosSchema)
async def post_cavaleiro(cavaleiro:CavaleirosSchema,db:AsyncSession = Depends(get_session)):
    novo_cavaleiro= CavaleirosModel(nome=cavaleiro.nome, signo = cavaleiro.signo,armadura=cavaleiro.armadura,poder_especial=cavaleiro.poder_especial,url=cavaleiro.url)
    db.add(novo_cavaleiro)
    await db.commit()
    return novo_cavaleiro


@router.put("/{cavaleiro_id}",status_code=status.HTTP_202_ACCEPTED,response_model=CavaleirosSchema)
async def put_cavaleiro(cavaleiro_id,cavaleiro:CavaleirosSchema,db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CavaleirosModel).filter(CavaleirosModel.id == cavaleiro_id)
        result = await session.execute(query)
        cavaleiro_up=result.scalar_one_or_none()
        
        if cavaleiro_up:
            cavaleiro_up.nome = cavaleiro.nome
            cavaleiro_up.signo = cavaleiro.signo
            cavaleiro_up.armadura=cavaleiro.armadura
            cavaleiro_up.poder_especial=cavaleiro.poder_especial
            cavaleiro_up.url=cavaleiro.url
            
            await session.commit()
            return cavaleiro_up
        else:
             raise HTTPException(detail="Cavaleiro nao encontrado",status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{cavaleiro_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_cavaleiro(cavaleiro_id,db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CavaleirosModel).filter(CavaleirosModel.id == cavaleiro_id)
        result = await session.execute(query)
        cavaleiro_del=result.scalar_one_or_none()
        
        if cavaleiro_del:
            await session.delete(cavaleiro_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Cavaleiro nao encontrado",status_code=status.HTTP_404_NOT_FOUND)