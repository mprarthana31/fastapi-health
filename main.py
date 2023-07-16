from fastapi import FastAPI, status
import os
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/health", status_code=status.HTTP_200_OK)
async def root():
    return {"git_sha":os.getenv("GIT_SHA"),"build_at":os.getenv("BUILD_AT")}