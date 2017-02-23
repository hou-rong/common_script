#! /usr/bin/env python3
from optparse import OptionParser


def split_file(path, lines=300000):
    _check_count = 0
    source_file = open(path)
    _f_count = 0
    target_file = open('{0}_{1:0>3}'.format(path, _f_count), 'w')
    _count = 0
    for line in source_file:
        _check_count += 1
        if _check_count % 10000 == 0:
            print(_check_count)
        _count += 1
        if _count < lines:
            target_file.write(line)
        else:
            target_file.write(line)
            _count = 0
            _f_count += 1
            target_file = open('{0}_{1:0>3}'.format(path, _f_count), 'w')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="file_path",
                      help="split file path")
    parser.add_option("-l", "--line", dest="split_line", default=300000,
                      help="each file line")

    options, args = parser.parse_args()
    print(options)
    print(type(options))
    print(type(options.split_line))
    if options.file_path is None:
        parser.print_help()
    else:
        split_file(options.file_path, lines=int(options.split_line))
