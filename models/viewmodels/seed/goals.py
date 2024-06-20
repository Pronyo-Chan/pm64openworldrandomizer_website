class Goals:
    def __init__(self, starway_spirits_needed: int, require_specific_spirits: bool, limit_chapter_logic: bool,
        shuffle_star_beam: bool, star_beam_spirits_needed: bool, star_beam_power_stars_needed: bool,
        seed_goal: int, starway_power_stars_needed: int, star_hunt_total: int
    ):

        self.StarWaySpiritsNeeded = starway_spirits_needed if starway_spirits_needed > -1 else "Random"
        self.RequireSpecificSpirits = require_specific_spirits
        self.LimitChapterLogic = limit_chapter_logic

        self.ShuffleStarBeam = shuffle_star_beam
        self.StarBeamSpiritsNeeded = star_beam_spirits_needed if star_beam_spirits_needed > -1 else "Random"
        self.StarBeamPowerStarsNeeded = star_beam_power_stars_needed

        self.SeedGoal = seed_goal
        self.StarWayPowerStarsNeeded = starway_power_stars_needed
        self.StarHuntTotal = star_hunt_total
        
