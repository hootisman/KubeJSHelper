#!/bin/bash

name="modpacktodo"

soffice --convert-to csv:"Text - txt - csv (StarCalc)":44,34,UTF8,1,,0,true,true,true,false,false,1 base/$name.ods #armor
soffice --convert-to csv:"Text - txt - csv (StarCalc)":44,34,UTF8,1,,0,true,true,true,false,false,2 base/$name.ods #block
soffice --convert-to csv:"Text - txt - csv (StarCalc)":44,34,UTF8,1,,0,true,true,true,false,false,3 base/$name.ods #item
soffice --convert-to csv:"Text - txt - csv (StarCalc)":44,34,UTF8,1,,0,true,true,true,false,false,4 base/$name.ods #item_xp
soffice --convert-to csv:"Text - txt - csv (StarCalc)":44,34,UTF8,1,,0,true,true,true,false,false,5 base/$name.ods #block_xp

mv $name-armor.csv ./sheets/armor.csv
mv $name-block.csv ./sheets/block.csv
mv $name-item.csv ./sheets/item.csv
mv $name-item_xp.csv ./sheets/item_xp.csv
mv $name-block_xp.csv ./sheets/block_xp.csv
