class CountOutOfBounds(Exception):
    """
    The result count is greater than the elements in the list provided.
    """
    pass

class ListProcessingError(Exception):
    """
    The list being processed either cannot be parsed or the file does not exist.
    """
    pass