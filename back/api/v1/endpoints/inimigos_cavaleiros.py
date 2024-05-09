from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from models.modelInimigosCavaleiros import InimigosCavaleirosModel
from schemas.inimigos_cavaleiros_schema import InimigosCavaleirosSchema
from core.deps import get_session

router = APIRouter()

@router.get("/",response_model=List[InimigosCavaleirosSchema])
async def get_cavaleiros(db:AsyncSession = Depends(get_session)):
    async with db as session :
        query = select(InimigosCavaleirosModel)
        result = await session.execute(query)
        inimigos_cavaleiros: list[InimigosCavaleirosModel] = result.scalars().all()
        return inimigos_cavaleiros

@router.get("/{inimigos_cavaleiros}",response_model=InimigosCavaleirosSchema,status_code=status.HTTP_200_OK)
async def get_cavaleiro(inimigos_cavaleirosId:int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InimigosCavaleirosModel).filter(InimigosCavaleirosModel.id==inimigos_cavaleirosId)
        result= await session.execute(query)
        inimigo_cavaleiro = result.scalar_one_or_none()
        
        if inimigo_cavaleiro:
            return inimigo_cavaleiro
        else:
            raise HTTPException(detail="Inimigo Cavaleiro nao encontrado",status_code=status.HTTP_404_NOT_FOUND)
        
        
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=InimigosCavaleirosSchema)
async def post_cavaleiro(inimigo_cavaleiro:InimigosCavaleirosSchema,db:AsyncSession = Depends(get_session)):
    novo_inimigo_cavaleiro=InimigosCavaleirosModel(nome=inimigo_cavaleiro.nome, signo = inimigo_cavaleiro.signo,armadura=inimigo_cavaleiro.armadura,poder_especial=inimigo_cavaleiro.poder_especial,url=inimigo_cavaleiro.url,id_cavaleiro = inimigo_cavaleiro.id_cavaleiro)
    db.add(novo_inimigo_cavaleiro)
    await db.commit()
    return novo_inimigo_cavaleiro


@router.put("/{cavaleiro_id}",status_code=status.HTTP_202_ACCEPTED,response_model=InimigosCavaleirosSchema)
async def put_cavaleiro(cavaleiro_id,cavaleiro:InimigosCavaleirosSchema,db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InimigosCavaleirosModel).filter(InimigosCavaleirosModel.id == cavaleiro_id)
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
        query = select(InimigosCavaleirosModel).filter(InimigosCavaleirosModel.id == cavaleiro_id)
        result = await session.execute(query)
        cavaleiro_del=result.scalar_one_or_none()
        
        if cavaleiro_del:
            await session.delete(cavaleiro_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Cavaleiro nao encontrado",status_code=status.HTTP_404_NOT_FOUND)