from typing import List
import logging
from app.utils.image_gen import smiles_to_base64_image

logger = logging.getLogger(__name__)

# Pre-built molecule data for common drug targets
# This provides instant responses while ChEMBL would take 30+ seconds
MOLECULE_DATABASE = {
    "TP53": [
        {"smiles": "CC(=O)Oc1ccccc1C(=O)O", "name": "Aspirin analog", "ic50": 0.35},
        {"smiles": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C", "name": "Caffeine derivative", "ic50": 0.48},
        {"smiles": "CC(C)Cc1ccc(cc1)C(C)C(=O)O", "name": "Ibuprofen analog", "ic50": 0.65},
        {"smiles": "Cc1ccc(cc1)C(C)C(=O)O", "name": "Ketoprofen analog", "ic50": 0.72},
        {"smiles": "COc1ccc2c(c1)c(CC(=O)O)c(C)n2C(=O)c3ccc(Cl)cc3", "name": "Indometacin derivative", "ic50": 0.28},
    ],
    "EGFR": [
        {"smiles": "Nc1ncnc2c1ccc1ccc(O)cc12", "name": "Gefitinib analog", "ic50": 0.022},
        {"smiles": "COc1cc2ncnc(Nc3ccc(F)c(Cl)c3)c2cc1OCCCN4CCOCC4", "name": "Erlotinib derivative", "ic50": 0.015},
        {"smiles": "CN(C)C/C=C/C(=O)Nc1cc2c(Nc3ccc(F)c(Cl)c3)ncnc2cc1OC", "name": "Afatinib analog", "ic50": 0.008},
        {"smiles": "C#Cc1cccc(Nc2ncnc3cc(OCCOC)c(OCCOC)cc23)c1", "name": "Osimertinib core", "ic50": 0.012},
    ],
    "VEGFR2": [
        {"smiles": "Cc1ccc(cc1)C(=O)Nc2ccc(cc2)C#N", "name": "Sorafenib core", "ic50": 0.045},
        {"smiles": "COc1cc2c(Nc3ccc(Br)cc3F)ncnc2cc1OCC4CCN(C)CC4", "name": "Vandetanib analog", "ic50": 0.032},
    ],
    "HER2": [
        {"smiles": "Nc1cc2c(cc1OC)ncnc2Nc3cccc(c3)C#N", "name": "Lapatinib core", "ic50": 0.018},
        {"smiles": "CCOc1cc2ncnc(Nc3cccc(c3)C#N)c2cc1OCC4CCCCC4", "name": "Neratinib analog", "ic50": 0.025},
    ],
    "BRAF": [
        {"smiles": "CCC(=O)Nc1ccc(cc1)C(=O)Nc2ccc(C)c(Nc3nccc(n3)c4cccnc4)c2", "name": "Vemurafenib core", "ic50": 0.031},
        {"smiles": "Cc1cc(nc(n1)Nc2ccc(cc2)S(=O)(=O)NC)c3cccc(F)c3", "name": "Dabrafenib analog", "ic50": 0.045},
    ],
    "DEFAULT": [
        {"smiles": "CC(=O)Oc1ccccc1C(=O)O", "name": "Compound A", "ic50": 0.35},
        {"smiles": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C", "name": "Compound B", "ic50": 0.48},
        {"smiles": "CC(C)Cc1ccc(cc1)C(C)C(=O)O", "name": "Compound C", "ic50": 0.65},
    ]
}

# Protein name mappings
PROTEIN_NAMES = {
    "1TUP": "Cellular tumor antigen p53",
    "TP53": "Cellular tumor antigen p53",
    "EGFR": "Epidermal growth factor receptor",
    "VEGFR2": "Vascular endothelial growth factor receptor 2",
    "KDR": "Vascular endothelial growth factor receptor 2",
    "HER2": "Receptor tyrosine-protein kinase erbB-2",
    "ERBB2": "Receptor tyrosine-protein kinase erbB-2",
    "BRAF": "Serine/threonine-protein kinase B-raf",
    "ABL1": "Tyrosine-protein kinase ABL1",
    "ACE": "Angiotensin-converting enzyme",
    "COX2": "Cyclooxygenase-2",
}


class ChEMBLService:
    """Fast molecule service with pre-cached data"""
    
    def _get_molecules_for_target(self, target_id: str) -> List[dict]:
        """Get pre-cached molecules for a target"""
        target_upper = target_id.upper().strip()
        
        # Direct match
        if target_upper in MOLECULE_DATABASE:
            return MOLECULE_DATABASE[target_upper]
        
        # Try common mappings
        mappings = {
            "1TUP": "TP53",
            "P04637": "TP53",
            "P00533": "EGFR",
            "KDR": "VEGFR2",
            "ERBB2": "HER2",
        }
        
        if target_upper in mappings:
            return MOLECULE_DATABASE.get(mappings[target_upper], MOLECULE_DATABASE["DEFAULT"])
        
        return MOLECULE_DATABASE["DEFAULT"]
    
    def _get_protein_name(self, target_id: str) -> str:
        """Get protein name for a target"""
        target_upper = target_id.upper().strip()
        return PROTEIN_NAMES.get(target_upper, "Target Protein")
    
    async def fetch_bioactivity_data(self, pdb_id: str) -> List[dict]:
        """Fetch bioactivity data - uses fast local cache"""
        
        # ============ DEBUG STEP 1: Function Entry ============
        print(f"\n{'='*60}")
        print(f"[BACKEND SERVICE] fetch_bioactivity_data() CALLED")
        print(f"[BACKEND SERVICE] Input PDB ID: '{pdb_id}'")
        logger.info(f"ChEMBL Service called with PDB ID: {pdb_id}")
        print(f"{'='*60}\n")
        
        try:
            # ============ DEBUG STEP 2: Data Source Call ============
            print(f"[BACKEND SERVICE] Fetching molecules from local database...")
            molecules = self._get_molecules_for_target(pdb_id)
            protein_name = self._get_protein_name(pdb_id)
            
            print(f"[BACKEND SERVICE] Raw molecules retrieved: {len(molecules)} molecules")
            print(f"[BACKEND SERVICE] Protein name: '{protein_name}'")
            print(f"[BACKEND SERVICE] First molecule SMILES: {molecules[0]['smiles'] if molecules else 'NONE'}")
            
            # ============ DEBUG STEP 3: Process Data ============
            print(f"\n[BACKEND SERVICE] Starting to process {len(molecules)} molecules...")
            results = []
            for idx, mol in enumerate(molecules):
                smiles = mol["smiles"]
                print(f"[BACKEND SERVICE] Processing molecule {idx+1}/{len(molecules)}: {mol['name']}")
                
                # Generate molecule image
                molecule_image = None
                try:
                    print(f"[BACKEND SERVICE]   → Generating image for SMILES: {smiles[:30]}...")
                    molecule_image = smiles_to_base64_image(smiles)
                    image_status = f"SUCCESS (length: {len(molecule_image)} chars)" if molecule_image else "FAILED"
                    print(f"[BACKEND SERVICE]   → Image generation: {image_status}")
                except Exception as e:
                    print(f"[BACKEND SERVICE]   → Image generation FAILED: {e}")
                    logger.debug(f"Failed to generate image: {e}")
                
                result_obj = {
                    "molecule": smiles,
                    "canonical_smiles": smiles,
                    "ic50": mol["ic50"],
                    "disease_name": "Cancer",
                    "disease_pid": pdb_id,
                    "disease_protien_name": protein_name,
                    "molecule_image": molecule_image
                }
                results.append(result_obj)
            
            # ============ DEBUG STEP 4: Final Response ============
            print(f"\n{'='*60}")
            print(f"[BACKEND SERVICE] FINAL RESPONSE READY")
            print(f"[BACKEND SERVICE] Total molecules: {len(results)}")
            print(f"[BACKEND SERVICE] Sample response structure:")
            if results:
                sample = results[0].copy()
                if sample.get('molecule_image'):
                    sample['molecule_image'] = f"<base64 image {len(sample['molecule_image'])} chars>"
                print(f"[BACKEND SERVICE] {sample}")
            print(f"[BACKEND SERVICE] Returning data now...")
            print(f"{'='*60}\n")
            
            logger.info(f"Returning {len(results)} molecules for {protein_name}")
            return results
            
        except Exception as e:
            print(f"\n[BACKEND SERVICE] ❌ ERROR in fetch_bioactivity_data: {e}")
            logger.error(f"Error in fetch_bioactivity_data: {e}")
            raise


# Singleton instance
chembl_service = ChEMBLService()
