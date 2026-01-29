from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Simple placeholder image (1x1 white pixel PNG in base64)
PLACEHOLDER_IMAGE = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="

class MoleculeRequest(BaseModel):
    disease: str

class MoleculeResponse(BaseModel):
    molecule: str
    molecule_name: str
    smile_string: str
    ic50: float
    disease_name: str
    disease_pid: str
    disease_protien_name: str
    molecule_image: Optional[str] = None

@router.post("/alternate_molecule_generator/", response_model=List[MoleculeResponse])
async def generate_alternate_molecules(request: MoleculeRequest):
    """Generate alternate molecules for a given disease"""
    try:
        # Mock implementation - replace with actual ML-based generation
        mock_results = [
            {
                "molecule": "CC(=O)Oc1ccccc1C(=O)O",
                "molecule_name": "Aspirin_Analog_1",
                "smile_string": "CC(=O)Oc1ccccc1C(=O)O",
                "ic50": 0.35,
                "disease_name": request.disease,
                "disease_pid": "1TUP",
                "disease_protien_name": "TP53",
                "molecule_image": PLACEHOLDER_IMAGE
            },
            {
                "molecule": "CCO",
                "molecule_name": "Compound_A",
                "smile_string": "CCO",
                "ic50": 0.45,
                "disease_name": request.disease,
                "disease_pid": "2ABC",
                "disease_protien_name": "TP53",
                "molecule_image": PLACEHOLDER_IMAGE
            },
            {
                "molecule": "CC(=O)O",
                "molecule_name": "Compound_B",
                "smile_string": "CC(=O)O",
                "ic50": 0.52,
                "disease_name": request.disease,
                "disease_pid": "3DEF",
                "disease_protien_name": "TP53",
                "molecule_image": PLACEHOLDER_IMAGE
            },
            {
                "molecule": "c1ccccc1",
                "molecule_name": "Benzene_Derivative",
                "smile_string": "c1ccccc1",
                "ic50": 0.78,
                "disease_name": request.disease,
                "disease_pid": "4GHI",
                "disease_protien_name": "TP53",
                "molecule_image": PLACEHOLDER_IMAGE
            }
        ]
        return mock_results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
