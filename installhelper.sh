#!/bin/bash

path=$(pwd)

cp -r "$path/output"/* "$1/kubejs/server_scripts/pmmo/"
echo "kubejs scripts installed in path : " + $1

cp -r "$path/datapack/armor" "$2/data/minecraft/pmmo/items/"
cp -r "$path/datapack/item" "$2/data/minecraft/pmmo/items/"
cp -r "$path/datapack/block" "$2/data/minecraft/pmmo/blocks/"
echo "datapack scripts installed in path : " + $2
