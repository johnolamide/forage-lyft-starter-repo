import abc

class Battery(abc.ABC):
    """
    Battery Abstract Class
    """
    @abc.abstractmethod
    def needs_service(self):
        pass
