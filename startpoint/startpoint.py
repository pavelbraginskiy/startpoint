import sys
if sys.version_info < (3,3): 
    from inspect import signature, Parameter
else:
    from funcsigs import signature, Parameter

def entrypoint(modname, alt=lambda:None):
    def _f(func):
        if modname == "__main__":
            arg_count = len(signature(func).parameters)
            # Thanks to Mego for this snippet. Counts the number of required arguments that `func` has.
            req_count = len([x for x in signature(func).parameters.values() if x._kind is Parameter.POSITIONAL_OR_KEYWORD and x.default is Parameter.empty])
            if req_count == 1 or (req_count == 0 and arg_count > 0):
                func(sys.argv)
            elif arg_count == 0:
                func()
            else:
                raise ValueError("Entry point should have 0 or 1 required arguments!")
        else:
            alt()
        return func
    return _f
