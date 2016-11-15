class C():
    def __init__(self):
        self.__attr = 0
    @property
    def attr(self):
        """Supply get/set/del functionally for property "attr"."""
        return None
    @attr.getter
    def attr(self):
        return self.__attr
    @attr.setter
    def attr(self, value):
        self.__attr = value
    @attr.deleter
    def attr(self):
        del self.__attr
