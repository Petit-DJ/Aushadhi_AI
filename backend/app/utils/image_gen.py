import base64
from io import BytesIO
import logging

logger = logging.getLogger(__name__)

def smiles_to_base64_image(smiles: str, size=(300, 300)) -> str:
    """
    Convert SMILES string to base64 encoded PNG image.
    
    Requires RDKit to be installed:
    - pip install rdkit (or conda install -c conda-forge rdkit)
    """
    try:
        # Import RDKit - will fail if not installed
        from rdkit import Chem
        from rdkit.Chem import Draw
        
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            raise ValueError(f"Invalid SMILES: {smiles}")
        
        img = Draw.MolToImage(mol, size=size)
        
        # Convert to base64
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return img_str
        
    except ImportError:
        logger.warning("RDKit not installed. Returning placeholder for molecule image.")
        return None
    except Exception as e:
        logger.error(f"Error generating image: {e}")
        raise ValueError(f"Error generating image: {e}")
