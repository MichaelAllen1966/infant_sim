

class GlobVars:
    """
    Class to store global variables.

    Attributes
    ----------
    infant_id: Infant count used to create new infants ids.

    """
    def __init__(self):
        """GlobVars constructor"""

        self.duration = 100

        self.infant_id = 0

        self.patient_types={
            0: 'Improving without treatment',
            1: 'GI deterioration',
            2: 'Pulmnonary deterioration',
            3: 'Cerbral derioration',
            4: 'Death with any treatment'}

        self.starting_health_range = (30, 60)
        self.observation_jitter = 2
        
    def get_new_infant_id(self):
        """Create new infant ID by incrementing count."""
        self.infant_id += 1
        return self.infant_id
