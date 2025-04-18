starting_maps = {
    0x00010104: "Toad Town", # mac_00 (4)
    0x00000101: "Goomba Village", # kmr_02 (1)
    0x00090100: "Dry Dry Outpost", # dro_02 (0)
    0x00110302: "YoshiVillage", # jan_03 (2)
    0xFFFFFFFF: "Random"
}

class World:
    def __init__(
        self,
        starting_location: int,
        magical_seeds_required: int,
        blue_house_open: bool, 
        toybox_open: bool, 
        prologue_open: bool, 
        whale_open: bool,
        ch7_bridge_visible: bool,
        mt_rugged_open: bool,
        forever_forest_open: bool,
        bowsers_castle_mode: bool,
        shuffle_dungeon_entrances: int,
        mirror_mode: int,
        static_map_mirroring: bool
    ):

        self.StartingLocation = starting_maps.get(starting_location)
        self.MagicalSeedsRequired = "Random" if magical_seeds_required == -1 else str(magical_seeds_required)
        self.OpenBlueHouse = blue_house_open
        self.OpenToyBox = toybox_open
        self.OpenPrologue = prologue_open
        self.OpenWhale = whale_open
        self.Ch7BridgeVisible = ch7_bridge_visible
        self.OpenMtRugged = mt_rugged_open
        self.OpenForeverForest = forever_forest_open
        self.BowsersCastleMode = bowsers_castle_mode
        self.ShuffleDungeonEntrances = shuffle_dungeon_entrances
        self.MirrorMode = 3 if static_map_mirroring else mirror_mode
