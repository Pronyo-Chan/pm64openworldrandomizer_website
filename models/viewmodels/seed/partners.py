class Partners:
    def __init__(
        self,
        partners_in_default_locations: bool,
        partner_shuffle: int,
        partners_always_usable: bool,
        start_with_random_partners: bool,
        random_partners_min: bool,
        random_partners_max: bool,
        start_with_partners: dict
    ):

        self.ShufflePartners = not partners_in_default_locations
        self.PartnersAlwaysUsable = partners_always_usable
        self.StartWithRandomPartners = start_with_random_partners
        self.MinNumberOfStartingPartners = random_partners_min
        self.MaxNumberOfStartingPartners = random_partners_max

        if partners_in_default_locations:
            self.ShufflePartners = 0 if partners_in_default_locations  else 2
        else:
            self.ShufflePartners = partner_shuffle

        if start_with_partners is None:
            return
            
        self.StartWithPartners = []
        if start_with_partners.get("Goombario"):
            self.StartWithPartners.append("Goombario")
        if start_with_partners.get("Kooper"):
            self.StartWithPartners.append("Kooper")
        if start_with_partners.get("Bombette"):
            self.StartWithPartners.append("Bombette")
        if start_with_partners.get("Parakarry"):
            self.StartWithPartners.append("Parakarry")
        if start_with_partners.get("Bow"):
            self.StartWithPartners.append("Bow")
        if start_with_partners.get("Watt"):
            self.StartWithPartners.append("Watt")
        if start_with_partners.get("Sushie"):
            self.StartWithPartners.append("Sushie")
        if start_with_partners.get("Lakilester"):
            self.StartWithPartners.append("Lakilester")

