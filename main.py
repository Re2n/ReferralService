from contextlib import asynccontextmanager

from fastapi import FastAPI

from config.Database import db
from routers.ReferralCode import referral_code_router
from routers.User import user_router
from schemas.Base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await db.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(referral_code_router)