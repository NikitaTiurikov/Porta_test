from abc_processor import Processor


class MinProcessor(Processor):
    def __init__(self):
        self.__min_num = None

    def process_num(self, num):
        if self.__min_num is None or self.__min_num > num:
            self.__min_num = num

    def get_result(self):
        return self.__min_num
