class Items:
    def __init__(self, add_item_pouches: bool, gear_shuffle_mode: int, include_coins: bool, include_dojo: bool, include_favors_mode: int,
        include_letters_mode: int, include_panels: bool, include_radio_trade_events: bool, include_shops: bool, key_items_outside_dungeon: bool,
        shuffle_blocks: bool, shuffle_items: bool, rip_cheato_items_in_logic
    ):

        self.ShuffleItems = shuffle_items
        self.Coinsanity = include_coins
        self.Shopsanity = include_shops
        self.IncludeHiddenPanels = include_panels
        self.Keysanity = key_items_outside_dungeon
        self.IncludeDojoRewards = include_dojo
        self.AddItemPouches = add_item_pouches
        self.IncludeTradingEventRewards = include_radio_trade_events
        self.ShuffleSuperAndMulticoinBlocks = shuffle_blocks
        self.GearShuffle = gear_shuffle_mode
        self.LetterDeliveryRewards = include_letters_mode
        self.KoopaKootFavors = include_favors_mode
        self.RipCheatoItemsInLogic = rip_cheato_items_in_logic
