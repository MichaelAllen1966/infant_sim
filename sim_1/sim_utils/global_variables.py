

class GlobVars:
    """
    Class to store global variables.

    Attributes
    ----------
    infant_id: Infant count used to create new infants ids.

    """
    def __init__(self):
        """GlobVars constructor"""

        self.duration = 150

        self.infant_id = 0

        self.patient_types={
            0: 'Improving without treatment',
            1: 'GI deterioration',
            2: 'Pulmnonary deterioration',
            3: 'Cerbral derioration',
            4: 'Death with any treatment'}

        self.starting_health_range = (20, 65)
        self.delay_before_condition_range = (5, 50)
        self.change_rate_range = (0.75, 1.5)
        self.observation_jitter = 5
        
    def get_new_infant_id(self):
        """Create new infant ID by incrementing count."""
        self.infant_id += 1
        return self.infant_id
