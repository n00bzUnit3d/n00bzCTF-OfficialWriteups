# Conti | Censored1375 
- Description: A bunch of conti's internal sofware, source code and training materials were leaked by an angry Ukrainian affiliate back in March, we heard there were even credentials for something called "lero". Can you help us find it? Flag format n00bz{username, password}

# Write up

Google for `conti leaks lero` gives us [a threatpost link](https://threatpost.com/conti-ransomware-decryptor-trickbot-source-code-leaked/178727/) which metions vx-underground,it also states
```   
Other TrickBot leaks include server-side components written in Erlang, a trickbot-command-dispatcher-backend and trickbot-data-collector-backend, dubbed lero and dero.
```
Which means `lero` is part of Trickbot, googling `vx-underground` gives us their official website and twitter but we(i) can't seem to find `/Conti` directory like in the blog post

So instead google `vx-underground conti` which provides us with the [/Conti](https://share.vx-underground.org/Conti/) directory

Download `Conti Trickbot Leaks.7z` and open with password of `infected`

Look in `lero > doc > credentials` we will find the server control panel credentials `alkahov4:nt5Sbt5ZF&$qr*T`

# Flag - n00bz{alkahov4, nt5Sbt5ZF&$qr*T}