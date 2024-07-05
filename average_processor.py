from abc_processor import Processor


class AverageProcessor(Processor):
    def __init__(self):
        self.__length = 0
        self.__sum_of_nums = None

    def process_num(self, num):
        self.__length += 1
        if self.__sum_of_nums is None:
            self.__sum_of_nums = num
        else:
            self.__sum_of_nums += num

    def get_result(self):
        return self.__sum_of_nums \
            if self.__sum_of_nums is None or self.__sum_of_nums == 0 \
            else self.__sum_of_nums / self.__length
