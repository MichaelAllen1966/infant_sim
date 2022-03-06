import numpy as np
import pandas as pd
import random

from operator import itemgetter
from .treatments import Treatments

class Patient:
    """
    Patient class
    """
    def __init__(self, global_vars):
        """
        Constructor for Patient class
        """

        self.global_vars = global_vars

        # Get new infant id
        infant_id = global_vars.get_new_infant_id()

        # Set random seed
        random.seed = infant_id

        # Set attributes
        self.day = 0
        self.id = infant_id
        self.treatments = Treatments(infant_id)

        # Set up lists for records
        self.observations = []
        self.health = []

        # Set patient type at random
        type_index = random.randint(0, len(self.global_vars.patient_types) - 1)
        self.patient_type_index = type_index
        self.patient_type = self.global_vars.patient_types[type_index]

        # Set random starting health between limits
        self.current_health = dict()
        self.current_health['general'] = random.randint(*global_vars.starting_health_range)

        # Set starting organ-specific health as equal to overall health
        self.current_health['gi'] = self.current_health['general']
        self.current_health['pulmonary'] = self.current_health['general']
        self.current_health['brain'] = self.current_health['general']

        # Record first set of health stats (dict syntax appends a copy)
        self.health.append(dict(self.current_health))

        # Get first set of observations (imprecise measurements of health)
        self.get_observations()

    def get_observations(self):
        """
        Get observations by adding random jitter to health.
        As jitter may take observations outside range 0-100, clip to 0-100.
        """

        self.current_observations = dict()
        for key, value in self.current_health.items():
            jitter = self.global_vars.observation_jitter
            obs = value + random.randint(-jitter, jitter)
            obs = np.clip(obs, 0 , 100)
            self.current_observations[key] = obs
        self.observations.append(dict(self.current_observations))

    def loop_through_days(self):
        for day in range(self.global_vars.duration):
            self.update_health()
            self.get_observations()

        # Convert lists of dictionaries into pandas dataframes
        self.health = pd.DataFrame(self.health)
        self.observations = pd.DataFrame(self.observations)
        self.observations['label'] = self.patient_type_index

    def update_health(self):
        """
        Update health status
        """
        # Currently only update based on no treatment
        if self.patient_type_index == 0:
            # Improving patient without treatment
            self.current_health['gi'] += 1
            self.current_health['pulmonary'] += 1
            self.current_health['brain'] += 1
        elif self.patient_type_index == 1:
            # GI deterioration
            self.current_health['general'] -=1
            self.current_health['gi'] -= 1
            self.current_health['pulmonary'] += 1
            self.current_health['brain'] += 1
        elif self.patient_type_index == 1:
            # Pulmnonary deterioration
            self.current_health['gi'] += 1
            self.current_health['pulmonary'] -= 1
            self.current_health['brain'] += 1
        elif self.patient_type_index == 2:
            # Cerbral derioration
            self.current_health['gi'] += 1
            self.current_health['pulmonary'] += 1
            self.current_health['brain'] -= 1
        elif self.patient_type_index == 4:
            # Death with any treatment
            self.current_health['gi'] -= 1
            self.current_health['pulmonary'] -= 1
            self.current_health['brain'] -= 1

        # Set general health as minimum of organ-specific values
        keys_to_get = ['gi', 'pulmonary', 'brain']
        retrieved_values = itemgetter(*keys_to_get)(self.current_health)
        self.current_health['general'] = min(retrieved_values)

        # Clip all health values to 0-100 range
        for key, value in self.current_health.items():
            self.current_health[key] = np.clip(value, 0, 100)

        # Record
        self.health.append(dict(self.current_health))




















