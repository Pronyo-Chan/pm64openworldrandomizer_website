from models.viewmodels.seed.cosmetics import Cosmetics
from models.viewmodels.seed.partners import Partners
from models.viewmodels.seed.items import Items
from models.viewmodels.seed.gameplay import Gameplay
from models.viewmodels.seed.glitches import glitches_names

class SeedViewModel:
    def __init__(self, seed_document: dict):
        self.Items = Items(
            add_item_pouches = seed_document["AddItemPouches"],
            gear_shuffle_mode = seed_document["GearShuffleMode"],
            include_coins= seed_document["IncludeCoins"],
            include_dojo = seed_document["IncludeDojo"],
            include_favors_mode = seed_document["IncludeFavorsMode"],
            include_letters_mode = seed_document["IncludeLettersMode"],
            include_panels = seed_document["IncludePanels"],
            include_radio_trade_events = seed_document["IncludeRadioTradeEvent"],
            include_shops = seed_document["IncludeShops"],
            key_items_outside_dungeon = seed_document["KeyitemsOutsideDungeon"],
            rip_cheato_items_in_logic = seed_document["RipCheatoItemsInLogic"],
            shuffle_blocks = seed_document["ShuffleBlocks"],
            shuffle_items = seed_document["ShuffleItems"]
        ).__dict__

        self.Partners = Partners(
            partners_in_default_locations = seed_document["PartnersInDefaultLocations"],
            partners_always_usable = seed_document["PartnersAlwaysUsable"],
            random_partners_max = seed_document["RandomPartnersMax"],
            random_partners_min = seed_document["RandomPartnersMin"],
            start_with_random_partners = seed_document["StartWithRandomPartners"]
        ).__dict__

        self.Gameplay = Gameplay(
            random_badges_bp = seed_document["RandomBadgesBP"],
            random_badges_fp = seed_document["RandomBadgesFP"],
            random_partner_fp = seed_document["RandomPartnerFP"],
            random_starpower_sp = seed_document["RandomStarpowerSP"],
            random_formations = seed_document["RandomFormations"],
            mystery_random_pick = seed_document["MysteryRandomPick"],
            random_choice = seed_document["RandomChoice"]
        ).__dict__

        self.Cosmetics = Cosmetics(
            mario_setting = seed_document["MarioSetting"],
            mario_sprite = seed_document["MarioSprite"],
            goombario_setting = seed_document["GoombarioSetting"],
            goombario_sprite = seed_document["GoombarioSprite"],
            kooper_setting = seed_document["KooperSetting"],
            kooper_sprite = seed_document["KooperSprite"],
            bombette_sprite = seed_document["BombetteSetting"],
            bombette_setting = seed_document["BombetteSprite"],
            parakarry_setting = seed_document["ParakarrySetting"],
            parakarry_sprite = seed_document["ParakarrySprite"],
            bow_setting = seed_document["BowSetting"],
            bow_sprite = seed_document["BowSprite"],
            watt_setting = seed_document["WattSetting"],
            watt_sprite = seed_document["WattSprite"],
            sushie_setting = seed_document["SushieSetting"],
            sushie_sprite = seed_document["SushieSprite"],
            bosses_setting = seed_document["BossesSetting"],
            npc_setting = seed_document["NPCSetting"],
            enemies_setting = seed_document["EnemiesSetting"],
            coin_color = seed_document["CoinColor"],
            random_coin_color = seed_document["RandomCoinColor"],
            box5_color_a = seed_document["Box5ColorA"]
        ).__dict__

        self.Glitches = [g for g in glitches_names if seed_document[g] is True]
        