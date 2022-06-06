const puppeteer = require("puppeteer");
const crypto = require("crypto");
const fs = require('fs');

const ADMIN_PASS = crypto.randomBytes(64).toString('hex');
const host_url = process.env.HOST
const login_url = 'http://'+host_url+'/admin';

const browser_options = {
        executablePath: '/usr/bin/chromium-browser',
        headless: true,
        args: [
                '--incognito',
                '--no-sandbox',
                '--disable-background-networking',
                '--disable-default-apps',
                '--disable-extensions',
                '--disable-gpu',
                '--disable-sync',
                '--disable-translate',
                '--hide-scrollbars',
                '--metrics-recording-only',
                '--mute-audio',
                '--no-first-run',
                '--safebrowsing-disable-auto-update',
		'--js-flags=--noexpose_wasm,--jitless'
        ],
	ignoreHTTPSErrors: true
};

module.exports = {

    ADMIN_PASS:ADMIN_PASS,

    visit:async function visit(url){
        //Define sleep
        const sleep = ms => new Promise(r => setTimeout(r, ms));

        //Remove flag file
        try {
            fs.unlinkSync("../admin/private/flag")
        } catch(err) {}
    
        //Open a new browser
        const browser = await puppeteer.launch(browser_options);
        const page = (await browser.pages())[0]
    
        //goto login page
        await page.goto(login_url);

        //Wait for a .5 seconds to load, then go to user supplied page
        await sleep(500);
        await page.evaluate((url) => {
            window.open(url, '_blank');
        }, url);
        //sleep for 1 second, then get the user pages title
        await sleep(1000);// wait for a second
        opened = (await browser.pages())[1]
        opened.setDefaultNavigationTimeout(2000);
        var content = await opened.content();
        var contains = await content.includes("<script>");
        await opened.close();
        
        //Go back to first page
        page.bringToFront();
        await page.reload();

        //A url check just in case bot went to wrong site
        const host = await page.evaluate(() => document.location.host);
        if (host != host_url){
            await browser.close();
            return "Unexpected error!";
        }

        //Login
        await page.type('input[name="username"]', 'admin');
        await page.type('input[name="password"]', ADMIN_PASS);

        await Promise.all([
            page.waitForNavigation(),
            page.click('button[type="submit"]')
    
        ]);
        
        //Get the flag and save it in a file
        try{
            //Wait for page to load, then get the flag
            await sleep(500);
            var flag = await page.evaluate(() => document.getElementById("flag").innerHTML);

            //Write the flag to a file
            fs.writeFileSync("../admin/private/flag", flag);
            
        } catch(e){}
        await browser.close();
        return contains;
    }

}
