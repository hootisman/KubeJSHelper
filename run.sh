#!/bin/bash

name="modpacktodo"

soffice --convert-to csv:"Text - txt - csv (StarCalc)":44,34,UTF8,1,,0,true,true,true,false,false,1 base/$name.ods
soffice --convert-to csv:"Text - txt - csv (StarCalc)":44,34,UTF8,1,,0,true,true,true,false,false,2 base/$name.ods
soffice --convert-to csv:"Text - txt - csv (StarCalc)":44,34,UTF8,1,,0,true,true,true,false,false,3 base/$name.ods

mv $name-armor.csv ./sheets/armor.csv
mv $name-block.csv ./sheets/block.csv
mv $name-item.csv ./sheets/item.csv

python skillsgen.py
