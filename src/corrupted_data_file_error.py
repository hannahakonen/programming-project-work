


class CorruptedDataFileError(Exception):

    def __init__(self, message):
        super(CorruptedDataFileError, self).__init__(message)
