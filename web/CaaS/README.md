# Curl as a Service | NoobMaster
- Description: Curl as a Service. Note flag is not in flag.txt

remote:https://challs.n00bzunit3d.xyz:30533/
challenge:/attachments/CaaS/challenge_redacted.py

# Write up
Simple arbitary file read using curl, but the flag file is not flag.txt but some random name we dont know as it is redacted in the file given. But what if we read the real challenge.py, the one without the redacted? Yes that's right! It's have the flag function not redacted, it is - 


```py
@app.route('/such_a_1337_flag_file_th4t_n0_one_c4n_defnitely_f1nd_hahahaha_lollll_nooob_xDDDDDDd.txt')
def flag():
    return render_template('such_a_1337_flag_file_th4t_n0_one_c4n_defnitely_f1nd_hahahaha_lollll_nooob_xDDDDDDd.txt')
```


So the flag is at `/such_a_1337_flag_file_th4t_n0_one_c4n_defnitely_f1nd_hahahaha_lollll_nooob_xDDDDDDd.txt` Reading that using curl gives us the flag!


Input - 



1) `file:///chall/challenge.py`


Then visit `/such_a_1337_flag_file_th4t_n0_one_c4n_defnitely_f1nd_hahahaha_lollll_nooob_xDDDDDDd.txt`


# Flag - n00bz{4rb1t4ry_f1le_re4d_us1ng_curl_ftw!}

