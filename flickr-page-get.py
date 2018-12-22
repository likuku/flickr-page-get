#!/usr/bin/env python
# encoding: utf-8
"""
flickr-page-get.py
Copyright (c) 2018 likuku. All rights reserved.
last update on Dec23,2018
"""

import sys
import os
import requests
import random
import time

USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',)
# headers={'User-Agent': random.choice(USER_AGENTS)}

def check_photo_page_in_local(_str_input_page_url,_str_input_photo_dir_path):
    _url_str = _str_input_page_url
    _dir_path_str = _str_input_photo_dir_path
    _page_name_str = _url_str.rsplit('/',1)[1]
    _page_path_str = '%s/html/%s.html' % (_dir_path_str,_page_name_str)
    _bool_src_media_path = os.path.isfile(_page_path_str)
    return(_bool_src_media_path)

def get_photo_page(_str_input_page_url,_str_input_photo_dir_path):
    _url_str = _str_input_page_url
    _dir_path_str = _str_input_photo_dir_path
    try:
        pass
        _page_name_str = _url_str.rsplit('/',1)[1]
        _page_path_str = '%s/html/%s.html' % (_dir_path_str,_page_name_str)
        _response = requests.get(_url_str, headers={'User-Agent': random.choice(USER_AGENTS)})
        #print(_response.headers)
        if _response.status_code == requests.codes.ok:
            open(_page_path_str, 'wb').write(_response.content)
    except Exception as e:
        raise

def make_str_photo_page_url(_str_flickr_id,_str_photo_file_name):
    _str_flickr_base_url = 'https://www.flickr.com/photos'
    _str_photo_id = _str_photo_file_name.rsplit('.')[0].split('flickr_')[1]
    _str_photo_page_url = '%s/%s/%s' % (_str_flickr_base_url,
                                        _str_flickr_id,
                                        _str_photo_id)
    return(_str_photo_page_url)

def get_str_list_photo_file_name_in_dir(_str_dir_path):
    _str_list = []
    with os.scandir(_str_dir_path) as it:
        for entry in it:
            if entry.name.startswith('flickr_') and entry.is_file():
                _str_list.append(entry.name)
    return(_str_list)

def check_str_raw_src_media_path(_str_input):
    if len(_str_input) == 0:
        _bool_src_media_path = False
    else:
        _bool_src_media_path = os.path.isdir(_str_input.replace('"','').strip())
    return(_bool_src_media_path)

def get_str_raw_src_flickr_id_from_keyboard():
    _str_input_msg = 'Please enter photo`s FlickrID : '
    _str_raw_input = str(input(_str_input_msg))
    return(_str_raw_input)

def get_str_raw_src_photo_dir_path_from_keyboard():
    _str_input_msg = 'Please enter a photo dir path : '
    _str_raw_input = str(input(_str_input_msg))
    return(_str_raw_input)

def test(arg):
    pass

def main():
    _str_raw_photo_dir = get_str_raw_src_photo_dir_path_from_keyboard()
    if check_str_raw_src_media_path(_str_raw_photo_dir) is True:
        pass
    else:
        print('The photo dir cannot be accessed. After running again, re-enter')
        time.sleep(2)
        exit()
    _str_flickr_id = get_str_raw_src_flickr_id_from_keyboard()
    if len(_str_flickr_id) is not 0:
        pass
    else:
        print('Input error. After running again, re-enter')
        time.sleep(2)
        exit()
    _str_list_photo = get_str_list_photo_file_name_in_dir(_str_raw_photo_dir)
    for _str_photo_file in _str_list_photo:
        _str_photo_page_url = make_str_photo_page_url(_str_flickr_id,_str_photo_file)
        if check_photo_page_in_local(_str_photo_page_url,_str_raw_photo_dir):
            continue
        else:
            pass
        print(_str_photo_page_url)
        get_photo_page(_str_photo_page_url,_str_raw_photo_dir)
        time.sleep(random.choice((0.1,0.2,0.3,0.4,0.5)))

if __name__ == '__main__':
    main()
