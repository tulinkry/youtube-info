class YoutubeObject(object):
    """
    A convenient mapping from the youtube api response to an
    object supporting attribute references to the json object.
    """

    def __init__(self, data={}):
        super(YoutubeObject, self).__setattr__('_data', data)

    def __getattr__(self, name):
        """
        Get the class attribute, the non-existent attributes are backed by
        elements in the _data attribute.
        :param name: the attribute name
        :return: the attribute value
        """
        if name in self.__dict__:
            return self.__dict__[name]

        if name in self._data:
            if isinstance(self._data[name], dict):
                return YoutubeObject(self._data[name])

            return self._data[name]

        raise AttributeError("No attribute '{}'"
                             " in class '{}'.".format(name,
                                                      self.__class__.__name__))

    def __setattr__(self, name, value):
        """
        Set the class attribute to a value, the non-existent
        attributes are backed by elements
        in the _data attribute.
        :param name: the attribute name
        :param value: the attribute new value
        :return: the attribute new value
        """
        if name in self.__dict__:
            self.__dict__[name] = value
            return value

        self._data[name] = value

        return value

    def __repr__(self):
        return repr(self._data)
