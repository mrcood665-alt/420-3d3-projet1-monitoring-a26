from abc import ABC, abstractmethod

from models.subject import Sujet

class Observateur(ABC):

    @abstractmethod
    def actualiser(self, sujet: Sujet) -> None:
        pass