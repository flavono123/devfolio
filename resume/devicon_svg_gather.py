from os import listdir
from os.path import join, abspath, dirname, isdir


#TODO: refering devicon git repo.. static?
#BASE_DIR = dirname(abspath(__file__))
#ROOT_DEV = lambda *args: join(BASE_DIR, *args)


def get_svg_code_dict():
    dir_name_list = [dir_name for dir_name in listdir(ROOT_DEV('devicon', 'icons'))]
    dir_name_list.sort()

    suffix_candidates = ['plain', 'plain-wordmark', 'original', 'original-wordmark']

    svg_code_dict = {}

    for i, dir_name in enumerate(dir_name_list):
        for suffix in suffix_candidates:
            file_name = dir_name + '-' + suffix + '.svg'
            #FIXME: ROOT_DEV not work
            file_path = ROOT_DEV('devicon', 'icons', dir_name, file_name)
            try:
                with open(file_path, mode='r') as f:
                    svg_code = f.read()
                    svg_code_dict[dir_name] = svg_code
                    break
            except FileNotFoundError:
                continue

    return svg_code_dict
