def non_decorate_message(site_name):
    return ('welcome to '+ site(site_name))

def site(site_name):
    return site_name
msg = non_decorate_message("Thailand")
print(msg)


def decorate_message(fun):
    def addWelcome(site_name):
        return "welcome to " + fun(site_name)
    return addWelcome

def site(site_name):
    return site_name

site = decorate_message(site)
print(site("Thailand"))


