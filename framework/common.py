import inspect


def PageObject(cls):
    # print(inspect.getmembers(cls))

    classes = inspect.getmro(cls)

    for incls in classes:
        inheritance = inspect.getmro(incls)
        if len(inheritance) > 1 and inheritance[1] is Component:
            # this is the class we were looking for
            if not hasattr(incls, 'ID'):
                continue

            attribs = list(filter(lambda attr: not attr.startswith("_"), vars(incls.ID)))

            for attr in attribs:
                attr_value = getattr(incls.ID, attr)
                if hasattr(cls.ID, attr) and getattr(cls.ID, attr) != attr_value:
                    raise Exception(
                        "The attribute {} already exists in base class with a different value. Please rename the attribute".format(
                            attr))
                setattr(cls.ID, attr, attr_value)

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


class Component(object):
    pass
