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

class ConcreteTranscationManager(TranscationManager):
    def log_transcation(self, transcation_type: str, amount: float) -> None:
        self._transcation.append((transcation_type,amount))
    def show_transcation_history(self) -> None:
        for i in self._transcation:
            print(i)
            
