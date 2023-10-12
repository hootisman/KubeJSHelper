import csv
import os
import shutil
import datapackstrs
from collections import defaultdict

SKILLS = ["magic", "slayer", "fish", "attack", "alch", "mine", "eng", "def", "build", "smith", "wood", "ranged", "craft", "farm", "fly", "cook", "agility", "navi", "hunt", "tame", "stealth", "char", "myst"]
SKILLIDS = dict(zip(SKILLS,["magic","slayer","fishing","attack","alchemy","mining","engineering","defence","building","smithing","woodcutting","ranged","crafting","farming","flying","cooking","agility","navigation","hunter","taming","stealth","charisma","mysticcrafting"]))
DATAPACKFILES = {"armor": datapackstrs.ARMOR_STR, "item": datapackstrs.ITEM_STR, "block": datapackstrs.BLOCK_STR}
OUTPUTS = []
DATAPACK_LOC = "datapack/"
TAGS = defaultdict(list)

def create_datapack(idtype):
    for skill,skilltags in TAGS.items():
        for tag in skilltags:
            skillpath = DATAPACK_LOC + tag.split(":")[1] + '.json'
            req = getReq(tag,skill)
            if not os.path.exists(skillpath):
                file_write(skillpath, DATAPACKFILES[idtype].format(tag,SKILLIDS[skill],req))

def getReq(tag, skill):
    cutted = (tag.split(":")[1]).split('_')[0]
    return cutted[len(skill):]

def parse_csv(idtype):
    """
    opens csv file for xp gains, then creates .json files for each skill, xp type, and value
    """
    with open('sheets/' + idtype + '_xp.csv', newline='') as csvfile:
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
    filepath = DATAPACK_LOC + xptype + "_" + skill + "_" + xpval + ".json"
    if not os.path.exists(filepath):
        file_write(filepath, datapackstrs.XP_STR.format(xptype, SKILLIDS[skill], xpval))
        OUTPUTS.append(filepath) #for when we need to enclose files

        file_write(filepath, "\t\"{0}\"".format(item)) #add here so later commas fit nicely!
    else:
        file_write(filepath, ",\n\t\"{0}\"".format(item)) #oh look we need comma first, crazy!


def add_skill_req(idtype, item, skill, req):
    skillpath = OUTPUT_LOC + skill + ".js"
    tag = 'pmmo:' + skill + req + '_' + idtype
    TAGS[skill].append(tag)

    if not os.path.exists(skillpath):
        #CHANGE ITEM TO BLOCK ETC WHEN WORKIGN WITH THEM!
        tagtype = ""
        match idtype:
            case "armor" | "item":
                tagtype = "item"
            case "block":
                tagtype = "block"
            case _:
                tagtype = "item"

        file_write(skillpath,'ServerEvents.tags(\'' + tagtype + '\', event => {\n')
        OUTPUTS.append(skill)

    file_write(skillpath,'\tevent.add(\'' + tag + '\',\'' + item + '\')\n')

def enclose_files():
    #enclose files in end brackets
    for filepath in OUTPUTS:
        file_write(filepath,"\n\t]\n}")

def file_write(loc,line):
    #so expensive L
    with open(loc,'a') as f:
        f.write(line)

if __name__ == "__main__":
    idtype = input('id type? (item, block)\n')


    DATAPACK_LOC = DATAPACK_LOC + idtype + '/xp/'   #sets output file to be whatever id type + xp
    if os.path.exists(DATAPACK_LOC):
        shutil.rmtree(DATAPACK_LOC)
    os.makedirs(DATAPACK_LOC)

    parse_csv(idtype)
