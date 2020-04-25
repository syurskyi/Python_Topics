______ _2
______ u_l_

url _ "http://172.30.42.127/test.php"
data _ {'txtName' : 'Ric', 'txtAge' : '19', 'btnSubmit' : 'Submit'}
params _ u_l_.urlencode(data)
req _ _2.R..(url, data_params)
handle _ _2.u_o..(req)
page _ handle.r..
print(page)
