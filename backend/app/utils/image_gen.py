from rdkit import Chem
from rdkit.Chem import Draw
import base64
from io import BytesIO

def smiles_to_base64_image(smiles: str, size=(300, 300)) -> str:
    """
        Convert SMILES string to base64 encoded PNG image.
    """
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            raise ValueError(f"Invalid SMILES: {smiles}")
        
        img = Draw.MolToImage(mol, size=size)
        
        # Convert to base64
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return img_str
        
    except Exception as e:
                raise ValueError(f"Error generating image: {e}")
