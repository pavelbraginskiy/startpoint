from inspect import signature, Parameter

def entrypoint(modname, alt=lambda:None):
    def _f(func):
        if modname == "__main__":
            count = len([x for x in signature(func).parameters.values() if x._kind is Parameter.POSITIONAL_OR_KEYWORD and x.default is Parameter.empty])
            if count == 1:
                func(__import__('sys').argv)
            elif count == 0:
                func()
            else:
                raise ValueError("Entry point should have 0 or 1 required arguments!")
        else:
            alt()
        return func
    return _f
