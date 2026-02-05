from fastapi import FastAPI, HTTPException
import logging
import os
from datetime import datetime

app = FastAPI(title="Code Generation Service")
logger = logging.getLogger(__name__)

TEMPLATE_STORAGE_PATH = os.getenv("TEMPLATE_STORAGE_PATH", "/data/templates")

@app.post("/generate/wordpress")
async def generate_wordpress_template(request: dict):
    """Generate WordPress template"""
    try:
        template_id = f"tpl_{request.get('name')}_{int(datetime.now().timestamp())}"
        
        return {
            "status": "completed",
            "template_id": template_id,
            "path": f"{TEMPLATE_STORAGE_PATH}/{template_id}"
        }
    except Exception as e:
        logger.error(f"Error generating WordPress template: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/templates/list")
async def list_templates():
    """List all generated templates"""
    try:
        templates = []
        if os.path.exists(TEMPLATE_STORAGE_PATH):
            templates = os.listdir(TEMPLATE_STORAGE_PATH)
        
        return {
            "total": len(templates),
            "templates": templates
        }
    except Exception as e:
        logger.error(f"Error listing templates: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
