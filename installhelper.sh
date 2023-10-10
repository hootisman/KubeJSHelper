#!/bin/bash

path=$(pwd)

cp -r "$path/output"/* "$1/kubejs/server_scripts/pmmo/"
echo "kubejs scripts installed in path : " + $1

cp -r "$path/datapack"/* "$2/data/minecraft/pmmo/items/"
echo "datapack scripts installed in path : " + $2
