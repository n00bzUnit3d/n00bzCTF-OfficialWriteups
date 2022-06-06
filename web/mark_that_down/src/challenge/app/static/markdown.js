var showdown  = require('showdown');
var converter = new showdown.Converter();

const fs = require('fs');
const crypto = require("crypto");

module.exports = {

    check:function check(markdown){
        var b_blacklist = ['<', '>', ';'];
        for (i=0; i<b_blacklist.length; i++){
            if (markdown.toLowerCase().indexOf(b_blacklist[i]) >= 0){
                return false;
            }
        }

        var html = converter.makeHtml(markdown);

        //Check for illegal words after parsing
        var a_blacklist = ['script','data'];
        for (i=0; i<a_blacklist.length; i++){
            if (html.toLowerCase().indexOf(a_blacklist[i]) >= 0){
                return false;
            }
        }
        return html;
    },

    save:function save(html){
        var new_filename = crypto.randomUUID()+".html"
        var save_dir = "public/"
        try {
            fs.writeFileSync("./"+save_dir+new_filename, html);
            return new_filename;
        } catch (err) {
        console.error(err);
        }
    }
}