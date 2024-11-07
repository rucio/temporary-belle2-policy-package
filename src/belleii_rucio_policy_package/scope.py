from typing import TYPE_CHECKING, Optional

import rucio.common.utils

if TYPE_CHECKING:
    from collections.abc import Sequence

class BelleIIScopeExtractionAlgorithm(rucio.common.utils.ScopeExtractionAlgorithms):
    def __init__(self) -> None:
        """
        Initialises scope extraction algorithm object
        """
        super().__init__()

    @classmethod
    def _module_init_(cls) -> None:
        """
        Registers the included scope extraction algorithms
        """
        cls.register('belleii', cls.extract_scope_belleii)

    @staticmethod
    def extract_scope_belleii(did: str, scopes: Optional['Sequence[str]']) -> 'Sequence[str]':
        split_did = did.split('/')
        if did.startswith('/belle/mock/'):
            return 'mock', did
        if did.startswith('/belle/MC/'):
            if did.startswith('/belle/MC/BG') or \
               did.startswith('/belle/MC/build') or \
               did.startswith('/belle/MC/generic') or \
               did.startswith('/belle/MC/log') or \
               did.startswith('/belle/MC/mcprod') or \
               did.startswith('/belle/MC/prerelease') or \
               did.startswith('/belle/MC/release'):
                return 'mc', did
            if did.startswith('/belle/MC/cert') or \
               did.startswith('/belle/MC/dirac') or \
               did.startswith('/belle/MC/dr3') or \
               did.startswith('/belle/MC/fab') or \
               did.startswith('/belle/MC/hideki') or \
               did.startswith('/belle/MC/merge') or \
               did.startswith('/belle/MC/migration') or \
               did.startswith('/belle/MC/skim') or \
               did.startswith('/belle/MC/test'):
                return 'mc_tmp', did
            if len(split_did) > 4:
                if split_did[3].find('fab') > -1 or split_did[3].find('merge') > -1 or split_did[3].find('skim') > -1:
                    return 'mc_tmp', did
                if split_did[3].find('release') > -1:
                    return 'mc', did
            return 'mc_tmp', did
        if did.startswith('/belle/Raw/'):
            return 'raw', did
        if did.startswith('/belle/hRaw'):
            return 'hraw', did
        if did.startswith('/belle/user/'):
            if len(split_did) > 4:
                if len(split_did[3]) == 1 and scopes is not None and 'user.%s' % (split_did[4]) in scopes:
                    return 'user.%s' % split_did[4], did
            if len(split_did) > 3:
                if scopes is not None and 'user.%s' % (split_did[3]) in scopes:
                    return 'user.%s' % split_did[3], did
            return 'user', did
        if did.startswith('/belle/group/'):
            if len(split_did) > 4:
                if scopes is not None and 'group.%s' % (split_did[4]) in scopes:
                    return 'group.%s' % split_did[4], did
            return 'group', did
        if did.startswith('/belle/data/') or did.startswith('/belle/Data/'):
            if len(split_did) > 4:
                if split_did[3] in ['fab', 'skim']:  # /belle/Data/fab --> data_tmp
                    return 'data_tmp', did
                if split_did[3].find('release') > -1:  # /belle/Data/release --> data
                    return 'data', did
            if len(split_did) > 5:
                if split_did[3] in ['proc']:  # /belle/Data/proc
                    if split_did[4].find('release') > -1:  # /belle/Data/proc/release*
                        if len(split_did) > 7 and split_did[6] in ['GCR2c', 'prod00000007', 'prod6b', 'proc7b',
                                                                   'proc8b', 'Bucket4', 'Bucket6test', 'bucket6',
                                                                   'proc9', 'bucket7', 'SKIMDATAx1', 'proc10Valid',
                                                                   'proc10', 'SkimP10x1', 'SkimP11x1', 'SkimB9x1',
                                                                   'SkimB10x1', 'SkimB11x1']:  # /belle/Data/proc/release*/*/proc10/* --> data_tmp (Old convention)
                            return 'data_tmp', did
                        else:  # /belle/Data/proc/release*/*/proc11/* --> data (New convention)
                            return 'data', did
                    if split_did[4].find('fab') > -1:  # /belle/Data/proc/fab* --> data_tmp
                        return 'data_tmp', did
            return 'data_tmp', did
        if did.startswith('/belle/ddm/functional_tests/') or did.startswith('/belle/ddm/tests/') or did.startswith('/belle/test/ddm_test'):
            return 'test', did
        if did.startswith('/belle/BG/'):
            return 'data', did
        if did.startswith('/belle/collection'):
            return 'collection', did
        return 'other', did


BelleIIScopeExtractionAlgorithm._module_init_()