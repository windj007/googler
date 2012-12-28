def load_modules(root_package, classnames, *args, **kvargs):
    return [load_class("%s.%s" % (root_package, clsname.lower()), clsname)(*args, **kvargs) for clsname in classnames]


def load_class(package, classname):
    mod = __import__(package, globals(), locals(), [classname], -1)
    return getattr(mod, classname)
