from datetime import datetime, timezone, timedelta

def build_database_seed(seed_request, rando_result):
    seed_result = rando_result.web_settings
    seed_result["PaletteOffset"] = rando_result.palette_offset
    seed_result["CosmeticsOffset"] = rando_result.cosmetics_offset
    seed_result["AudioOffset"] = rando_result.audio_offset
    seed_result["MusicOffset"] = rando_result.music_offset
    seed_result["SeedHashItems"] = rando_result.hash_items

    seed_result["SeedID"] = seed_request["SeedID"]
    seed_result["CreationDate"] = datetime.now(timezone.utc)
    seed_result["StarRodModVersion"] = seed_request["StarRodModVersion"]
    seed_result["SettingsString"] = seed_request.get("SettingsString")
    if seed_request.get("WriteSpoilerLog") and seed_request.get("RevealLogInHours") != 0:
        seed_result["RevealLogAtTime"] = datetime.now(timezone.utc) + timedelta(hours = seed_request["RevealLogInHours"])
    seed_result["SeedValue"] = seed_request["SeedValue"]

    return seed_result