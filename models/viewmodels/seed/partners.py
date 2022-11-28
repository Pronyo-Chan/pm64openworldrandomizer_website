class Partners:
    def __init__(
        self,
        partners_in_default_locations: bool,
        partners_always_usable: bool,
        start_with_random_partners: bool,
        random_partners_min: bool,
        random_partners_max: bool
    ):

        self.ShufflePartners = not partners_in_default_locations
        self.PartnersAlwaysUsable = partners_always_usable
        self.StartWithRandomPartners = start_with_random_partners
        self.MinNumberOfStartingPartners = random_partners_min
        self.MaxNumberOfStartingPartners = random_partners_max

