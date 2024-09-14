from abc import ABC,abstractmethod

class TranscationManager(ABC):
    def __init__(self) -> None:
        self._transcation = []
    @abstractmethod
    def log_transcation(self,transcation_type:str,amount:float) -> None:
        pass
    @abstractmethod
    def show_transcation_history(self) -> None:
        pass


