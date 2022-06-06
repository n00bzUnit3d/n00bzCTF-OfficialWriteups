# Cookie Clicker | awawa

- Description: I wanna reach a million cookies!

- Hint: the game has an autosave feature! :o

Zip_File:https://storage.googleapis.com/static.n00bzunit3d.xyz/Cookie%20Clicker/cookieclicker.zip

# Write up

we are told to get a million cookies, after trying to click for a bit we can see that we could make a simple autoclicker script but that'd be no fun, looking through the settings
we see it has an autosave feature and that it makes a savefile

looking in the game folder we see a file called "save.xlsx" and editing it we see some values, messing with it we see that the first two cells are the gold amount and the cookie amount
values respectively, editing the second value to 10 million makes the game print out "b'bjAwYnp7WXVtbXlDMDBraWV6fQ=='"

"b'bjAwYnp7WXVtbXlDMDBraWV6fQ=='" seems to be a base64 encoded string, decoding it gives us the result "b'n00bz{YummyC00kiez}'", removing the quotes and the b gives us the flag

# Flag - n00bz{YummyC00kiez}

