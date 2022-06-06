# Stager | Censored1375 
- Description: We found a strange file on our server at n00bzunit3d, it seems to be some sort of empire stager, can you tell me where it's staging the next payload? Flag format n00bz{stager_url}, i.e n00bz{www.example.com}

forensics.txt:/attachments/Stager/forensics.txt

# Write up

Open up the file, we see 
```powershell
var c= 'powershell -noP -sta -w 1 -enc  
```
Indicating a powershell stager, install powershell onto your system to prepare for further analysis and let's keep going


```
IAAkAHsASABtAGAANABPAGAATgB1AH0AIAAgAD0AIABbAHQAeQBQAGUAX....
```
Lots of base64, run that through [cyberchef](https://gchq.github.io/CyberChef/) and override the base64 with the result  

```
.$.{.H.m.`.4.O.`.N.u.}. . .= ....
```
Now we have lots of dots, you can remove this by hand but that's too troubling so using vscode, we can automatically remove all the dots in the file

```
${Hm`4O`Nu}  = [tyPe]("{2}{0}{4}{7}{5}{1}{6}{3}{8}....
```
You should now have something that starts like this, now you can clean up the code a bit by making a newline after every `;`, this way there some whitespace inbetween the code making it easier to read 

Once again, you can manually decode all of this(if you know powershell) but since we're n00bz, we're just gonna get powershell to run the code and give us the decoded result

```
pwsh -> ("{2}{0}{4}{7}{5}{1}{6}{3}{8}"-f 'EtSe','N','SYSTemn','AnAGe','rVIc','oI','TM','eP','r') ;
```
Open powershell and run this piece of code, this returns `SYSTemnEtSerVIcePoINTMAnAGer`, we can do similarly for the rest of the code until we find the stager url which is 
```
aAB0AHQAcAA6AC8ALwB3AGkAawBpAC4AbgAwADAAYgB6AHUAbgBpAHQAMwBkAC4AeAB5AHoAOgA4ADAAOAAwAA==
-> wiki.n00bzunit3d.xyz
```

Semi-full deobfuscated file in [forensics-deobf.md](./forensics-deobf.md)

*Becareful when decoding obfuscated powershell this way since you might accidentally run mallicous code with more complex obfuscation* 

If you want to learn more about this, i recommend watching john hammond's malware analysis videos as they contain the techniques used here

# Flag - n00bz{wiki.n00bzunit3d.xyz}
