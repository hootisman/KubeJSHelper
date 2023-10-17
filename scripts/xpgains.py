import csv
import os
import sys
import shutil
import datapackstrs
from collections import defaultdict

PARENTDIR = os.getcwd()
SKILLS = ["magic", "slayer", "fish", "attack", "alch", "mine", "eng", "def", "build", "smith", "wood", "ranged", "craft", "farm", "fly", "cook", "agility", "navi", "hunt", "tame", "stealth", "char", "myst"]
SKILLIDS = dict(zip(SKILLS,["magic","slayer","fishing","attack","alchemy","mining","engineering","defence","building","smithing","woodcutting","ranged","crafting","farming","flying","cooking","agility","navigation","hunter","taming","stealth","charisma","mysticcrafting"]))
OUTPUTS = []
DATAPACK_LOC = PARENTDIR + "/datapack/"

def parse_csv(idtype):
    """
    opens csv file for xp gains, then creates .json files for each skill, xp type, and value
    """
    with open(PARENTDIR + '/sheets/' + idtype + '_xp.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        #for each datapoint in csv
        for row in reader:
            #gets and removes object ID from current row; item = object ID, row = skills with xp value
            item = row["items"]
            xptype = row["xp"]

            row.pop("items") #gets rid of 'items' col from row
            row.pop("xp")

            skills={k:v for k,v in row.items() if v.isnumeric()} #skills to add xp gains 
            for skill,xpval in skills.items():
                add_skill_xp(idtype, xptype, item, skill, xpval)
        enclose_files()
def add_skill_xp(idtype,xptype,item,skill,xpval):
    """
    Parameters
    ----------
    idtype : string
    type of object xp gain is being set for. ex: block, item

    xptype : string
    type of xp gain we are setting ex: 'ANVIL_REPAIR' , 'BREW' , etc.

    item : string
    item we are setting ex: minecraft:diamond

    skill : string
    skill we are setting ex: 'myst' , 'fish' NOTE: to convert to skill names used by pmmo, do 'SKILLIDS[skill]'

    xpval : int 
    value of xp we are setting ex: 1000, 640, etc.
    """
    filepath = DATAPACK_LOC + xptype.lower() + "_" + skill + "_" + xpval + ".json"
    if not os.path.exists(filepath):
        file_write(filepath, datapackstrs.XP_STR.format(xptype, SKILLIDS[skill], xpval))
        OUTPUTS.append(filepath) #for when we need to enclose files

        file_write(filepath, "\t\"{0}\"".format(item)) #add here so later commas fit nicely!
    else:
        file_write(filepath, ",\n\t\"{0}\"".format(item)) #oh look we need comma first, crazy!


def enclose_files():
    #enclose files in end brackets
    for filepath in OUTPUTS:
        file_write(filepath,"\n\t]\n}")

def file_write(loc,line):
    #so expensive L
    with open(loc,'a') as f:
        f.write(line)

if __name__ == "__main__":
    # idtype = input('id type? (item, block)\n')
    idtype = sys.argv[1]
    valid_args = ["item", "block"]
    
    #if first argument is not valid
    if not idtype in valid_args:
        print("invalid arg, try again. ")
        sys.exit(0)
    

    DATAPACK_LOC = DATAPACK_LOC + idtype + '_xp/'   #sets output file to be whatever id type + xp
    if os.path.exists(DATAPACK_LOC):
        shutil.rmtree(DATAPACK_LOC)
    os.makedirs(DATAPACK_LOC)

    parse_csv(idtype)
