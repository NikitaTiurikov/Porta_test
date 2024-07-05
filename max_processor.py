from abc_processor import Processor


class MaxProcessor(Processor):
    def __init__(self):
        self.__max_num = None

    def process_num(self, num):
        if self.__max_num is None or self.__max_num < num:
            self.__max_num = num

    def get_result(self):
        return self.__max_num
