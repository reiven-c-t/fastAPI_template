from api.v1.endpoints import items, login, queue_tasks, users
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(queue_tasks.router, prefix="/queue", tags=["queue"])
