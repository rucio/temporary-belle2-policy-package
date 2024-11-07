import rucio.rse.translation

class BelleIIRSEDeterministicTranslation(rucio.rse.translation.RSEDeterministicTranslation):

    def __init__(self, rse=None, rse_attributes=None, protocol_attributes=None):
        """
        Initialize a translator object from the RSE, its attributes, and the protocol-specific
        attributes.

        :param rse: Name of RSE for this translation.
        :param rse_attributes: A dictionary of RSE-specific attributes for use in the translation.
        :param protocol_attributes: A dictionary of RSE/protocol-specific attributes.
        """
        super().__init__()
        self.rse = rse
        self.rse_attributes = rse_attributes if rse_attributes else {}
        self.protocol_attributes = protocol_attributes if protocol_attributes else {}

    @classmethod
    def _module_init_(cls):
        """
        Initialize the class object on first module load.
        """
        cls.register(cls.lfn2pfn_belleii, "belleii")

    @staticmethod
    def lfn2pfn_belleii(scope, name, rse, rse_attrs, protocol_attrs):
        """
        Given a LFN, convert it directly to a path using the mapping:

            path -> path
        This is valid only for the belleii convention where the scope can be determined
        from the LFN using a determinitic function.

        :param scope: Scope of the LFN.
        :param name: File name of the LFN.
        :param rse: RSE for PFN (ignored)
        :param rse_attrs: RSE attributes for PFN (ignored)
        :param protocol_attrs: RSE protocol attributes for PFN (ignored)
        :returns: Path for use in the PFN generation.
        """
        del scope
        del rse
        del rse_attrs
        del protocol_attrs
        return name
    
BelleIIRSEDeterministicTranslation._module_init_()