class Goals:
    def __init__(self, starway_spirits_needed: int, require_spirits: bool,
        shuffle_star_beam: bool, star_beam_spirits_needed: bool, star_beam_power_stars_needed: bool,
        seed_goal: int, starway_power_stars_needed: int, star_hunt_total: int
    ):

        self.StarWaySpiritsNeeded = starway_spirits_needed if starway_spirits_needed > -1 else "Random"
        self.RequiredSpirits = require_spirits

        self.ShuffleStarBeam = shuffle_star_beam
        #Can remove this if in a month once old seeds are wiped
        if(star_beam_spirits_needed is not None):
            self.StarBeamSpiritsNeeded = star_beam_spirits_needed if star_beam_spirits_needed > -1 else "Random"

        self.StarBeamPowerStarsNeeded = star_beam_power_stars_needed

        self.SeedGoal = seed_goal
        self.StarWayPowerStarsNeeded = starway_power_stars_needed
        self.StarHuntTotal = star_hunt_total
        
