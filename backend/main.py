from fastapi import FastAPI

app = FastAPI(title="Rule Attorney API")


@app.get("/")
def root():
    return {"message": "Rule Attorney API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}
