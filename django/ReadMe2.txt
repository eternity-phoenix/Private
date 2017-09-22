Django 中缓存技术的配置与实现

缓存系统需要一些设置才能启用。也就是说你需要告诉 Django 要把数据存在哪里，即数据库中、文件系统或是直接存在内存中。这个决定回影响你的缓存性能。

缓存配置是通过 settings.py 文件的 CACHES 配置来实现，以下我们来列举出最常用的缓存配置变量。

数据库缓存

Django 可以把缓存保存在数据库中。如果你有一个快速、专业的数据库服务器的话那这种方式是效果最好的。为了把数据表用来做为缓存后端，你需要进行以下两个操作：

将 BACKEND：设置为 django.core.cache.backends.db.DatabaseCache
把 LOCATION 设置为数据表名称。这个名字可以是任何你想要的名字，只要它是一个合法的表名并且在你的数据库中没有被使用过。



在使用数据库缓存之前，需要用以下命令创建缓存表：

python manage.py createcachetable
这将在你的数据库中创建一个 Django 的基于数据库缓存系统预期的特定格式数据表。表名会从 LOCATION 中获得。



django.views.decorators.cache.cache_page()
更加轻巧的缓存框架使用方法是对单个有效视图的输出进行缓存。 django.views.decorators.cache 定义了一个自动缓存视图响应的 cache_page 装饰器，使用非常简单：

from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def my_view(request):
    return render(request, 'index.html', {'queryset':queryset})



虚拟缓存（用于开发）

Django 有一个 dummy 缓存，而且还不是真正的缓存 - 它只提供了一个缓存接口，但是什么也不会做。如果你在项目中使用缓存技术，但是在开发调试的时候不想开启缓存机制，你可以在 settings.py 进行设置，即可随即切换缓存开关。

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


==================================================================
使用 uwsgi 来运行项目

uwsgi --http :8001 --chdir /path/to/project --home=/path/to/env --module project.wsgi
其中 --home 指定 virtualenv 路径，如果没有也可以去掉。 project.wsgi 指的是 project/wsgi.py 文件。


生成 supervisor 默认配置文件，比如我们放在 /etc/supervisord.conf 路径中：

$ sudo echo_supervisord_conf > /etc/supervisord.conf
$ cat /etc/supervisord.conf

[program:shiyanlou]
command=/path/to/uwsgi --http :8003 --chdir /path/to/shiyanlou --module shiyanlou.wsgi
directory=/path/to/shiyanlou
startsecs=0
stopwaitsecs=0
autostart=true
autorestart=true


启动 supervisor

sudo supervisord -c /etc/supervisord.conf
重启 shiyanlou 程序

sudo supervisorctl -c /etc/supervisord.conf restart shiyanlou
sudo supervisorctl -c /etc/supervisord.conf [start|stop|restart] [program-name|all]


//////////////////////////////////////////////
以 uwsgi 为例，上面这样使用一行命令太长了，我们使用 ini 配置文件来搞定，比如项目在 /home/tu/shiyanlou 这个位置，

在其中新建一个 uwsgi.ini 全路径为 /home/tu/shiyanlou/uwsgi.ini：

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
注意上面的 /home/tu/shiyanlou/shiyanlou.sock ，一会儿我们把它和 nginx 关联起来。

在项目上新建一个空白的 reload 文件，只要 touch 一下这个文件（touch reload) 项目就会重启。

修改 supervisor 配置文件中的 command 一行：

[program:shiyanlou]
command=/path/to/uwsgi --ini /home/tu/shiyanlou/uwsgi.ini
directory=/path/to/shiyanlou
startsecs=0
之后重启 supervisor：

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


