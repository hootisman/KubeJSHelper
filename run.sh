#!/bin/bash

echo "converting .ods to sheets"
./convert_sheets.sh
echo "adding sheets to sheets/"

echo "generating skill reqs for: armor"
python scripts/skillsgen.py armor

echo "generating skill reqs for: item"
python scripts/skillsgen.py item

echo "generating skill reqs for: block"
python scripts/skillsgen.py block

echo "generating xp gains for: item"
python scripts/xpgains.py item

echo "generating xp gains for: block"
python scripts/xpgains.py block
