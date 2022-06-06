var express = require("express");
var app = express();
var rateLimit = require("express-rate-limit")

const host_url = process.env.HOST

var admin = require("../admin/admin.js");
var markdown = require("./static/markdown.js");
var login = require('./private/admin.js');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'))

static = __dirname + "/static/";
private = __dirname + "/private/";

const reportLimiter = rateLimit({
	windowMs: 10 * 1000, // 10 seconds
	max: 1, // Limit each IP to 1 requests per windowMs
    handler: function (req, res) {
        return res.status(429).send('Too many requests!');
    }
})

app.get('/', (req, res) => {
    res.sendFile(static + "markdown.html");
});
app.post('/', (req, res) => {
    var html = markdown.check(req.body.markdown);
    if (!html){
        res.send(`<head>
                <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css' rel='stylesheet'>
                </head><body class="bg-dark text-center text-light mt-4">
                <h1>Illegal words/characters found!</h1>
                </body>`);
        return;
    }
    var save_path = markdown.save(html);
    res.end(`<head>
            <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css' rel='stylesheet'>
            </head><body class="bg-dark text-center text-light mt-4">
            <h3>Your file has been succesfully uploaded to <a href=/${save_path}>${save_path}</a> !</h1>
            </body>`);
});

app.get("/report", (req, res) => {
    res.sendFile(static + "report.html");
});
app.post("/report", reportLimiter, (req, res) => {
    var url = req.body.url;
    if (url.toLowerCase().startsWith("http://"+host_url) || url.toLowerCase().startsWith("https://"+host_url)){
        admin.visit(url).then((result) => {
            if (result){res.send("This page does break our rules!");}
            else if (!result){res.send("This page isn't breaking our rules!");}
        })
    }
    else{
        res.send("Page isn't on this site!")
    }
});

app.get('/admin', (req, res) => {
    res.sendFile(private + "login.html");
});
app.post('/admin', (req, res) => {
    user = req.body.username;
    pass = req.body.password;
    login.validate(user, pass).then((page) => {
        res.sendFile(private + page);
    })
});


app.listen(42069, () =>{ console.log("App started on port 42069")})
