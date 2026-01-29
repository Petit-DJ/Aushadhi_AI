from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Simple placeholder image (1x1 white pixel PNG in base64)
PLACEHOLDER_IMAGE = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="

class ChEMBLRequest(BaseModel):
    pdb_id_input: str

class ChEMBLResponse(BaseModel):
    molecule: str
    canonical_smiles: str
    ic50: float
    disease_name: str
    disease_pid: str
    disease_protien_name: str
    molecule_image: Optional[str] = None

@router.post("/fetch_chambl_data/", response_model=List[ChEMBLResponse])
async def fetch_chembl_data(request: ChEMBLRequest):
    """Fetch ChEMBL molecular hits for a given PDB ID"""
    try:
        # Mock implementation - replace with actual ChEMBL integration
        mock_results = [
            {
                "molecule": "CC(=O)Oc1ccccc1C(=O)O",
                "canonical_smiles": "CC(=O)Oc1ccccc1C(=O)O",
                "ic50": 0.32,
                "disease_name": "Cancer",
                "disease_pid": request.pdb_id_input,
                "disease_protien_name": "TP53",
                "molecule_image": PLACEHOLDER_IMAGE
            },
            {
                "molecule": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",
                "canonical_smiles": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",
                "ic50": 0.48,
                "disease_name": "Cancer",
                "disease_pid": f"{request.pdb_id_input}_2",
                "disease_protien_name": "TP53",
                "molecule_image": PLACEHOLDER_IMAGE
            },
            {
                "molecule": "CC(C)Cc1ccc(cc1)C(C)C(=O)O",
                "canonical_smiles": "CC(C)Cc1ccc(cc1)C(C)C(=O)O",
                "ic50": 0.65,
                "disease_name": "Cancer",
                "disease_pid": f"{request.pdb_id_input}_3",
                "disease_protien_name": "TP53",
                "molecule_image": PLACEHOLDER_IMAGE
            }
        ]
        return mock_results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
