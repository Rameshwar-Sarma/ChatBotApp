from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }

app.include_router(router)