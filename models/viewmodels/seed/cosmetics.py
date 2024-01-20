mario_color_choices = {
    0: "Default",
    1: "Luigi",
    2: "Wario",
    3: "Waluigi",
    4: "Fire",
    5: "Ice",
    6: "Maker",
    7: "Classic"
}

goombario_color_choices = {
    0: "Default",
    1: "Green",
    2: "Red",
    3: "Yellow",
    4: "Blue",
    5: "Grey"
}

kooper_color_choices = {
    0: "Default",
    1: "Green",
    2: "Red",
    3: "Purple",
    4: "Grey",
}

bombette_color_choices = {
    0: "Default",
    1: "Orange",
    2: "Green",
    3: "Yellow",
    4: "Blue",
    5: "Red",
    6: "Purple"
}

parakarry_color_choices = {
    0: "Default",
    1: "Green",
    2: "Red",
    3: "Purple"
}

bow_color_choices = {
    0: "Default",
    1: "Red",
    2: "Pink",
    3: "Blue",
    4: "Grey"
}

watt_color_choices = {
    0: "Default",
    1: "Blue",
    2: "Pink",
    3: "Green"
}

sushie_color_choices = {
    0: "Default",
    1: "Red",
    2: "Yellow",
    3: "Green",
    4: "Blue"
}

lakilester_color_choices = {
    0: "Default",
    1: "Blue",
    2: "Dark",
    3: "Red",
    4: "Green"
}

box_colors = {
    0xEBE677FF : "Default",
    0x8D8FFFFF : "Blue",
    0xAAD080FF : "Green",
    0x8ED4ECFF : "Teal",
    0xD7BF74FF : "Brown",
    0xB797B7FF : "Purple",
    0xC0C0C0FF : "Grey",
}

coin_colors = {
    0 : "Default",
    1 : "Red",
    2 : "Blue",
    3 : "Purple",
    4 : "Silver"
}

def get_box_color(color_mode, box5_color_a):
    if color_mode == 0:
        return box_colors.get(box5_color_a)

    elif color_mode == 1:
        return "Random Pick"

    if color_mode == 2:
        return "Animated"

def get_palette_description(setting, sprite = None, character_color_choices = None):
    if setting == 0:
        return "Default"

    elif setting == 1:
        return character_color_choices[sprite]

    elif setting == 2:
        return "Random Pick"

    elif setting == 3:
        return "Random Pick (No Vanilla)"

    elif setting == 4:
        return "Random On Every Load"
    
    else:
        return "Default"
        #raise Exception(f"Couldn't find description for palette with setting: {setting}, sprite: {sprite}, color choices: {character_color_choices}")

def get_shuffle_music_description(shuffle_music, shuffle_music_mode):
    if not shuffle_music:
        return "Off"
    
    if shuffle_music_mode == 0:
        return "Shuffle By Mood"
    
    if shuffle_music_mode == 1:
        return "Shuffle By Type"
    
    if shuffle_music_mode == 2:
        return "Full Shuffle"
    
            
class Cosmetics:

    def __init__(
        self, mario_setting: int, mario_sprite: int, goombario_setting: int, goombario_sprite: int,
        kooper_setting: int, kooper_sprite: int, bombette_setting: int, bombette_sprite: int,
        parakarry_setting: int, parakarry_sprite: int, bow_setting: int, bow_sprite: int,
        watt_setting: int, watt_sprite: int, sushie_setting: int, sushie_sprite: int,
        lakilester_setting: int, lakilester_sprite: int, bosses_setting: int,
        enemies_setting: int, hammer_setting: int, npc_setting: int, color_mode: int, box5_color_a: int,
        coin_color: int, random_coin_color: bool, random_text: bool, roman_numerals: bool,
        random_pitch: bool, shuffle_music: bool, shuffle_music_mode: int, shuffle_jingles: bool, mute_danger_beeps: bool
    ):

        self.Mario = get_palette_description(mario_setting, mario_sprite, mario_color_choices)
        self.Goombario = get_palette_description(goombario_setting, goombario_sprite, goombario_color_choices)
        self.Kooper = get_palette_description(kooper_setting, kooper_sprite, kooper_color_choices)
        self.Bombette = get_palette_description(bombette_setting, bombette_sprite, bombette_color_choices)
        self.Parakarry = get_palette_description(parakarry_setting, parakarry_sprite, parakarry_color_choices)
        self.Bow = get_palette_description(bow_setting, bow_sprite, bow_color_choices)
        self.Watt = get_palette_description(watt_setting, watt_sprite, watt_color_choices)
        self.Sushie = get_palette_description(sushie_setting, sushie_sprite, sushie_color_choices)
        self.Lakilester = get_palette_description(lakilester_setting, lakilester_sprite, lakilester_color_choices)
        
        self.Bosses = get_palette_description(bosses_setting)
        self.NPC = get_palette_description(npc_setting)
        self.Enemies = get_palette_description(enemies_setting)
        self.Hammer = get_palette_description(hammer_setting)

        self.StatusMenu = get_box_color(color_mode, box5_color_a)
        self.CoinColor = "Random Pick" if random_coin_color else coin_colors.get(coin_color)

        self.RandomText = random_text
        self.RomanNumerals = roman_numerals
        self.RandomPitch = random_pitch
        self.MuteDangerBeeps = mute_danger_beeps
        self.ShuffleMusic = get_shuffle_music_description(shuffle_music, shuffle_music_mode)
        self.ShuffleJingles = shuffle_jingles
