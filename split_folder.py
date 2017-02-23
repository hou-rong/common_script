#! /usr/bin/env python3
import os
import shutil
from optparse import OptionParser


def get_dst_path_name(__src_path, __folder_count):
    if __src_path.endswith('/'):
        __src_path = __src_path[:-1]
    __dst_path = '{0}_split_{1:03d}'.format(__src_path, __folder_count)
    if not os.path.exists(__dst_path):
        os.mkdir(__dst_path)
    return __dst_path


def move_file(__src_path, __is_copy, __each_file_per_folder):
    _count = 0
    _folder_count = 0
    dst_path = get_dst_path_name(__src_path, _folder_count)
    for file_name in os.listdir(__src_path):
        # file_path
        src_file = os.path.join(__src_path, file_name)
        dst_file = os.path.join(dst_path, file_name)

        # move func
        if __is_copy:
            shutil.copy(src_file, dst_file)
        else:
            shutil.move(src_file, dst_file)

        _count += 1
        if _count % 10000 == 0:
            print('Now', _count)
        if _count % __each_file_per_folder == 0:
            _folder_count += 1
            dst_path = get_dst_path_name(__src_path, _folder_count)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-p", "--path", dest="folder_path",
                      help="folder path")
    parser.add_option("-n", "--number", dest="each_file_per_folder", default=300000,
                      help="each file per folder")
    parser.add_option("-c", "--is_copy", dest="is_copy", default=False, action="store_true",
                      help="is copy or move")
    parser.print_help()
    options, args = parser.parse_args()

    if options.folder_path is None:
        parser.print_help()
    else:
        src_path = options.folder_path
        is_copy = options.is_copy
        each_file_per_folder = int(options.each_file_per_folder)
        move_file(src_path, is_copy, each_file_per_folder)
