from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import httpx
import logging
from datetime import datetime
import os

app = FastAPI(title="TemplateAI API Gateway")
logger = logging.getLogger(__name__)

# Service URLs
LANGGRAPH_URL = os.getenv("LANGGRAPH_URL", "http://langgraph-orchestrator:8001")
AUTOGEN_URL = os.getenv("AUTOGEN_URL", "http://autogen-agents:8002")
CODE_GEN_URL = os.getenv("CODE_GEN_URL", "http://code-generation:8003")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "api-gateway"
    }

@app.post("/api/v1/templates/generate")
async def generate_template(request: dict):
    """Generate a new template"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{LANGGRAPH_URL}/workflow/start",
                json=request,
                timeout=300.0
            )
            workflow_id = response.json()["workflow_id"]
        
        return {
            "status": "processing",
            "workflow_id": workflow_id,
            "message": "Template generation started"
        }
    except Exception as e:
        logger.error(f"Error generating template: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/templates/list")
async def list_templates():
    """List all generated templates"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{CODE_GEN_URL}/templates/list",
                timeout=30.0
            )
            return response.json()
    except Exception as e:
        logger.error(f"Error listing templates: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/status/{workflow_id}")
async def get_status(workflow_id: str):
    """Get workflow status"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{LANGGRAPH_URL}/workflow/{workflow_id}/status",
                timeout=30.0
            )
            return response.json()
    except Exception as e:
        logger.error(f"Error getting status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
