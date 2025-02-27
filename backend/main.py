import app.config.charge_environnement as config
from app.fastapi.champion_router import champion_router
from app.fastapi.item_router import item_router
from app.fastapi.login_router import login_router
from app.fastapi.user_router import user_router
from app_setup import app_setup
from fastapi import FastAPI

app = FastAPI()

app.include_router(user_router, tags=["User"])
app.include_router(champion_router, tags=["Champion"])
app.include_router(item_router, tags=["Item"])
app.include_router(login_router, tags=["Login"])

if __name__ == "__main__":
    config.load_dotenv()
    import uvicorn

    app_setup()
    uvicorn.run(app, host="0.0.0.0", port=8000)
