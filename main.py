import sys
from min_processor import MinProcessor
from max_processor import MaxProcessor
from average_processor import AverageProcessor
from asc_seq_processor import AscSeqProcessor
from desc_seq_processor import DescSeqProcessor
from median_processor import MedianProcessor

print('argument list', sys.argv, '\n')
file_name = sys.argv[1]


if __name__ == '__main__':
    maximum = MaxProcessor()
    minimum = MinProcessor()
    average = AverageProcessor()
    asc_sequence = AscSeqProcessor()
    desc_sequence = DescSeqProcessor()
    median = MedianProcessor()

    with open(file_name, 'r', encoding='UTF8') as file:
        for line in file:
            number = int(line)
            minimum.process_num(number)
            maximum.process_num(number)
            average.process_num(number)
            asc_sequence.process_num(number)
            desc_sequence.process_num(number)
            median.process_num(number)
    print(f'Minimum number in file: {minimum.get_result()}')
    print(f'Maximum number in file: {maximum.get_result()}')
    print(f'Average: {average.get_result()}')
    print(f'Median: {median.get_result()}')
    print(f'The longest ascending sequence: {asc_sequence.get_result()}')
    print(f'The longest descending sequence: {desc_sequence.get_result()}')
