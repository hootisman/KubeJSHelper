ITEM_STR = '''{{
    \"negative_effect\": {{
        \"minecraft:weakness\":3,
        \"minecraft:slowness\":3,
        \"minecraft:mining_fatigue\":3
    }},
    \"override\": false,
    \"isTagFor\": [
        \"#{0}\"
    ],
    \"requirements\": {{
        \"USE\": {{
        \"{1}\":{2}
        }},
        \"TOOL\": {{
        \"{1}\":{2}
        }},
        \"WEAPON\": {{
        \"{1}\":{2}
        }},
        \"PLACE\": {{
        \"{1}\":{2}
        }},
        \"BREAK\": {{
        \"{1}\":{2}
        }},
        \"INTERACT\": {{
        \"{1}\":{2}
        }},
        \"USE_ENCHANTMENT\": {{
        \"{1}\":{2}
        }}
    }}
}}
'''

ARMOR_STR = '''{{
    \"negative_effect\": {{
        \"minecraft:weakness\":3,
        \"minecraft:slowness\":3,
        \"minecraft:mining_fatigue\":3,
        \"minecraft:wither\":3,
        \"minecraft:blindness\":3
    }},
    \"override\": false,
    \"isTagFor\": [
        \"#{0}\"
    ],
    \"requirements\": {{
        \"USE\": {{
        \"{1}\":{2}
        }},
        \"WEAR\": {{
        \"{1}\":{2}
        }},
        \"INTERACT\": {{
        \"{1}\":{2}
        }},
        \"USE_ENCHANTMENT\": {{
        \"{1}\":{2}
        }}
    }}
}}
'''
BLOCK_STR = '''{{
    \"override\": false,
    \"isTagFor\": [
        \"#{0}\"
    ],
    \"requirements\": {{
        \"PLACE\": {{
        \"{1}\":{2}
        }},
        \"BREAK\": {{
        \"{1}\":{2}
        }},
        \"INTERACT\": {{
        \"{1}\":{2}
        }}
    }}
}}
'''
