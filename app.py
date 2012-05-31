# -*- coding:utf-8 -*-
from Core.bottle import Bottle, debug, jinja2_template as template, TEMPLATE_PATH, static_file, request, response
from setting import STORAGE_DOMAIN_NAME

import sae.storage, time, random
app = Bottle()
debug(True)
TEMPLATE_PATH.append('static/template/')

def RandUrl(length):
    '''随机字符串'''
    source = ['A','B','C','D','E','F','G','H','I','J','K','L',\
              'M','N','O','P','Q','R','S','T','U',\
              'V','W','X','Y','Z','a','b','c','d','e','f','g',\
              'h','i','j','k','l','m','n','o','p','q','r','s',\
              't','u','v','w','x','y','z'\
              '1','2','3','4','5','6','7','8','9','0'
              ]
    return ''.join(random.sample(source, length))

@app.get('/static/<filename:re:.*[^/]>')
def server_static_file(filename):
    return static_file(filename, root='./static/')

@app.get('/index')
@app.get('/')
def index():
    return 'index'

@app.get('/upload')
def upload():
    return template("upload.html")

@app.post('/upload_c')
def upload_c_post():
    data = request.files.get('Filedata')
    _filetype = data.filename.split('.')[-1].lower()
    _filename = '%s%s.%s'%(str(int(time.time())), RandUrl(6), _filetype)
    _content_type='image/%s'%_filetype
    _content = data.file.read()
    put_obj2storage(_filename, _content, expires='365', type=_content_type)
    return _filename

@app.put('/api/upload')
@app.post('/api/upload')
def api_upload():
    _data = request.POST.get('data')
    _filetype = request.POST.get('filename').split('.')[-1].lower()
    _filename = '%s%s.%s'%(str(int(time.time())), RandUrl(6), _filetype)
    _content_type='image/%s'%_filetype
    put_obj2storage(_filename, _data, expires='365', type=_content_type)
    return '/img/%s'%_filename


@app.get('/img/<filename:re:.*[^/]>')
def get_img(filename):
    _filetype = filename.split('.')[-1]
    response.add_header('Content-type', 'image/%s'%_filetype)
    return get_obj_from_storage(filename)

def put_obj2storage(file_name = '', data = '', expires='365', type=None, encoding= None, domain_name = STORAGE_DOMAIN_NAME):
    '''存进storage'''
    s = sae.storage.Client()
    ob = sae.storage.Object(data = data, cache_control='access plus %s day' % expires, content_type= type, content_encoding= encoding)
    return s.put(domain_name, file_name, ob)

def get_obj_from_storage(file_name = '', domain_name = STORAGE_DOMAIN_NAME):
    '''从storage中获取数据'''
    s = sae.storage.Client()
    ob = s.get(domain_name, file_name)
    return ob.data
