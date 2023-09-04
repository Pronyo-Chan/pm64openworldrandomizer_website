class ItemPool:
    def __init__(self, item_trap_mode: int, random_consumable_mode: bool, item_quality: int):
        self.ItemTraps = item_trap_mode
        self.ConsumableItemPool = random_consumable_mode
        self.ItemQuality = item_quality
        
