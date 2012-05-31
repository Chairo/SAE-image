SAE-image
=========

演示：http://7ats.sinaapp.com/upload

需要创建一个名为“images”的Storage，或者在setting.py中修改成自己的Storage名称

config.yaml中修改sae名称和版本号

##api使用方法
<pre>import requests

if __name__ == '__main__':
    data = open('aa.jpg','rb')
    r = requests.put('http://7ats.sinaapp.com/api/upload', data={'data': data.read(), 'filename':"1.jpg"})
    print r.content</pre>
