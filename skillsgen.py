import csv
import os
import shutil

SKILLS = ["magic", "slayer", "fish", "attack", "alch", "mine", "eng", "def", "build", "smith", "wood", "ranged", "craft", "farm", "fly", "cook", "agility", "navi", "hunt", "tame", "stealth", "char", "myst"]
OUTPUTS = []
OUTPUT_LOC = "./output/"


def parse_csv(idtype):
    with open('sheets/' + idtype + '.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        #for each datapoint in csv
        for row in reader:
            item = row["items"]
            row.pop("items")
            skills={k:v for k,v in row.items() if v.isnumeric()} #skills to add to requirements
            for skill,req in skills.items():
                print(skill)
                add_skill_req(idtype, item, skill, req)
            print('\n')
        enclose_files()

def add_skill_req(idtype, item, skill, req):
    skillpath = OUTPUT_LOC + skill + ".js"
    tag = 'pmmo:' + skill + req + '_' + idtype
    if not os.path.exists(skillpath):
        #CHANGE ITEM TO BLOCK ETC WHEN WORKIGN WITH THEM!
        file_write(skillpath,'ServerEvents.tags(\'item\', event => {\n')
        OUTPUTS.append(skill)
    file_write(skillpath,'\tevent.add(\'' + tag + '\',\'' + item + '\')\n')

def enclose_files():
    for skill in OUTPUTS:
        file_write(OUTPUT_LOC + skill + ".js","})")

def file_write(loc,line):
    with open(loc,'a') as f:
        f.write(line)
if __name__ == "__main__":
    idtype = input('id type? ')
    shutil.rmtree('output')
    os.mkdir('output')
    parse_csv(idtype)
