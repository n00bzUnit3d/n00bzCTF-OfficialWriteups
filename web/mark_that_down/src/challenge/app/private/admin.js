const crypto = require("crypto");
const ADMIN_PASS = require("../../admin/admin.js").ADMIN_PASS;
var admin_hash = crypto.createHash('sha512').update(ADMIN_PASS).digest('hex');

module.exports = {

    validate:async function validate(user, pass){
        var user_hash = crypto.createHash('sha512').update(user).digest('hex');
        var pass_hash = crypto.createHash('sha512').update(pass).digest('hex');

        if (user_hash === "c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec"){
            if (pass_hash === admin_hash){
                return "admin.html";
            }

        }
        return "login.html";
    }
}