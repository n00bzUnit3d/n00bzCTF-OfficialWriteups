# So_snowy! | NoobMaster
- Description: It's so snowy
- Hint: So much Snow!

enc.txt:/attachments/So_snowy!/enc.txt
wordlists.txt:/attachments/So_snowy!/wordlists.txt

# Write up 
So many things telling us to use stegsnow with the wordlist given, there was a challenge in idekCTF where censored made a script to use it, did some changes here's the script - 


```sh
#!/bin/bash
# Thanks to Censored1375 for this script
chall=$(cat ./wordlists.txt)

for i in $chall; do
        echo -e "=== Password: $i ===\n"
        stegsnow -C -p $i enc.txt
        echo -e "\n"
done
```
now grep for n00bz and you will get the flag!


# Flag - n00bz{st3g_1s_s0_sn0wy}
