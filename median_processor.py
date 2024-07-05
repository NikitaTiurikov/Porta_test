from abc_processor import Processor


class MedianProcessor(Processor):
    def __init__(self):
        self.__lst = []

# На жаль я не знаю як рахувати медіану не заганяючи масив в памʼять
    def process_num(self, num):
        self.__lst.append(num)

    def get_result(self):
        if len(self.__lst) == 0:
            return None
        self.__lst.sort()
        half = len(self.__lst) // 2
        if len(self.__lst) % 2 == 0:
            return (self.__lst[half] + self.__lst[half - 1]) / 2
        return self.__lst[half]