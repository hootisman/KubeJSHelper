#!/bin/bash

SKILLS=("magic" "slayer" "fish" "attack" "alch" "mine" "eng" "def" "build" "smith" "wood" "ranged" "craft" "farm" "fly" "cook" "agility" "navi" "hunt" "tame" "stealth" "char" "myst")
OUTPUTS=()
#@param $1 name : name of skill
#@param $2 value : value of skill
#@param $3 idtype : type of tag to make ex: arm for armor, itm for item, etc.
addToFile() {
	output="./output/$1.js"
	if ! [ -f "$output" ]; then
		#CHANGE ITEM!!! WHEN WORKING WITH BLOCKS!!
		echo "ServerEvents.tags('item', event => {" >$output
		OUTPUTS+=("$1")
	fi

	echo -e "\tevent.add('pmmo:$1$2_$3','$items')" >>$output

}

encloseFile() {
	for skl in ${OUTPUTS[@]}; do
		echo "})" >>"./output/$skl.js"
	done
}

parseCSV() {

	while IFS="," read -r items magic slayer fish attack alch mine eng def build smith wood ranged craft farm fly cook agility navi hunt tame stealth char myst; do

		#echo "${!2}"

		# if [ -n "${!2}" ]; then
		# 	echo -e "\tevent.add('pmmo:magic10_$1','$items')" >>$output
		# fi
		#for each skill
		for skl in ${SKILLS[@]}; do
			#if object has value in skill
			echo $skl
			if [ -n "${!skl}" ]; then
				addToFile $skl ${!skl} $1
			fi
		done

	done < <(tail -n +2 "./sheets/$1.csv")

	encloseFile
}

read -p 'id type? ' idtype
# read -p 'skill? ' skill

rm -rf ./output/*

# parseCSV $idtype $skill
parseCSV $idtype
