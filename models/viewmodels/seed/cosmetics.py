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
    0: "Green",
    1: "Red",
    2: "Purple",
    3: "Grey",
}

bombette_color_choices = {
    0: "Default",
    1: "Orange",
    2: "Purple",
    3: "Green",
    4: "Yellow",
    5: "Blue"
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
    3: "Green"
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

def get_character_color_description(character_setting, character_sprite, character_color_choices):
    if character_setting == 0:
        return "Default"

    elif character_setting == 1:
        return character_color_choices[character_sprite]

    elif character_setting == 2:
        return "Random Pick"

    elif character_setting == 3:
        return "Random Pick (No Vanilla)"

    elif character_setting == 4:
        return "Random On Every Load"
            
class Cosmetics:

    def __init__(
        self, mario_setting: int, mario_sprite: int, goombario_setting: int, goombario_sprite: int,
        kooper_setting: int, kooper_sprite: int, bombette_setting: int, bombette_sprite: int,
        parakarry_setting: int, parakarry_sprite: int, bow_setting: int, bow_sprite: int,
        watt_setting: int, watt_sprite: int, sushie_setting: int, sushie_sprite: int,
        bosses_setting: int, enemies_setting: int, npc_setting: int, box5_color_a: int,
        coin_color: int, random_coin_color: bool
    ):

        self.Mario = get_character_color_description(mario_setting, mario_sprite, mario_color_choices)
        self.Goombario = get_character_color_description(goombario_setting, goombario_sprite, goombario_color_choices)
        self.Kooper = get_character_color_description(kooper_setting, kooper_sprite, kooper_color_choices)
        self.Bombette = get_character_color_description(bombette_setting, bombette_sprite, bombette_color_choices)
        self.Parakarry = get_character_color_description(parakarry_setting, parakarry_sprite, parakarry_color_choices)
        self.Bow = get_character_color_description(bow_setting, bow_sprite, bow_color_choices)
        self.Watt = get_character_color_description(watt_setting, watt_sprite, watt_color_choices)
        self.Sushie = get_character_color_description(sushie_setting, sushie_sprite, sushie_color_choices)
        self.Bosses = bosses_setting
        self.NPC = npc_setting
        self.Enemies = enemies_setting

        self.StatusMenu = box_colors.get(box5_color_a)
        self.CoinColor = "Random" if random_coin_color else coin_colors.get(coin_color)
