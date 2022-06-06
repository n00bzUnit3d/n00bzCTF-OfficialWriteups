Disclaimer: This is the intended solution, im not 100% sure that there arent unintended solutions

TLDR:
    the admin bot is vulnerable to reverse tabnabbing. By creating a custom form using markdown
    and using an attacker controlled site to perform tabnabbing and receive the credentials, the
    attacker is able to login as admin and get the flag

The markup page:
    The page says not to use any javascript and does some blacklist checking for that, but by using a markdown image
    with an onerror event javascript can be created. `![]("onerror="alert(1))`

The report page:
    It is a simple "provide a url and admin will visit" form, but the site tries to check if the url is of the same domain.
    This can be bypassed because only a startsWith("...") is done meaning we can can just put the domain as username to another domain.
    (Note: this isnt really necessary to do the chall but it makes things easier)

The admin bot:
    The vulnerable part of code here is `await page.evaluate((url) => {
            window.open(url, '_blank');
        }, url);`
    The window.open() is susceptible to reverse tabnabbing meaning we can inject javascript on the window.opener page or even
    change the url. For this challenge the javascript injecting part was countered by closing the opened page and reloading the first page, so all we have left is to change the url.

The attack:
    The attack will require a server with some code. I use nodejs and then ngrok the port

    1. Create a server which will show the 3. steps page and receive the credentials (attack.js)
    2. Create a form with the required attributes in markdown using images with onerror events (markdown_payload_solve.md)
        The payload needs to include the servers url (the ngrok one in my case)
    3. Create a page to perform tabnabbing and change the first tabs url to the markdown one (attack.html)
        This needs to include the markdown pages url
    4. Provide the 3. steps page to admin bot by bypassing the domain check and wait for the admin to visit
    5. Congratulations, you just performed a phishing attack on an admin bot. Login and get the flag
        n00bz{r3v3rs3_t4bn4bb1ng_1s_ju5t_lurk1ng_4r0und..}

