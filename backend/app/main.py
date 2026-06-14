from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DevIntel AI Backend Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}