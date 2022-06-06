var express = require("express");
var app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('.'))

app.get("/", (req, res) => {
    console.log(req.url);
    res.sendFile(__dirname+'/attack.html');
});

app.listen(1337, () =>{ console.log("App started on port 1337")})