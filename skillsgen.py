import csv
import os
import shutil
from collections import defaultdict

SKILLS = ["magic", "slayer", "fish", "attack", "alch", "mine", "eng", "def", "build", "smith", "wood", "ranged", "craft", "farm", "fly", "cook", "agility", "navi", "hunt", "tame", "stealth", "char", "myst"]
SKILLIDS = dict(zip(SKILLS,["magic","slayer","fishing","attack","alchemy","mining","engineering","defence","building","smithing","woodcutting","ranged","crafting","farming","flying","cooking","agility","navigation","hunter","taming","stealth","charisma","mysticcrafting"]))
OUTPUTS = []
OUTPUT_LOC = "output/"
DATAPACK_LOC = "datapack/"
TAGS = defaultdict(list)

def create_datapack():
    for skill,skilltags in TAGS.items():
        for tag in skilltags:
            skillpath = DATAPACK_LOC + tag.split(":")[1] + '.json'
            req = getReq(tag,skill)
            if not os.path.exists(skillpath):
                file_write(skillpath, 
                        '''
{{\"negative_effect\": {{
        \"minecraft:weakness\":3,
        \"minecraft:slowness\":3,
        \"minecraft:mining_fatigue\":3,
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

}}'''.format(tag,SKILLIDS[skill],req))

def getReq(tag, skill):
    cutted = (tag.split(":")[1]).split('_')[0]
    return cutted[len(skill):]

def parse_csv(idtype):
    with open('sheets/' + idtype + '.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        #for each datapoint in csv
        for row in reader:
            item = row["items"]
            row.pop("items") #gets rid of 'items' col from row

            skills={k:v for k,v in row.items() if v.isnumeric()} #skills to add to requirements
            for skill,req in skills.items():
                add_skill_req(idtype, item, skill, req)
        enclose_files()

def add_skill_req(idtype, item, skill, req):
    skillpath = OUTPUT_LOC + skill + ".js"
    tag = 'pmmo:' + skill + req + '_' + idtype
    TAGS[skill].append(tag)

    if not os.path.exists(skillpath):
        #CHANGE ITEM TO BLOCK ETC WHEN WORKIGN WITH THEM!
        file_write(skillpath,'ServerEvents.tags(\'item\', event => {\n')
        OUTPUTS.append(skill)

    file_write(skillpath,'\tevent.add(\'' + tag + '\',\'' + item + '\')\n')

def enclose_files():
    #enclose files in end bracket
    for skill in OUTPUTS:
        file_write(OUTPUT_LOC + skill + ".js","})")

def file_write(loc,line):
    #so expensive L
    with open(loc,'a') as f:
        f.write(line)

if __name__ == "__main__":
    idtype = input('id type? ')
    shutil.rmtree(OUTPUT_LOC)
    os.mkdir(OUTPUT_LOC)
    OUTPUT_LOC = OUTPUT_LOC + idtype + '/'
    os.mkdir(OUTPUT_LOC)

    shutil.rmtree(DATAPACK_LOC)
    os.mkdir(DATAPACK_LOC)
    DATAPACK_LOC = DATAPACK_LOC + idtype + '/'
    os.mkdir(DATAPACK_LOC)

    parse_csv(idtype)
    create_datapack()
