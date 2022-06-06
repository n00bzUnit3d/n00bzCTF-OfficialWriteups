from flask import Flask, request, render_template, render_template_string, redirect
import subprocess
import urllib
app = Flask(__name__)
def blacklist(inp):
    blacklist = ['{{','}}','import','os','system','[','\x5f',']']
    for b in blacklist:
        inp = inp.replace(b, '')
    return inp
@app.route('/')
def main():
    return redirect('/curl')

@app.route('/curl',methods=['GET','POST'])
def curl():
    if request.method == 'GET':
        return render_template('curl.html')
    elif request.method == 'POST':
        inp = request.values['curl']
        #print(inp)
        
        #p = subprocess.Popen(["python3", "admin.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #print('a')
        def admin():
            return inp
        print(admin()) 
        webUrl = urllib.request.urlopen(f'{inp}')
        data = webUrl.read()
        #print(data)
        #data = data.replace(b'\n',b'\r\n')
        return f'Am Admin, Going to visit "{inp}" fingers crossed, Result:{data}</p>'
@app.route('/such_a_1337_flag_file_th4t_n0_one_c4n_defnitely_f1nd_hahahaha_lollll_nooob_xDDDDDDd.txt')
def flag():
    return render_template('such_a_1337_flag_file_th4t_n0_one_c4n_defnitely_f1nd_hahahaha_lollll_nooob_xDDDDDDd.txt')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
