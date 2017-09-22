django-admin.py startproject project-name
在 Windows 系统下，如果报错，尝试用 django-admin 代替 django-admin.py。

python3 manage.py startapp app-name
django-admin.py startapp app-name

python manage.py makemigrations
python manage.py migrate

# 默认情况下在 0.0.0.0:8080 启动
python manage.py runserver 
# 当提示端口被占用的时候，可以用其他端口 python manage.py runserver 8081

python manage.py flush
此命令会询问是 yes 还是 no，选择 yes 会把数据库全部清空掉，只留下空表。

python manage.py createsuperuser
# 按照提示输入用户名和对应的密码可以，邮箱可以留空，用户名和密码必填
# 修改用户密码可以使用以下命令
python manage.py changepassword username

导出数据 导入数据 *
python manage.py dumpdata appname > appname.json
python manage.py loaddata appname.json


Django 项目环境终端
python manage.py shell
如果你安装了 bpython 或 ipython 会自动用它们的界面，这里推荐使用 ipython。
这个命令和直接运行 python 进入 shell 的区别是：**你可以在这个 shell 里面调用当前项目的 models.py 中的 API，对于操作数据，还有一些小测试非常方便。


数据库命令行
python manage.py dbshell
Django 会自动进入在 settings.py 中设置的数据库，如果是 MySQL 或 postgreSQL ，会要求输入数据库用户密码。在这个终端可以执行数据库的 SQL 语句。


直接在终端上输入以下命令，可以看到详细的列表，在忘记参数名时特别有用。
python manage.py



------------------------
Django 模板查找机制：查找模板的过程是在每个 app 的 templates 目录中找，每个 app 的 template 形成一个目录列表，Django 遍历这个列表
一个个目录进行查询，当在某一个目录中找到时就停止，所有的都遍历之后，仍旧找不到指定的模板，则进入 Template Not Found 状态。
这一点与 Python 对包的查询过程十分类似。这样的设计当然也有利弊，好处是一个 app 可以用另一个 app 的模板文件，
而弊端就是可能会发现查询错误的情况，所以我们在 templates 中再以 app 名对其进行细分，则会更加清晰。例如下面这个项目的目录结构，就是笔者比较推荐的：

zqxt
├── tutorial
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── templates
│   │   └── tutorial
│   │       ├── index.html
│   │       └── search.html
│   ├── tests.py
│   └── views.py
├── tryit
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── templates
│   │   └── tryit
│   │       ├── index.html
│   │       └── poll.html
│   ├── tests.py
│   └── views.py
├── manage.py
└── zqxt
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
这样，使用的时候，模板就是 "tutorial/index.html" 和 "tryit/index.html" 这样有app作为名称的一部分，就不会混淆。

变量				描述
forloop.counter		索引从 1 开始算
forloop.counter0	索引从 0 开始算
forloop.revcounter	索引从最大长度到 1
forloop.revcounter0	索引从最大长度到 0
forloop.first		当遍历的元素为第一项时为真
forloop.last		当遍历的元素为最后一项时为真
forloop.parentloop	用在嵌套的 for 循环中，获取上一层 for 循环的 forloop



===================================
备注：name 和 age 等字段中不能有 __（双下划线，因为在Django QuerySet API中有特殊含义（用于关系，包含，不区分大小写，以什么开头或结尾，日期的大于小于，正则等）。
也不能有Python中的关键字，name 是合法的，studentname 也合法，但是student\_name不合法，try, class, continue 也不合法，
因为它是Python的关键字( import keyword; print(keyword.kwlist) 可以打出所有的关键字)。

3.1 增操作

新建一个对象的写法有以下几种：

# 1
Person.objects.create(name = name, age = age)

# 2
p = Person(name = name, age = age)
p.save()

# 3
p = Person(name = name)
p.age = age
p.save()

# 4 
Person.objects.get_or_create(name = name, age = age)
第四种方法是防止重复的很好方法，但是速度相对较慢，返回一个元祖，第一个为 Person 对象，第二个为 True 或 False 布尔量。新建时返回的是 True，已经存在时返回 False。

3.2 查操作

查找一个对象有更多的方式：

# 1
Person.objects.all()

# 2. 切片操作，获取10个人，不支持负索引，切片可以节约内存
Person.objects.all()[:10]

# 3
Person.objects.get(name = name)

# 4. get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到 filter
Person.objects.filter(name = "abc")

# 5. 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件
Person.objects.filter(name__iexact = "abc")

# 6. 名称中包含 "abc"的人
Person.objects.filter(name__contains = "abc")

# 7. 名称中包含 "abc"，且abc不区分大小写
Person.objects.filter(name__icontains = "abc")

# 8. 正则表达式查询
Person.objects.filter(name__regex = "^abc")

# 9. 正则表达式不区分大小写
Person.objects.filter(name__iregex = "^abc")

# 10. 排除包含 WZ 的Person对象
Person.objects.exclude(name__contains = "WZ")

# 11. 找出名称含有abc, 但是排除年龄是23岁的
Person.objects.filter(name__contains="abc").exclude(age = 23)




