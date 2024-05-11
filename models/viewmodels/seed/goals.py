class Goals:
    def __init__(self, starway_spirits_needed: int, require_specific_spirits: bool, limit_chapter_logic: bool,
        shuffle_star_beam: bool, star_beam_spirits_needed: bool, star_beam_power_stars_needed: bool,
        seed_goal: int, starway_power_stars_needed: int, star_hunt_total: int
    ):

        self.RandomNumberOfStarWayStarSpirits = starway_spirits_needed == -1
        self.RandomNumberOfStarBeamStarSpirits = star_beam_spirits_needed == -1
        self.StarWaySpiritsNeeded = starway_spirits_needed
        self.RequireSpecificSpirits = require_specific_spirits
        self.LimitChapterLogic = limit_chapter_logic

        self.ShuffleStarBeam = shuffle_star_beam
        self.StarBeamSpiritsNeeded = star_beam_spirits_needed
        self.StarBeamPowerStarsNeeded = star_beam_power_stars_needed

        self.SeedGoal = seed_goal
        self.StarWayPowerStarsNeeded = starway_power_stars_needed
        self.StarHuntTotal = star_hunt_total
        
