import abc

class Engine(abc.ABC):
    """
    Engine Abstract Class
    """
    @abc.abstractmethod
    def needs_service(self):
        pass
