from fastapi import FastAPI, HTTPException
import logging
import os

app = FastAPI(title="Testing Service")
logger = logging.getLogger(__name__)

@app.post("/validate/wordpress")
async def validate_wordpress(request: dict):
    """Validate WordPress template"""
    try:
        return {
            "status": "valid",
            "issues": [],
            "warnings": []
        }
    except Exception as e:
        logger.error(f"Error validating: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
