from fastapi import FastAPI, HTTPException
import logging
import os

app = FastAPI(title="Database Service")
logger = logging.getLogger(__name__)

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
