"""An Abstract Expression"""


class AbstractExpression:
    """
    All Terminal and Non-Terminal expressions will implement an
    `interpret` method
    """

    @staticmethod
    def interpret():
        """
        The `interpret` method gets called recursively for
        each AbstractExpression
        """
