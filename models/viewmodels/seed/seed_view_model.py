from models.viewmodels.seed.goals import Goals
from models.viewmodels.seed.item_pool import ItemPool
from models.viewmodels.seed.stats_and_gear import StatsAndGear
from models.viewmodels.seed.cosmetics import Cosmetics
from models.viewmodels.seed.general_difficulty import GeneralDifficulty
from models.viewmodels.seed.open_world import World
from models.viewmodels.seed.partners import Partners
from models.viewmodels.seed.items import Items
from models.viewmodels.seed.gameplay import Gameplay
from models.viewmodels.seed.glitches import glitches_names
from models.viewmodels.seed.quality_of_life import QualityOfLife
from models.viewmodels.seed.seed_info import SeedInfo
from models.viewmodels.seed.spoiler import Spoiler

class SeedViewModel:
    def __init__(self, seed_document: dict):

        self.SeedInfo = SeedInfo(
            seed_id = seed_document["SeedID"],
            creation_date = seed_document["CreationDate"],
            seed_hash_items = seed_document["SeedHashItems"],
            settings_string = seed_document["SettingsString"],
            star_rod_mod_version = seed_document["StarRodModVersion"],
            is_plandomizer_seed = seed_document.get("IsPlandomizerSeed")
        ).__dict__

        self.Items = Items(
            gear_shuffle_mode = seed_document["GearShuffleMode"],
            partner_upgrade_shuffle = seed_document.get("PartnerUpgradeShuffle"),
            include_coins_overworld = seed_document.get("IncludeCoinsOverworld"),
            include_coins_blocks = seed_document.get("IncludeCoinsBlocks"),
            include_coins_favors = seed_document.get("IncludeCoinsFavors"),
            include_coins_foliage = seed_document.get("IncludeCoinsFoliage"),
            include_dojo = int(seed_document["IncludeDojo"]),
            include_favors_mode = seed_document["IncludeFavorsMode"],
            include_letters_mode = seed_document["IncludeLettersMode"],
            include_panels = seed_document["IncludePanels"],
            include_radio_trade_events = seed_document["IncludeRadioTradeEvent"],
            include_shops = seed_document["IncludeShops"],
            key_items_outside_dungeon = seed_document["KeyitemsOutsideDungeon"],
            rip_cheato_items_in_logic = seed_document["RipCheatoItemsInLogic"],
            shuffle_blocks = seed_document.get("ShuffleBlocks"),
            multi_coin_block_shuffle = seed_document.get("MultiCoinBlockShuffle"),
            shuffle_items = seed_document["ShuffleItems"],
            progression_on_merlow = seed_document.get("ProgressionOnMerlow"),
            progression_on_rowf = int(seed_document.get("ProgressionOnRowf")),
        ).__dict__

        self.Partners = Partners(
            partners_in_default_locations = seed_document.get("PartnersInDefaultLocations"), #TODO: Remove after no seeds with this setting remain
            partner_shuffle = seed_document.get("PartnerShuffle"),
            partners_always_usable = seed_document["PartnersAlwaysUsable"],
            random_partners_max = seed_document.get("RandomPartnersMax"),
            random_partners_min = seed_document.get("RandomPartnersMin"),
            start_with_random_partners = seed_document["StartWithRandomPartners"],
            start_with_partners = seed_document.get("StartWithPartners")
        ).__dict__

        self.Gameplay = Gameplay(
            random_badges_bp = seed_document["RandomBadgesBP"],
            random_badges_fp = seed_document["RandomBadgesFP"],
            random_partner_fp = seed_document["RandomPartnerFP"],
            random_starpower_sp = seed_document["RandomStarpowerSP"],
            random_formations = seed_document["RandomFormations"],
            mystery_random_pick = seed_document["MysteryRandomPick"],
            random_choice = seed_document["RandomChoice"],
            randomize_puzzles = seed_document.get("RandomizePuzzles"),
            boss_shuffle_mode = seed_document.get("BossShuffleMode")
        ).__dict__

        self.Cosmetics = Cosmetics(
            mario_setting = seed_document["MarioSetting"],
            mario_sprite = seed_document["MarioSprite"],
            goombario_setting = seed_document["GoombarioSetting"],
            goombario_sprite = seed_document["GoombarioSprite"],
            kooper_setting = seed_document["KooperSetting"],
            kooper_sprite = seed_document["KooperSprite"],
            bombette_setting = seed_document["BombetteSetting"],
            bombette_sprite = seed_document["BombetteSprite"],
            parakarry_setting = seed_document["ParakarrySetting"],
            parakarry_sprite = seed_document["ParakarrySprite"],
            bow_setting = seed_document["BowSetting"],
            bow_sprite = seed_document["BowSprite"],
            watt_setting = seed_document["WattSetting"],
            watt_sprite = seed_document["WattSprite"],
            sushie_setting = seed_document["SushieSetting"],
            sushie_sprite = seed_document["SushieSprite"],
            lakilester_setting = seed_document.get("LakilesterSetting"),
            lakilester_sprite = seed_document.get("LakilesterSprite"),
            bosses_setting = seed_document["BossesSetting"],
            npc_setting = seed_document["NPCSetting"],
            enemies_setting = seed_document["EnemiesSetting"],
            hammer_setting = seed_document.get("HammerSetting"),
            coin_color = seed_document["CoinColor"],
            random_coin_color = seed_document["RandomCoinColor"],
            color_mode = seed_document.get("ColorMode"),
            box5_color_a = seed_document["Box5ColorA"],
            roman_numerals = seed_document["RomanNumerals"],
            random_text = seed_document["RandomText"],
            random_pitch = seed_document["RandomPitch"],
            mute_danger_beeps = seed_document.get("MuteDangerBeeps"),
            shuffle_music = seed_document.get("ShuffleMusic"),
            shuffle_music_mode = seed_document.get("ShuffleMusicMode"),
            shuffle_jingles = seed_document.get("ShuffleJingles"),
        ).__dict__

        self.Glitches = [g for g in glitches_names if seed_document.get(g) is True]

        self.GeneralDifficulty = GeneralDifficulty(
            progressive_scaling = seed_document["ProgressiveScaling"],
            shuffle_chapter_difficulty = seed_document["ShuffleChapterDifficulty"],
            double_damage = seed_document["DoubleDamage"],
            quadruple_damage = seed_document["QuadrupleDamage"],
            merlow_reward_pricing = seed_document["MerlowRewardPricing"],
            cap_enemy_xp = seed_document["CapEnemyXP"],
            xp_multiplier = seed_document.get("XPMultiplier"),
            one_hit_ko = seed_document["OHKO"],
            no_save_blocks = seed_document["NoSaveBlocks"],
            no_heart_blocks = seed_document["NoHeartBlocks"],
            no_healing_items = seed_document["NoHealingItems"],
            badge_synergy = seed_document.get("BadgeSynergy"),
            drop_star_points = seed_document.get("DropStarPoints"),
            chet_rippo_available = seed_document.get("ChetRippoAvailable"),
            bowser_door_quiz = seed_document.get("BowserDoorQuiz"),
            kent_c_koopa = seed_document.get("KentCKoopa")
        ).__dict__

        self.Goals = Goals(
            starway_spirits_needed = seed_document.get("StarWaySpiritsNeededCnt"),
            require_spirits = seed_document.get("RequiredSpirits"),
            shuffle_star_beam = seed_document.get("ShuffleStarBeam"),
            star_beam_spirits_needed = seed_document.get("StarBeamSpiritsNeeded"),
            star_beam_power_stars_needed = seed_document.get("StarBeamPowerStarsNeeded"),            
            seed_goal = seed_document.get("SeedGoal"),
            starway_power_stars_needed = seed_document.get("StarWayPowerStarsNeeded"),
            star_hunt_total = seed_document.get("StarHuntTotal"),
        ).__dict__

        self.ItemPool = ItemPool(
            item_trap_mode = seed_document["ItemTrapMode"],
            random_consumable_mode = seed_document["RandomConsumableMode"],
            item_quality = seed_document["ItemQuality"],
            add_item_pouches = seed_document["AddItemPouches"],
            add_unused_badge_duplicates = seed_document.get("AddUnusedBadgeDuplicates"),
            add_beta_items = seed_document.get("AddBetaItems"),
            progressive_badges = seed_document.get("ProgressiveBadges"),
            badge_pool_limit = seed_document.get("BadgePoolLimit")
        ).__dict__

        self.StatsAndGear = StatsAndGear(
            starting_boots = seed_document["StartingBoots"],
            starting_hammer = seed_document["StartingHammer"],
            starting_coins = seed_document["StartingCoins"],
            starting_max_hp = seed_document["StartingMaxHP"],
            starting_max_bp = seed_document["StartingMaxBP"],
            starting_max_fp = seed_document["StartingMaxFP"],
            random_starting_stats_level = seed_document.get("RandomStartingStatsLevel"),
            starting_star_power = seed_document["StartingStarPower"],
            start_with_random_items = seed_document["StartWithRandomItems"],
            random_items_min = seed_document["RandomItemsMin"],
            random_items_max = seed_document["RandomItemsMax"],
            starting_item_0 = seed_document["StartingItem0"],
            starting_item_1 = seed_document["StartingItem1"],
            starting_item_2 = seed_document["StartingItem2"],
            starting_item_3 = seed_document["StartingItem3"],
            starting_item_4 = seed_document["StartingItem4"],
            starting_item_5 = seed_document["StartingItem5"],
            starting_item_6 = seed_document["StartingItem6"],
            starting_item_7 = seed_document["StartingItem7"],
            starting_item_8 = seed_document["StartingItem8"],
            starting_item_9 = seed_document["StartingItem9"],
            starting_item_A = seed_document["StartingItemA"],
            starting_item_B = seed_document["StartingItemB"],
            starting_item_C = seed_document["StartingItemC"],
            starting_item_D = seed_document["StartingItemD"],
            starting_item_E = seed_document["StartingItemE"],
            starting_item_F = seed_document["StartingItemF"]
        ).__dict__

        self.World = World(
            starting_location = seed_document["StartingMap"],
            magical_seeds_required = seed_document["MagicalSeedsRequired"],
            blue_house_open = seed_document["BlueHouseOpen"],
            toybox_open = seed_document["ToyboxOpen"],
            prologue_open = seed_document["PrologueOpen"],
            whale_open = seed_document["WhaleOpen"],
            ch7_bridge_visible = seed_document.get("Ch7BridgeVisible"),
            mt_rugged_open = seed_document.get("MtRuggedOpen"),
            forever_forest_open = seed_document.get("ForeverForestOpen"),
            bowsers_castle_mode = seed_document["BowsersCastleMode"],
            shuffle_dungeon_entrances = int(seed_document.get("ShuffleDungeonEntrances")),
            mirror_mode = seed_document.get("MirrorMode"),
            static_map_mirroring = seed_document.get("StaticMapMirroring"),
        ).__dict__

        self.QualityOfLife = QualityOfLife(
            hidden_block_mode = seed_document["HiddenBlockMode"],
            always_speedy_spin = seed_document["AlwaysSpeedySpin"],
            allow_physics_glitches = seed_document["AllowPhysicsGlitches"],
            always_peekaboo = seed_document["AlwaysPeekaboo"],
            skip_quiz = seed_document["SkipQuiz"],
            always_i_spy = seed_document["AlwaysISpy"],
            quizmo_always_appears = seed_document["QuizmoAlwaysAppears"],
            foliage_item_hints = seed_document["FoliageItemHints"],
            hidden_panel_visibility = seed_document["HiddenPanelVisibility"],
            i_spy_panel_hints = seed_document.get("ISpyPanelHints"),
            cook_without_frying_pan = seed_document["CookWithoutFryingPan"],
            shorten_cutscenes = seed_document.get("ShortenCutscenes"),
            cutscene_mode = seed_document.get("CutsceneMode"),
            skip_epilogue = seed_document["SkipEpilogue"],
        ).__dict__

        self.Spoiler = Spoiler(
            include_spoiler_log = seed_document["WriteSpoilerLog"],
            allow_item_hints = seed_document["AllowItemHints"],
            reveal_log_at_time = seed_document.get("RevealLogAtTime") # nullable
        ).__dict__
        