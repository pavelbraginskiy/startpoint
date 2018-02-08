def entrypoint(modname, alt=lambda:None):
    def _f(func):
        func() if modname == '__main__' else alt()
        return func
    return _f
