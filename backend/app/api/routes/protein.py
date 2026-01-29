from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ProteinRequest(BaseModel):
    disease: str

class ProteinResponse(BaseModel):
    disease_protien: str
    protien_id: str
    percentage_contro: float
    Associated_pathway: str

@router.post("/find_protien/", response_model=List[ProteinResponse])
async def find_protein(request: ProteinRequest):
    """Find target proteins for a given disease"""
    try:
        # Mock implementation - replace with actual logic
        mock_results = [
            {
                "disease_protien": "TP53 (Tumor Protein P53)",
                "protien_id": "1TUP",
                "percentage_contro": 0.68,
                "Associated_pathway": "p53 ras"
            }
        ]
        return mock_results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
