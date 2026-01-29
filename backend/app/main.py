from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import protein, chembl, molecules, evaluation

app = FastAPI(
    title="AushadhiAI API",
    description="Drug discovery platform backend",
    version="1.0.0"
)

# CORS configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your Next.js app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(protein.router, tags=["Protein"])
app.include_router(chembl.router, tags=["ChEMBL"])
app.include_router(molecules.router, tags=["Molecules"])
app.include_router(evaluation.router, tags=["Evaluation"])

@app.get("/")
async def root():
    return {"message": "AushadhiAI API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
