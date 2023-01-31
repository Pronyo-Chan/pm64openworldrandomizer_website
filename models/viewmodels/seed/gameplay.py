class Gameplay:
    def __init__(
        self,
        random_badges_bp: int,
        random_badges_fp: int,
        random_partner_fp: int,
        random_starpower_sp: int,
        random_formations: bool,
        mystery_random_pick: bool,
        random_choice: bool,
    ):

        self.BadgesBP = random_badges_bp
        self.BadgesFP = random_badges_fp
        self.PartnersFP = random_partner_fp
        self.StarPowerSP = random_starpower_sp
        self.ShuffleBattleFormations = random_formations

        self.MysteryMode = 0

        if(mystery_random_pick):
            self.MysteryMode = 1
        elif(random_choice):
            self.MysteryMode = 2
