from wechat.services import login


l = login.Login()
l.login()
print(l.redirect_uri)