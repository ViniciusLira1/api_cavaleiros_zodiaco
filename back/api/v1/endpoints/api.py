from fastapi import APIRouter

from api.v1.endpoints import cavaleiros_zodiaco
from api.v1.endpoints import inimigos_cavaleiros

api_router = APIRouter()
api_router.include_router(cavaleiros_zodiaco.router,prefix="/cavaleiros",tags=["cavaleiros"])
api_router.include_router(inimigos_cavaleiros.router,prefix="/inimigos",tags=["inimigos"])