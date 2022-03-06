import random

from .observations import Observations
from .treatments import Treatments

class Patient:
    """
    Patient class
    """
    def __init__(self, global_vars):
        """
        Constructor for Patient class
        """
        # Get new infant id
        infant_id = global_vars.get_new_infant_id()

        # Set random seed
        random.seed = infant_id

        # Set attributes
        self.id = infant_id
        self.observations = Observations(infant_id)
        self.treatments = Treatments(infant_id)
        _ = random.randint(0,4)
        self.patient_type = global_vars.patient_types[_]
        self.health = random.randint(*global_vars.starting_health_range)




