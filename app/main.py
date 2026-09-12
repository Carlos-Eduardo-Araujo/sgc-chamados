from fastapi import FastAPI
from app.database import Base, engine
from app.routes.chamados import router as chamados_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SGC - Sistema de Gerenciamento de Chamados",
    version="1.0.0",
    description="API acadêmica para registro e acompanhamento de chamados de suporte.",
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(chamados_router)
