import non_deterministic_pfn
import scope
import lfn2pfn

SUPPORTED_VERSION = ["35"]  # Only use with Rucio >=35.1.0 - pending https://github.com/rucio/rucio/issues/7082

def get_algorithms():
    return { 
        'non_deterministic_pfn': {
            'belleii_non_deterministic_pfn': non_deterministic_pfn.BelleIINonDeterministicPFNAlgorithm.construct_non_deterministic_pfn_belleii
            },
         'lfn2pfn': {
             'belleii_lfn2pfn': lfn2pfn.BelleIIRSEDeterministicTranslation.lfn2pfn_belleii
             },
         'scope': { 
             'belleii_extract_scope': scope.BelleIIScopeExtractionAlgorithm.extract_scope_belleii
             } 
    }