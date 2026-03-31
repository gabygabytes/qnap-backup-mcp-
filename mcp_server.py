from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "QNAP Backup MCP",
        "status": "running"
    }

@app.get("/backup/status")
def backup_status():
    return {
        "hdp": "no consultado aún",
        "hbs": "no consultado aún"
    }
