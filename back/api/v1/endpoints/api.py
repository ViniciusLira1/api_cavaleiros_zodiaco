from fastapi import APIRouter

from api.v1.endpoints import cavaleiros_zodiaco

api_router = APIRouter()
api_router.include_router(cavaleiros_zodiaco.router,prefix="/cavaleiros",tags=["cavaleiros"])