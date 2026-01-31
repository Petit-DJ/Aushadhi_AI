import { authApiClient } from "./api";

export function findTargetProtein(disease: string) {
    // ============ DEBUG STEP 1: Frontend Call ============
    console.log('\n' + '='.repeat(60));
    console.log('[FRONTEND API] findTargetProtein() CALLED');
    console.log('[FRONTEND API] Disease:', disease);
    console.log('='.repeat(60) + '\n');
    
    return authApiClient.post("/find_protien/", {"disease": disease});
}

export async function findHits(pdpid: string) {
    // ============ DEBUG STEP 1: Frontend Call ============
    console.log('\n' + '*'.repeat(60));
    console.log('[FRONTEND API] findHits() CALLED');
    console.log('[FRONTEND API] PDB ID:', pdpid);
    console.log('[FRONTEND API] Timestamp:', new Date().toISOString());
    console.log('*'.repeat(60) + '\n');
    
    try {
        console.log('[FRONTEND API] Making POST request to /fetch_chambl_data/...');
        console.log('[FRONTEND API] Request body:', {"pdb_id_input": pdpid});
        
        const startTime = performance.now();
        const response = await authApiClient.post("/fetch_chambl_data/", {"pdb_id_input": pdpid});
        const endTime = performance.now();
        const duration = (endTime - startTime).toFixed(2);
        
        // ============ DEBUG STEP 2: Response Received ============
        console.log('\n' + '*'.repeat(60));
        console.log('[FRONTEND API] RESPONSE RECEIVED');
        console.log('[FRONTEND API] Status:', response.status);
        console.log('[FRONTEND API] Duration:', duration + 'ms');
        console.log('[FRONTEND API] Response type:', typeof response.data);
        console.log('[FRONTEND API] Is Array:', Array.isArray(response.data));
        
        if (Array.isArray(response.data)) {
            console.log('[FRONTEND API] Number of molecules:', response.data.length);
            if (response.data.length > 0) {
                const firstMol = response.data[0];
                console.log('[FRONTEND API] First molecule structure:');
                console.log('[FRONTEND API]   - ic50:', firstMol.ic50);
                console.log('[FRONTEND API]   - disease_name:', firstMol.disease_name);
                console.log('[FRONTEND API]   - has molecule_image:', !!firstMol.molecule_image);
                if (firstMol.molecule_image) {
                    console.log('[FRONTEND API]   - image length:', firstMol.molecule_image.length, 'chars');
                }
            }
        } else {
            console.log('[FRONTEND API] Unexpected response format:', response.data);
        }
        console.log('*'.repeat(60) + '\n');
        
        return response;
        
    } catch (error: any) {
        // ============ DEBUG STEP 3: Error Handling ============
        console.error('\n' + '*'.repeat(60));
        console.error('[FRONTEND API] ❌ ERROR in findHits()');
        console.error('[FRONTEND API] Error type:', error.constructor.name);
        
        if (error.response) {
            console.error('[FRONTEND API] Response error:');
            console.error('[FRONTEND API]   - Status:', error.response.status);
            console.error('[FRONTEND API]   - Data:', error.response.data);
        } else if (error.request) {
            console.error('[FRONTEND API] No response received');
            console.error('[FRONTEND API] Request:', error.request);
        } else {
            console.error('[FRONTEND API] Error message:', error.message);
        }
        console.error('*'.repeat(60) + '\n');
        
        throw error;
    }
}

export function generateAlternateMols(disease: string) {
    console.log('[FRONTEND API] generateAlternateMols() called with:', disease);
    return authApiClient.post("/alternate_molecule_generator/", {"disease": disease});
}

export function showEvaluation(smile: string){
    console.log('[FRONTEND API] showEvaluation() called with SMILES:', smile);
    return authApiClient.post("/find_data_evaluation_report/",{"smiles":smile});
}
