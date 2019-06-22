# Adds a welcome message the string
# returned by fun(). Takes fun() as
# parameter and return welcome().

def decorate_message(fun):
    # Nested function
    def addWelcome(site_name):
        return "welcome to " + fun(site_name)

    # Decorator returns a function
    return addWelcome


@decorate_message
def site(site_name):
    return site_name



# Driver code

# this call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print(site("GeeksforGeeeks"))