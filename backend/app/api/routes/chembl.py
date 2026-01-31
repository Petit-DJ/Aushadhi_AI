from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.services.chembl_service import chembl_service

router = APIRouter()

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
    
    # ============ DEBUG STEP 1: Endpoint Hit ============
    print(f"\n{'*'*60}")
    print(f"[BACKEND ROUTE] /fetch_chambl_data/ ENDPOINT HIT")
    print(f"[BACKEND ROUTE] Request received: {request.dict()}")
    print(f"[BACKEND ROUTE] PDB ID: '{request.pdb_id_input}'")
    print(f"{'*'*60}\n")
    
    try:
        # ============ DEBUG STEP 2: Calling Service ============
        print(f"[BACKEND ROUTE] Calling ChEMBL service...")
        results = await chembl_service.fetch_bioactivity_data(request.pdb_id_input)
        
        # ============ DEBUG STEP 3: Service Response ============
        print(f"\n{'*'*60}")
        print(f"[BACKEND ROUTE] Service returned successfully")
        print(f"[BACKEND ROUTE] Number of molecules: {len(results)}")
        print(f"[BACKEND ROUTE] Response type: {type(results)}")
        if results:
            print(f"[BACKEND ROUTE] First molecule IC50: {results[0].get('ic50')}")
            has_image = results[0].get('molecule_image') is not None
            print(f"[BACKEND ROUTE] First molecule has image: {has_image}")
        print(f"[BACKEND ROUTE] Sending response to client...")
        print(f"{'*'*60}\n")
        
        return results
        
    except Exception as e:
        print(f"\n[BACKEND ROUTE] ❌ ERROR: {e}")
        print(f"[BACKEND ROUTE] Error type: {type(e).__name__}")
        raise HTTPException(status_code=500, detail=str(e))

