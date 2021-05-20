
from webapp2_extras.users import users



def logging_user(self):
    user = users.get_current_user()
    if user:
        greeting = str.format(
            "<a class=\"login\" href=\"{1}\">Welcome {0}, sign out</a>",
            user.nickname(),
            users.create_logout_url('/'))
    else:
        greeting = str.format(
            "<a class=\"login\" href=\"{0}\">Sign in or register</a>",
            users.create_login_url('/'))
    self.response.out.write(
        str.format("<html>{0}</html>", greeting))
