const puppeteer = require('puppeteer');
const queueName = __filename.split(".")[0].split("/").pop();
const express = require("express");
const socket = require("socket.io");
const APP_URL = process.env.APP_URL || "http://localhost:5000/login"
// App setup
const PORT = 3000;
const app = express();
app.get("/", (req, res) => {
    url = req.query.url;
    visit_url(url);
    res.send("admin will visit your url");
});
const server = app.listen(PORT, function () {
  console.log(`Listening on port ${PORT}`);
  console.log(`http://localhost:${PORT}`);
});

// Static files
app.use(express.static("public"));

// Socket setup

const challName = "csrf-chall"

async function visit_url (url) {
    var quote;
    return new Promise(async function(resolve, reject) {
        const browser = await puppeteer.launch({executablePath: '/app/latest/chrome',args:['-no-sandbox']});
        const page = await browser.newPage();  
        await page.setDefaultNavigationTimeout(1e3*15);
        try{
            var result = await page.goto(APP_URL);
            await page.type('#username', 'admin');
            await page.type('#password', 'veriverisoopersecratpassword');
            await page.click('#submit');
            const page2 = await browser.newPage();
            await page2.setDefaultNavigationTimeout(1e3*15);
            var result = await page2.goto(url);
            await page2.screenshot({path: "screen.png"})
        }
        catch(e){
            console.log(e);
        }        
        await browser.close();

        resolve(quote);
    });
}

console.log(`Started bot for chall ${challName} with id ${queueName}`)