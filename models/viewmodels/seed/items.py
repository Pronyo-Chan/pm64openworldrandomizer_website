class Items:
    def __init__(self,gear_shuffle_mode: int, include_coins_overworld: bool, include_coins_blocks: bool, include_coins_favors: bool, include_coins_foliage: bool,
        include_dojo: int, include_favors_mode: int, include_letters_mode: int, include_panels: bool, include_radio_trade_events: bool, partner_upgrade_shuffle: int,
        include_shops: bool, key_items_outside_dungeon: bool, shuffle_blocks: bool, multi_coin_block_shuffle: int, shuffle_items: bool, rip_cheato_items_in_logic: bool, progression_on_rowf: int, progression_on_merlow: bool,
    ):

        self.ShuffleItems = shuffle_items
        self.IncludeCoinsOverworld = include_coins_overworld
        self.IncludeCoinsBlocks = include_coins_blocks
        self.IncludeCoinsFavors = include_coins_favors
        self.IncludeCoinsFoliage = include_coins_foliage
        self.Shopsanity = include_shops
        self.IncludeHiddenPanels = include_panels
        self.Keysanity = key_items_outside_dungeon
        self.IncludeDojoRewards = include_dojo
        self.IncludeTradingEventRewards = include_radio_trade_events
        self.ShuffleSuperAndMulticoinBlocks = shuffle_blocks if shuffle_blocks else multi_coin_block_shuffle
        self.GearShuffle = gear_shuffle_mode
        self.LetterDeliveryRewards = include_letters_mode
        self.KoopaKootFavors = include_favors_mode
        self.RipCheatoItemsInLogic = rip_cheato_items_in_logic
        self.ProgressionOnRowf = progression_on_rowf
        self.ProgressionOnMerlow = progression_on_merlow
        self.PartnerUpgradeShuffle = partner_upgrade_shuffle
