class ItemPool:
    def __init__(self, item_trap_mode: int, random_consumable_mode: bool, item_quality: int, add_item_pouches: bool,
        add_unused_badge_duplicates: bool, add_beta_items: bool, progressive_badges: bool, badge_pool_limit: int
    ):
        self.ItemTraps = item_trap_mode
        self.ConsumableItemPool = random_consumable_mode
        self.ItemQuality = item_quality
        self.AddItemPouches = add_item_pouches
        self.AddUnusedBadgeDuplicates = add_unused_badge_duplicates
        self.AddBetaItems = add_beta_items
        self.ProgressiveBadges = progressive_badges
        self.BadgePoolLimit = badge_pool_limit
        
