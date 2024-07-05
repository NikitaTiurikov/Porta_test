from abc import ABC, abstractmethod


class Processor(ABC):
    @abstractmethod
    def process_num(self, num):
        pass

    @abstractmethod
    def get_result(self):
        pass
