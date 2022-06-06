#!/bin/bash
# Thanks to Censored1375 for this script
chall=$(cat ./wordlists.txt)

for i in $chall; do
        echo -e "=== Password: $i ===\n"
        stegsnow -C -p $i enc.txt
        echo -e "\n"
done