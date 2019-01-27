
def obj2dict(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value) \
                                     and not name.startswith('_') \
                                     and not name == "metadata":

            pr[name] = value

    return pr

