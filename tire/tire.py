import abc

class Tire(abc.ABC)
    """
    Tire Abstract Class
    """
    @abc.abstractmethod
    def needs_service(self):
        pass
