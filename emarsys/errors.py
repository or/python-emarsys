class EmarsysError(Exception):
    """
    General Emarsys Exception
    """

    def __init__(self, message, code=None):
        self.message = message
        self.code = u'{code}'.format(code=code)

    def __unicode__(self):
        if self.code is None:
            message = self.message
        else:
            message = u"{message} ({code})".format(message=self.message,
                                                   code=self.code)
        return u"EmarsysError({message})".format(message=message)

    def __str__(self):
        return unicode(self).encode("utf8")

    def __repr__(self):
        return str(self)


class MaxSizeExceededError(EmarsysError):
    """Codes: 1000, 2002, 3002"""


class InvalidDataError(EmarsysError):
    """Codes: 1002, 2004, 2005, 2006, 2007, 2012, 2013, 3003, 3004, 4002, 5001,
    6003, 6004, 6005, 6008, 6009, 10001"""


class NotFoundError(EmarsysError):
    """Codes: 7002, 2008"""


class AlreadyExistsError(EmarsysError):
    """Codes: 2009, 2010, 3005, 7001"""

error_dictionary = {
    "1002": InvalidDataError,
    "2004": InvalidDataError,
    "2005": InvalidDataError,
    "2006": InvalidDataError,
    "2007": InvalidDataError,
    "2012": InvalidDataError,
    "2013": InvalidDataError,
    "3003": InvalidDataError,
    "3004": InvalidDataError,
    "4002": InvalidDataError,
    "5001": InvalidDataError,
    "6003": InvalidDataError,
    "6004": InvalidDataError,
    "6005": InvalidDataError,
    "6008": InvalidDataError,
    "6009": InvalidDataError,
    "10001": InvalidDataError,
    "1000": MaxSizeExceededError,
    "2002": MaxSizeExceededError,
    "3002": MaxSizeExceededError,
    "2009": AlreadyExistsError,
    "2010": AlreadyExistsError,
    "3005": AlreadyExistsError,
    "7001": AlreadyExistsError,
    "7002": NotFoundError,
    "2008": NotFoundError
}
