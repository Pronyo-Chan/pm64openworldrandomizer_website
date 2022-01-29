from rest_framework import serializers

from .models import Setting


class StartWithPartnersSerializer(serializers.Serializer):
    Goombario = serializers.BooleanField()
    Kooper = serializers.BooleanField()
    Bombette = serializers.BooleanField()
    Bow = serializers.BooleanField()
    Watt = serializers.BooleanField()
    Sushie = serializers.BooleanField()
    Lakilester = serializers.BooleanField()

class SettingSerializer(serializers.ModelSerializer):
    StartWithPartners = StartWithPartnersSerializer()

    class Meta:
        model = Setting
        fields = [
            "AlwaysSpeedySpin",
            "AlwaysISpy",
            "AlwaysPeekaboo",
            "HiddenBlockMode",
            "AllowPhysicsGlitches",
            "InitialCoins",
            "CapEnemyXP",
            "NoXP",
            "DoubleDamage",
            "QuadrupleDamage",
            "OHKO",
            "NoSaveBlocks",
            "NoHeartBlock",
            "FlowerGateOpen",
            "BlueHouseOpen",
            "ToyboxOpen",
            "WhaleOpen",
            "ShuffleChapterDifficulty",
            "ProgressiveScaling",
            "RandomFormations",
            "ShuffleItems",
            "IncludeCoins",
            "IncludeShops",
            "IncludePanels",
            "IncludeFavors",
            "IncludeLetterChain",
            "KeyitemsOutsideDungeon",
            "ShuffleBadgesBP",
            "ShuffleBadgesFP",
            "ShufflePartnerFP",
            "ShuffleStarpowerSP",
            "RandomQuiz",
            "SkipQuiz",
            "QuizmoAlwaysAppears",
            "PartnersInDefaultLocations",
            "PartnersAlwaysUsable",
            "StartWithRandomPartners",
            "RandomPartnersMin",
            "RandomPartnersMax",
            "StartWithPartners",
            "WriteSpoilerLog",
            "RandomCoinPalette",
            "RomanNumerals",
            "TurnOffMusic",
            "IncludeDojo",
        ]

    def create(self):
        starting_partners = self.validated_data.pop("StartWithPartners")
        self.validated_data["StartWithGoombario"] = starting_partners.get("Goombario")
        self.validated_data["StartWithKooper"] = starting_partners.get("Kooper")
        self.validated_data["StartWithBombette"] = starting_partners.get("Bombette")
        self.validated_data["StartWithBow"] = starting_partners.get("Bow")
        self.validated_data["StartWithWatt"] = starting_partners.get("Watt")
        self.validated_data["StartWithSushie"] = starting_partners.get("Sushie")
        self.validated_data["StartWithLakilester"] = starting_partners.get("Lakilester")
        return Setting(**self.validated_data)

    def validate_InitialCoins(self, value):
        if value < 0 or value > 999:
            raise serializers.ValidationError("Initial Coins must be between 0 and 999")
        return value

    def validate_RandomPartnersMin(self, value):
        if value < 1 or value > 8:
            raise serializers.ValidationError("Random Partners Min must be between 1 and 8")
        return value

    def validate_RandomPartnersMax(self, value):
        if value < 1 or value > 8:
            raise serializers.ValidationError("Random Partners Min must be between 1 and 8")
        return value