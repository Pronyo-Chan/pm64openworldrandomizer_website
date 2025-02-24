class SeedInfo:
    def __init__(
        self,
        seed_id: int,
        creation_date: str,
        seed_hash_items: list, 
        settings_string: str, 
        star_rod_mod_version: int,
        is_plandomizer_seed: bool,
    ):

        self.SeedID = seed_id
        self.CreationDate = creation_date
        self.SeedHashItems = seed_hash_items
        self.SettingsString = settings_string
        self.StarRodModVersion = star_rod_mod_version
        self.IsPlandomizerSeed = is_plandomizer_seed
