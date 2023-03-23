const puppeteer = require('puppeteer');
const express = require('express');

const APP_URL = "http://0.0.0.0:8888/"; 

const app = express();

app.get("/", (req, res) => {
    url = req.query.url;
    visit_url(url);
    res.send("admin will visit your url");
});



async function intiialize () {
    var quote;
    return new Promise(async function(resolve, reject) {
        const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
        const page = await browser.newPage();  
        await page.setDefaultNavigationTimeout(1e3*15);
        try{
            await page.goto(APP_URL);
            await page.type('input[name=username]', process.env.ADMINUSER);
            await page.type('input[name=password]', process.env.ADMINPASS);
            await page.click('button[type=submit]');
            
            await page.goto(APP_URL);
            await page.type('input[name=username]', process.env.ADMINUSER);
            await page.type('input[name=password]', process.env.ADMINPASS);
            await page.click('button[type=submit]');

            await page.goto(APP_URL + "/dashboard",{
                waitUntil: "load",
              });
            await page.type('input[name=notetitle]', 'the fleg note');
            await page.type('textarea[name=note]', process.env.FLAG);
            await page.click('input[type=submit]');

        }   
        catch(e){
            console.log(e);
        }        
        await browser.close();

        resolve(quote);
    });
}

async function visit_url (url) {
    var quote;
    return new Promise(async function(resolve, reject) {
        intiialize (); 
        
        const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
        const page = await browser.newPage();  
        await page.setDefaultNavigationTimeout(1e3*15);
        try{
            await page.goto(APP_URL);
            await page.type('input[name=username]', process.env.ADMINUSER);
            await page.type('input[name=password]', process.env.ADMINPASS);
            await page.click('button[type=submit]');
            
            console.log("Opening " + url)
            const page2 = await browser.newPage();  
            await page2.goto(url);
            await page2.setDefaultNavigationTimeout(1e3*15);
            console.log("Opened title: ", page2.title())

            await page.goto(APP_URL);
            await page.type('input[name=username]', process.env.ADMINUSER);
            await page.type('input[name=password]', process.env.ADMINPASS);
            await page.click('button[type=submit]');
        }   
        catch(e){
            console.log(e);
        }        
        await browser.close();

        resolve(quote);
    });
}

app.listen(8080, () => {
    console.log(`App listening at http://localhost:8080`);
    intiialize();
})