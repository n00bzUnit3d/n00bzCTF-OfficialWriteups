# jane doe | Thxjxs

- Description: Jane Doe has been brutally murdered! The killer is still at large! Jane's right hand man and known associate `A. M. March` is on the run. He might know something... 

- Hint1: March prefers underscores
- Hint2: Can you find your wayback?

# Write up

Anyone's first instict would be to Google the name of the associate, but that turns out to be a dead end. The next best option would be to search for the associate's account in the most popular social media accounts. `Hint1` tells us that March prefers underscores so the account name would be of the form `a_m_march`.

Firing up [Twitter](https://twitter.com) and searching for `a_m_march` gets us this [account](https://twitter.com/A_M_March). Immediately the bio catches the eye: 
```
I love to march!!

a00om{abg_fb_snfg_yznb}
```
The second line definitely looks like a flag and since both the curly braces({}) are intact, it should be a rotation cipher. So try rot13 and sure enough, we get `n00bz{not_so_fast_lmao}`. However this doesn't turn out to be the flag, it's just a dummy flag.

We move on to another social media platform for now. [Facebook](https://www.facebook.com) returns no account for `a_m_march`, so try [Instagram](https://www.instagram.com) next. `a_m_march` does not get us a related account but we already know the full name of the associate from his Twitter handle - April May March. Trying out a few combinations and we get `april_m_march` as the required [account](https://www.instagram.com/april_m_march/). We know we're at the right account since the only post in this account has an image which is the profile picture of the Twitter account which we went through earlier.

Opening the post, we see this caption:
```
aSBrbmV3IHUnZCBmaW5kIG1lIGV2ZW50dWFsbHkuLi4K

b2sgZmluZSwgaSdsbCB0ZWxsIHUgdGhlIHRydXRoCg==

x1yy3q_w4a3_q03!}
```
The first two look like base64 and the third one is again a rotation cipher, could be rot13 again? Decoding the caption gives us:
```
i knew u'd find me eventually...

ok fine, i'll tell u the truth

k1ll3d_j4n3_d03!}
```
The first two seem to be part of the storyline but we're more interested in the third line - it seems to be the flag, or at least a part of it. 

Since we got only a dummy flag earlier, it is possible that the real flag or some clue is there somewhere among those tweets. The third last tweet seems intriguing. 
```
thank god for the delete tweet option lmao, we dont want any "sensitive info" to leak out

#youcantseeme
```
Looks like the flag was tweeted but then deleted. If the last tweet from the account doesn't strike us at first, Hint2 should definetly bring to mind the [**Wayback Machine**](https://archive.org/web/) or the Web Archive. Putting in the link of the Twitter account, we see that the url was indeed saved. Redirecting to the url, shows us a tweet which cant be seen now, since it'd been deleted:

```
dGhlcmUncyBtb3JlIHRvIGl0IHRoYW4gbWVldHMgdGhlIGV5ZS4uLgo=

a00om{1g_j45_wN_Wha3_ju0_
```
Again the first seems to be base64 and the second, rot13. Decoding gives us:
```
there's more to it than meets the eye...

n00bz{1t_w45_jA_Jun3_wh0_
```
We have our full flag now!

# Flag - n00bz{1t_w45_jA_Jun3_wh0_k1ll3d_j4n3_d03!}