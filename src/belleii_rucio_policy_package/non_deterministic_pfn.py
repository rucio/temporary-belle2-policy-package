from typing import Optional

from rucio.common.utils import NonDeterministicPFNAlgorithms


class BelleIINonDeterministicPFNAlgorithm(NonDeterministicPFNAlgorithms):
    """
    Belle II specific non-deterministic PFN algorithm
    """

    def __init__(self):
        super().__init__()

    @classmethod
    def _module_init_(cls) -> None:
        """
        Registers the included non-deterministic PFN algorithms
        """
        cls.register('belleii', cls.construct_non_deterministic_pfn_belleii)

    @staticmethod
    def construct_non_deterministic_pfn_belleii(dsn: str, scope: Optional[str], filename: str) -> str:
        """
        Defines relative PFN for Belle II specific replicas.
        This method contains the Belle II convention.
        To be used for non-deterministic Belle II sites.
        DSN (or datablock in the Belle II naming) contains /
        """

        fields = dsn.split("/")
        nfields = len(fields)
        if nfields == 0:
            return '/other/%s' % (filename)
        else:
            return '%s/%s' % (dsn, filename)
        
BelleIINonDeterministicPFNAlgorithm._module_init_()