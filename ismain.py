from inspect import signature

def entrypoint(modname, alt=lambda:None):
    def _f(func):
        if modname == "__main__":
            count = len(signature(func).parameters)
            if count > 0:
                func(__import__('sys'.argv))
            else:
                func()
        else:
            alt()
        return func
    return _f
