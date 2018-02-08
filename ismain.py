from inspect import signature

def entrypoint(modname, alt=lambda:None):
    def _f(func):
        if modname == "__main__":
            count = len(signature(func).parameters)
            if count == 1:
                func(__import__('sys'.argv))
            elif count == 0:
                func()
            else:
                raise raise ValueError("Entry point should take 0 or 1 arguments.")
        else:
            alt()
        return func
    return _f
