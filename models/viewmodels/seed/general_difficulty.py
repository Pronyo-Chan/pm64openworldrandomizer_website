class GeneralDifficulty:
    def __init__(self, progressive_scaling: bool, shuffle_chapter_difficulty: bool, double_damage: bool, quadruple_damage: bool,
        merlow_reward_pricing: bool, cap_enemy_xp: bool, xp_multiplier: float, one_hit_ko: bool, no_save_blocks: bool,
        no_heart_blocks: bool, no_healing_items: bool, starway_spirits_needed: int,
        require_specific_spirits: bool, limit_chapter_logic: bool, badge_synergy: bool, drop_star_points: bool,
        shuffle_star_beam: bool, star_beam_spirits_needed: bool, star_beam_power_stars_needed: bool
    ):

        if progressive_scaling:
            self.EnemyDifficulty = "Progressive Scaling"
        elif shuffle_chapter_difficulty:
            self.EnemyDifficulty = "Shuffle Chapter Difficulty"
        else:
            self.EnemyDifficulty = "Vanilla"

        if double_damage:
            self.EnemyDamage = "Double Pain"
        elif quadruple_damage:
            self.EnemyDamage = "Quadruple Pain"
        else:
            self.EnemyDamage = "Normal"

        self.MerlowRewardsPricing = merlow_reward_pricing
        self.CapEnemyXP = cap_enemy_xp
        self.XPMultiplier = xp_multiplier
        self.OneHitKO = one_hit_ko
        self.NoSaveBlocks = no_save_blocks
        self.NoHeartBlocks = no_heart_blocks
        self.NoHealingItems = no_healing_items
        self.DropStarPoints = drop_star_points
        self.RandomNumberOfRrequiredStarSpirits = starway_spirits_needed == -1
        self.StarSpiritsRequired = starway_spirits_needed
        self.RequireSpecificSpirits = require_specific_spirits
        self.LimitChapterLogic = limit_chapter_logic
        self.BadgeSynergy = badge_synergy

        self.ShuffleStarBeam = shuffle_star_beam
        self.StarBeamSpiritsNeeded = star_beam_spirits_needed
        self.StarBeamPowerStarsNeeded = star_beam_power_stars_needed
        
