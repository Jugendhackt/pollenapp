#!/bin/bash
export LANG=C
grep '"'"$1"'"' Allergiebaumkataster.csv |\
cut -d , -f 3,4 |\
tr , '\n' |\
tr -d \'\" >Suchergebnis.csv