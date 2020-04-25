______ p_l_, imaplib, getp__s

p _ p_l_.POP3("172.30.42.127", 110)
# p = poplib.POP3_SSL("172.30.42.126", 995)

print(p.g_w_
p.user("ric")
p.p__s_("P4ssw0rd!")

print(p.list)
p.quit

i _ imaplib.IMAP4("172.30.42.127", 143)
# i.login(getpass.getuser(), getpass.getpass_())
i.l..("ric", "P4ssw0rd!")
i.select
t, l _ i.list
print("Response code: ", t)
print(l)

t, ids _ i.s..(None, "ALL")
print("Response code: ", t)
print(ids)
t, msg _ i.fetch('5', "(UID BODY[TEXT])")
#  store messages on the server
#  i.store()
print(msg)
i.c..
i.logout
