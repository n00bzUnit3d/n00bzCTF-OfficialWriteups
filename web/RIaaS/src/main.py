from flask import Flask, request, render_template, render_template_string
def blacklist(inp):
    blacklist = ['_','{{','}}']
    for b in blacklist:
        inp = inp.replace(b, '')
        if 'curl http://' not in inp:
            inp = 'please use curl'
    return inp
    
app = Flask(__name__)

@app.route('/')
def main():
    return render_template_string('''<h1>Welcome to RIaaS(Random Input as a Service)!</h1>
        <p>Please login so that are robots know that you are human, But our login page seems to be lost</p>
        <!-- We have a blacklist to keep those sneaky hackers away! -->''')
@app.route('/robots.txt')
def robots():
    return render_template_string('''<p>User-agent: Stormtroopers</p><br> 
                                        <p>Disallow: /nottheflaglol</p>''')
@app.route('/nottheflaglol', methods=['GET', 'POST'])
def index(): 
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = blacklist(request.values['username'])
        print(username)
        if username != 'please use curl':

            return render_template_string('<p>You really thought I am going to execute ' + f"'{username}'" + ' ?')
        
    
        elif username == 'please use curl':
            return render_template_string('<p>No curl in input</p>')

# result = subprocess.run(
#     ['php', 'main.php'],    # program and arguments
#     stdout=subprocess.PIPE,  # capture stdout
#     check=True               # raise exception if program fails
# )
# print(result.stdout) 
       # result.stdout contains a byte-string
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
