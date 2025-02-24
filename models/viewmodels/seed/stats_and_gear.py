class StatsAndGear:
    def __init__(
        self,
        starting_boots: int,
        starting_hammer: int,
        starting_coins: int,
        starting_max_hp: int,
        starting_max_bp: int,
        starting_max_fp: int,
        random_starting_stats_level: int,
        starting_star_power: int,
        start_with_random_items: bool,
        random_items_min: int,
        random_items_max: int,
        starting_item_0: int,
        starting_item_1: int,
        starting_item_2: int,
        starting_item_3: int,
        starting_item_4: int,
        starting_item_5: int,
        starting_item_6: int,
        starting_item_7: int,
        starting_item_8: int,
        starting_item_9: int,
        starting_item_A: int,
        starting_item_B: int,
        starting_item_C: int,
        starting_item_D: int,
        starting_item_E: int,
        starting_item_F: int,
    ):

        self.Boots = starting_boots
        self.Hammer = starting_hammer
        self.Coins = starting_coins
        self.HP = starting_max_hp
        self.BP = starting_max_bp
        self.FP = starting_max_fp
        self.StarPower = starting_star_power

        self.RandomStartingStatsLevel = random_starting_stats_level

        self.StartingItems = []

        if not start_with_random_items:
            if starting_item_0:
                self.StartingItems.append(starting_item_0)
            if starting_item_1:
                self.StartingItems.append(starting_item_1)
            if starting_item_2:
                self.StartingItems.append(starting_item_2)
            if starting_item_3:
                self.StartingItems.append(starting_item_3)
            if starting_item_4:
                self.StartingItems.append(starting_item_4)
            if starting_item_5:
                self.StartingItems.append(starting_item_5)
            if starting_item_6:
                self.StartingItems.append(starting_item_6)
            if starting_item_7:
                self.StartingItems.append(starting_item_7)
            if starting_item_8:
                self.StartingItems.append(starting_item_8)
            if starting_item_9:
                self.StartingItems.append(starting_item_9)
            if starting_item_A:
                self.StartingItems.append(starting_item_A)
            if starting_item_B:
                self.StartingItems.append(starting_item_B)
            if starting_item_C:
                self.StartingItems.append(starting_item_C)
            if starting_item_D:
                self.StartingItems.append(starting_item_D)
            if starting_item_E:
                self.StartingItems.append(starting_item_E)
            if starting_item_F:
                self.StartingItems.append(starting_item_F)
        else:
            self.StartingItems.append("Random")
            self.MinNumberOfStartingItems = random_items_min
            self.MaxNumberOfStartingItems = random_items_max
        