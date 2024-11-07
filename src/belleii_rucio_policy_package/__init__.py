from belleii_rucio_policy_package.non_deterministic_pfn import BelleIINonDeterministicPFNAlgorithm
from belleii_rucio_policy_package.scope import BelleIIScopeExtractionAlgorithm
from belleii_rucio_policy_package.lfn2pfn import BelleIIRSEDeterministicTranslation

SUPPORTED_VERSION = ["35"]  # Only use with Rucio >=35.1.0 - pending https://github.com/rucio/rucio/issues/7082

def get_algorithms():
    return { 
        'non_deterministic_pfn': {
            'belleii_non_deterministic_pfn': BelleIINonDeterministicPFNAlgorithm.construct_non_deterministic_pfn_belleii
            },
         'lfn2pfn': {
             'belleii_lfn2pfn': BelleIIRSEDeterministicTranslation.lfn2pfn_belleii
             },
         'scope': { 
             'belleii_extract_scope': BelleIIScopeExtractionAlgorithm.extract_scope_belleii
             } 
    }