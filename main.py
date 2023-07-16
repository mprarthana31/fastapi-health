from fastapi import FastAPI, status
from dotenv import load_dotenv
import os
from fastapi.responses import PlainTextResponse

app = FastAPI()
load_dotenv()

@app.get("/health", status_code=status.HTTP_200_OK)
async def root():
    return {"git_sha":os.getenv("RENDER_GIT_COMMIT"),"build_at":os.getenv("BUILD_AT")}