var express = require("express");
var app = express();
var mongoose = require("mongoose");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('views'))

mongoose.connect("mongodb://mongo_local/host_nosqlforyou").catch(err => {
    console.log(err)
  });

var userSchema = new mongoose.Schema({
    username: String,
    password: String
});

var User = mongoose.model('User', userSchema);


app.get("/", (req, res) => {
    res.sendFile('index.html');
});

app.post("/", (req, res) => {
    console.log(req.body)
    var user = req.body.user;
    var pass = req.body.password;

    User.findOne({username: user, password: pass}).then(doc => {
        if(!doc){
            res.send('Too sad!');
        }
        res.send(doc);
    }).catch(err => {
        console.log(err);
    });
});

app.listen(42067, () =>{ console.log("App started on port 42067")})