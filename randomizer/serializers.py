from rest_framework import serializers

from .models import Setting


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = [
            "name",
            "version",
            "seed",
            "starting_map",
            "replace_duplicate_keys",
            "duplicate_key_replacement",
            "blocks_match_content",
            "initial_coins",
            "cap_enemy_xp",
            "damage_2x",
            "damage_4x",
            "one_hit_ko",
            "flower_gate_open",
            "blue_house_open",
            "placement_algorithm",
            "placement_logic",
            "shuffle_items",
            "include_coins",
            "include_shops",
            "include_panels",
            "key_items_outside_area",
            "key_items_outside_chapter",
            "shuffle_entrances",
            "shuffle_entrances_by_area",
            "shuffle_entrances_by_all",
            "match_entrance_types",
            "randomize_oneway_entrances",
            "unpaired_entrances",
            "random_quiz",
            "skip_quiz",
            "start_with_random_partners",
            "random_partners_min",
            "random_partners_max",
            "start_with_goombario",
            "start_with_kooper",
            "start_with_bombette",
            "start_with_parakarry",
            "start_with_bow",
            "start_with_watt",
            "start_with_sushie",
            "start_with_lakilester",
            "spoiler_log",
            "pretty_spoiler_log",
            "color_a",
            "color_b",
        ]

    def create(self):
        return Setting(**self.validated_data)

    def validate_initial_coins(self, value):
        if value < 0 or value > 999:
            raise serializers.ValidationError("Initial Coins must be between 0 and 999")
        return value

    def validate_random_partners_min(self, value):
        if value < 1 or value > 8:
            raise serializers.ValidationError("Random Partners Min must be between 1 and 8")
        return value

    def validate_random_partners_max(self, value):
        if value < 1 or value > 8:
            raise serializers.ValidationError("Random Partners Min must be between 1 and 8")
        return value