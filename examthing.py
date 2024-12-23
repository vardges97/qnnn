# 2# # # # # # class Singleton:
# # # # # # #   __instance = None

# # # # # # #   def __new__(cls, *args, **kwargs):
# # # # # # #     if cls.__instance is None:
# # # # # # #       cls.__instance = super().__new__(cls)
# # # # # # #     return cls.__instance


# 3# # # # # class Logger:
# # # # # #   def log(self, message: str):
# # # # # #     print(f"Logger prints: {message}")


# # # # # # class FileLoger(Logger):
# # # # # #   def log(self, message: object):
# # # # # #     print(f"Logger writes in file: {str(message)}")

# # # # # # class PDFLogger(FileLoger):
# # # # # #   def log(self, message):
# # # # # #     pass

# class our_property:
#     """ emulation of the property class
#         for educational purposes """
#
#     def __init__(self,
#                  fget=None,
#                  fset=None,
#                  fdel=None,
#                  doc=None):
#         """Attributes of 'our_decorator'
#         fget
#             function to be used for getting
#             an attribute value
#         fset
#             function to be used for setting
#             an attribute value
#         fdel
#             function to be used for deleting
#             an attribute
#         doc
#             the docstring
#         """
#         self.fget = fget
#         self.fset = fset
#         self.fdel = fdel
#         if doc is None and fget is not None:
#             doc = fget.__doc__
#         self.__doc__ = doc
#
#     def __get__(self, obj, objtype=None):
#         if obj is None:
#             return self
#         if self.fget is None:
#             raise AttributeError("unreadable attribute")
#         return self.fget(obj)
#
#     def __set__(self, obj, value):
#         if self.fset is None:
#             raise AttributeError("can't set attribute")
#         self.fset(obj, value)
#
#     def __delete__(self, obj):
#         if self.fdel is None:
#             raise AttributeError("can't delete attribute")
#         self.fdel(obj)
#
#     def getter(self, fget):
#         return type(self)(fget, self.fset, self.fdel, self.__doc__)
#
#     def setter(self, fset):
#         return type(self)(self.fget, fset, self.fdel, self.__doc__)
#
#     def deleter(self, fdel):
#         return type(self)(self.fget, self.fset, fdel, self.__doc__)


# better 6 # class Attributes:
# #   def __init__(self, cls):
# #     self.__cls = cls
# #   def __call__(self, *args, **kwargs):
# #     print(f"Class name: {self.__cls.__name__}")
# #     print(f"Attributes: ")

# #     try:
# #         instance = self.__cls(*args, **kwargs)
# #         instance_attributes = instance.__dict__.keys()
# #     except Exception:
# #       instance_attributes = []

# #     for attr_name in dir(self.__cls):
# #       attr = getattr(self.__cls, attr_name)
# #       if attr_name.startswith('__'):
# #         continue
# #       elif isinstance(attr, property):
# #         print(f"- Property: {attr_name}")
# #       elif callable(attr):
# #         print(f"- Method: {attr_name}")
# #       else:
# #         print(f"- Class attribute: {attr_name}")
# #     print(f"- Instance attributes: {list(instance_attributes)}")


# Creating a class dynamically using type()
Car = type('car', (object,), {'brand': lambda self: "lancia",'model': lambda self: "stratos"})

# Using the dynamically created class
# instance = Car()
# print(instance.brand())
# print(instance.model())


# class First(object):
#     def __init__(self):
#         print ("first")
#
# class Second(object):
#     def __init__(self):
#         print ("second")
#
# class Third(First, Second):
#     def __init__(self):
#         First.__init__(self)
#         Second.__init__(self)
#         print( "that's it")

# t = Third()

class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")
class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")
class Third(Second,First):
    def __init__(self):
        super(Third, self).__init__()
        print("third")

class A:
    def __init__(self):
        print('A')
        super().__init__()

class B(A):
    def __init__(self):
        print('B')
        super().__init__()
class X:
    def __init__(self):
        print('X')
        super().__init__()

class Forward(B,A,X):
    def __init__(self):
        print('Forward')
        super().__init__()

Forward()
Third()