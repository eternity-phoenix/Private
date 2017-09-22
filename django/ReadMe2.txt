Django �л��漼����������ʵ��

����ϵͳ��ҪһЩ���ò������á�Ҳ����˵����Ҫ���� Django Ҫ�����ݴ�����������ݿ��С��ļ�ϵͳ����ֱ�Ӵ����ڴ��С����������Ӱ����Ļ������ܡ�

����������ͨ�� settings.py �ļ��� CACHES ������ʵ�֣������������оٳ���õĻ������ñ�����

���ݿ⻺��

Django ���԰ѻ��汣�������ݿ��С��������һ�����١�רҵ�����ݿ�������Ļ������ַ�ʽ��Ч����õġ�Ϊ�˰����ݱ�������Ϊ�����ˣ�����Ҫ������������������

�� BACKEND������Ϊ django.core.cache.backends.db.DatabaseCache
�� LOCATION ����Ϊ���ݱ����ơ�������ֿ������κ�����Ҫ�����֣�ֻҪ����һ���Ϸ��ı���������������ݿ���û�б�ʹ�ù���



��ʹ�����ݿ⻺��֮ǰ����Ҫ����������������

python manage.py createcachetable
�⽫��������ݿ��д���һ�� Django �Ļ������ݿ⻺��ϵͳԤ�ڵ��ض���ʽ���ݱ�������� LOCATION �л�á�



django.views.decorators.cache.cache_page()
�������ɵĻ�����ʹ�÷����ǶԵ�����Ч��ͼ��������л��档 django.views.decorators.cache ������һ���Զ�������ͼ��Ӧ�� cache_page װ������ʹ�÷ǳ��򵥣�

from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def my_view(request):
    return render(request, 'index.html', {'queryset':queryset})



���⻺�棨���ڿ�����

Django ��һ�� dummy ���棬���һ����������Ļ��� - ��ֻ�ṩ��һ������ӿڣ�����ʲôҲ�����������������Ŀ��ʹ�û��漼���������ڿ������Ե�ʱ���뿪��������ƣ�������� settings.py �������ã������漴�л����濪�ء�

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


==================================================================
ʹ�� uwsgi ��������Ŀ

uwsgi --http :8001 --chdir /path/to/project --home=/path/to/env --module project.wsgi
���� --home ָ�� virtualenv ·�������û��Ҳ����ȥ���� project.wsgi ָ���� project/wsgi.py �ļ���


���� supervisor Ĭ�������ļ����������Ƿ��� /etc/supervisord.conf ·���У�

$ sudo echo_supervisord_conf > /etc/supervisord.conf
$ cat /etc/supervisord.conf

[program:shiyanlou]
command=/path/to/uwsgi --http :8003 --chdir /path/to/shiyanlou --module shiyanlou.wsgi
directory=/path/to/shiyanlou
startsecs=0
stopwaitsecs=0
autostart=true
autorestart=true


���� supervisor

sudo supervisord -c /etc/supervisord.conf
���� shiyanlou ����

sudo supervisorctl -c /etc/supervisord.conf restart shiyanlou
sudo supervisorctl -c /etc/supervisord.conf [start|stop|restart] [program-name|all]


//////////////////////////////////////////////
�� uwsgi Ϊ������������ʹ��һ������̫���ˣ�����ʹ�� ini �����ļ����㶨��������Ŀ�� /home/tu/shiyanlou ���λ�ã�

�������½�һ�� uwsgi.ini ȫ·��Ϊ /home/tu/shiyanlou/uwsgi.ini��

[uwsgi]
socket = /home/tu/shiyanlou/shiyanlou.sock
chdir = /home/tu/shiyanlou
wsgi-file = shiyanlou/wsgi.py
touch-reload = /home/tu/shiyanlou/reload

processes = 2
threads = 4

chmod-socket = 664
chown-socket = tu:www-data

vacuum = true
ע������� /home/tu/shiyanlou/shiyanlou.sock ��һ������ǰ����� nginx ����������

����Ŀ���½�һ���հ׵� reload �ļ���ֻҪ touch һ������ļ���touch reload) ��Ŀ�ͻ�������

�޸� supervisor �����ļ��е� command һ�У�

[program:shiyanlou]
command=/path/to/uwsgi --ini /home/tu/shiyanlou/uwsgi.ini
directory=/path/to/shiyanlou
startsecs=0
֮������ supervisor��

$ sudo supervisorctl -c /etc/supervisord.conf restart shiyanlou


---------------------------------------
server {
    listen      80;
    server_name test.shiyanlou.com;
    charset     utf-8;

    client_max_body_size 75M;

    location /media  {
        alias /path/to/project/media;
    }

    location /static {
        alias /path/to/project/static;
    }

    location / {
        uwsgi_pass  unix:///home/tu/shiyanlou/shiyanlou.sock;
        include     /etc/nginx/uwsgi_params;
    }
}


