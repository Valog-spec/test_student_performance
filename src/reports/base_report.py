from abc import ABC, abstractmethod
from typing import Any, List


class MyBaseReport(ABC):
    """Абстрактный базовый класс для отчетов"""

    @abstractmethod
    def create(self, data: List[dict]):
        pass

    @abstractmethod
    def display(self, data: Any):
        pass
