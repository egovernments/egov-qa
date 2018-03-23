import inspect


def PageObject(cls):
    # print(inspect.getmembers(cls))
    functions = inspect.getmembers(cls, predicate=inspect.isfunction)

    for (func_name, func_impl) in functions:
        # func_impl_static = staticmethod(func_impl)
        func_impl_static = func_impl
        # func_impl_static.__globals__ = func_impl.__globals__
        func_impl_static.__globals__['ID'] = getattr(cls, 'ID', {})
        # func_impl_static.__globals__['cls'] = cls
        # setattr(cls, func_name, func_impl_static)
    return cls


class Page(object):
    pass
