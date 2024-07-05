from abc_processor import Processor


class AscSeqProcessor(Processor):
    def __init__(self):
        self.__max_asc_seq = 0
        self.__asc_seq_count = 0
        self.__current_num = None
        self.__previous_num = None

    def process_num(self, num):
        if self.__previous_num is None:
            self.__previous_num = num
        self.__current_num = num

        if self.__current_num > self.__previous_num:
            self.__asc_seq_count += 1
            self.__max_asc_seq = max(self.__max_asc_seq, self.__asc_seq_count)
        else:
            self.__asc_seq_count = 1

        self.__previous_num = self.__current_num

    def get_result(self):
        return self.__max_asc_seq
