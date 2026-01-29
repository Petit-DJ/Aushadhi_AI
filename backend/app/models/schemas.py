from pydantic import BaseModel
from typing import List, Optional


# ============== Protein Schemas ==============

class ProteinRequest(BaseModel):
    disease: str

class ProteinResponse(BaseModel):
    disease_protien: str
    protien_id: str
    percentage_contro: float
    Associated_pathway: str


# ============== ChEMBL Schemas ==============

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


# ============== Molecule Schemas ==============

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


# ============== Evaluation Schemas ==============

class EvaluationRequest(BaseModel):
    smiles: str

class EvaluationResponse(BaseModel):
    molecule: str
    molecule_name: str
    ic50: float
    disease_name: str
    disease_pid: str
    disease_protien_name: str
    data_analysis_report: str
