"""
FastAPI
"""
import httpx

from fastapi import FastAPI
from USER_SERVICE.commons.logger import get_logger
from USER_SERVICE.pydantic_models.models import Response
from USER_SERVICE.pydantic_models.generated.user_svc_pcs.models import UserIn
from USER_SERVICE.pydantic_models.enviornment import get_settings

logger = get_logger('main.py')

settings = get_settings()

url_signup = f'{settings.user_svc_prc_host}/signup'

def get_url_activate(user_id:int):
    return f'{settings.user_svc_prc_host}/activate/{user_id}'

def get_url_deactivate(user_id:int):
    return f'{settings.user_svc_prc_host}/deactivate/{user_id}'

logger.info('   Initiliazing Fast API app')
app = FastAPI(title="FastAPI")

@app.post("/signup", response_model=Response)
async def signup(user:UserIn):
    logger.info('   signup function is executing')
    logger.info(user.json())
    async with httpx.AsyncClient() as client:
        response = await client.post(url_signup, data=user.json())
        if response.status_code == 200:
            data1 = response.json()
            logger.info(data1)
            return Response(code=200, message='SUCCESS', data=data1)

@app.get("/deactivate/{user_id}", response_model=Response)
async def deactivate(user_id:int):
    logger.info('   deactivate function is executing')
    return await toggle_enabled(user_id, False)

@app.get("/activate/{user_id}", response_model=Response)
async def activate(user_id:int):
    logger.info('   activate function is executing')
    return await toggle_enabled(user_id, True)

async def toggle_enabled(user_id:int, enabled: bool):
    logger.info('   toggle_enabled function is executing')
    async with httpx.AsyncClient() as client:
        url_toggle = get_url_activate(user_id) if enabled else get_url_deactivate(user_id)
        response = await client.get(url_toggle)
        data1 = response.json()
        logger.info(data1)
        if response.status_code == 200:
            return Response(code=200, message='SUCCESS', data=data1)

logger.info('   End of the main file')
