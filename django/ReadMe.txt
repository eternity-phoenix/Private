django-admin.py startproject project-name
�� Windows ϵͳ�£�������������� django-admin ���� django-admin.py��

python3 manage.py startapp app-name
django-admin.py startapp app-name

python manage.py makemigrations
python manage.py migrate

# Ĭ��������� 0.0.0.0:8080 ����
python manage.py runserver 
# ����ʾ�˿ڱ�ռ�õ�ʱ�򣬿����������˿� python manage.py runserver 8081

python manage.py flush
�������ѯ���� yes ���� no��ѡ�� yes ������ݿ�ȫ����յ���ֻ���¿ձ�

python manage.py createsuperuser
# ������ʾ�����û����Ͷ�Ӧ��������ԣ�����������գ��û������������
# �޸��û��������ʹ����������
python manage.py changepassword username

�������� �������� *
python manage.py dumpdata appname > appname.json
python manage.py loaddata appname.json


Django ��Ŀ�����ն�
python manage.py shell
����㰲װ�� bpython �� ipython ���Զ������ǵĽ��棬�����Ƽ�ʹ�� ipython��
��������ֱ������ python ���� shell �������ǣ�**���������� shell ������õ�ǰ��Ŀ�� models.py �е� API�����ڲ������ݣ�����һЩС���Էǳ����㡣


���ݿ�������
python manage.py dbshell
Django ���Զ������� settings.py �����õ����ݿ⣬����� MySQL �� postgreSQL ����Ҫ���������ݿ��û����롣������ն˿���ִ�����ݿ�� SQL ��䡣


ֱ�����ն�����������������Կ�����ϸ���б������ǲ�����ʱ�ر����á�
python manage.py



------------------------
Django ģ����һ��ƣ�����ģ��Ĺ�������ÿ�� app �� templates Ŀ¼���ң�ÿ�� app �� template �γ�һ��Ŀ¼�б�Django ��������б�
һ����Ŀ¼���в�ѯ������ĳһ��Ŀ¼���ҵ�ʱ��ֹͣ�����еĶ�����֮���Ծ��Ҳ���ָ����ģ�壬����� Template Not Found ״̬��
��һ���� Python �԰��Ĳ�ѯ����ʮ�����ơ���������Ƶ�ȻҲ�����ף��ô���һ�� app ��������һ�� app ��ģ���ļ���
���׶˾��ǿ��ܻᷢ�ֲ�ѯ�������������������� templates ������ app ���������ϸ�֣��������������������������Ŀ��Ŀ¼�ṹ�����Ǳ��߱Ƚ��Ƽ��ģ�

zqxt
������ tutorial
��   ������ __init__.py
��   ������ admin.py
��   ������ models.py
��   ������ templates
��   ��   ������ tutorial
��   ��       ������ index.html
��   ��       ������ search.html
��   ������ tests.py
��   ������ views.py
������ tryit
��   ������ __init__.py
��   ������ admin.py
��   ������ models.py
��   ������ templates
��   ��   ������ tryit
��   ��       ������ index.html
��   ��       ������ poll.html
��   ������ tests.py
��   ������ views.py
������ manage.py
������ zqxt
    ������ __init__.py
    ������ settings.py
    ������ urls.py
    ������ wsgi.py
������ʹ�õ�ʱ��ģ����� "tutorial/index.html" �� "tryit/index.html" ������app��Ϊ���Ƶ�һ���֣��Ͳ��������

����				����
forloop.counter		������ 1 ��ʼ��
forloop.counter0	������ 0 ��ʼ��
forloop.revcounter	��������󳤶ȵ� 1
forloop.revcounter0	��������󳤶ȵ� 0
forloop.first		��������Ԫ��Ϊ��һ��ʱΪ��
forloop.last		��������Ԫ��Ϊ���һ��ʱΪ��
forloop.parentloop	����Ƕ�׵� for ѭ���У���ȡ��һ�� for ѭ���� forloop



===================================
��ע��name �� age ���ֶ��в����� __��˫�»��ߣ���Ϊ��Django QuerySet API�������⺬�壨���ڹ�ϵ�������������ִ�Сд����ʲô��ͷ���β�����ڵĴ���С�ڣ�����ȣ���
Ҳ������Python�еĹؼ��֣�name �ǺϷ��ģ�studentname Ҳ�Ϸ�������student\_name���Ϸ���try, class, continue Ҳ���Ϸ���
��Ϊ����Python�Ĺؼ���( import keyword; print(keyword.kwlist) ���Դ�����еĹؼ���)��

3.1 ������

�½�һ�������д�������¼��֣�

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
�����ַ����Ƿ�ֹ�ظ��ĺܺ÷����������ٶ���Խ���������һ��Ԫ�棬��һ��Ϊ Person ���󣬵ڶ���Ϊ True �� False ���������½�ʱ���ص��� True���Ѿ�����ʱ���� False��

3.2 �����

����һ�������и���ķ�ʽ��

# 1
Person.objects.all()

# 2. ��Ƭ��������ȡ10���ˣ���֧�ָ���������Ƭ���Խ�Լ�ڴ�
Person.objects.all()[:10]

# 3
Person.objects.get(name = name)

# 4. get��������ȡһ������ģ������Ҫ��ȡ����������һЩ�ˣ���Ҫ�õ� filter
Person.objects.filter(name = "abc")

# 5. ����Ϊ abc ���ǲ����ִ�Сд�������ҵ� ABC, Abc, aBC����Щ����������
Person.objects.filter(name__iexact = "abc")

# 6. �����а��� "abc"����
Person.objects.filter(name__contains = "abc")

# 7. �����а��� "abc"����abc�����ִ�Сд
Person.objects.filter(name__icontains = "abc")

# 8. ������ʽ��ѯ
Person.objects.filter(name__regex = "^abc")

# 9. ������ʽ�����ִ�Сд
Person.objects.filter(name__iregex = "^abc")

# 10. �ų����� WZ ��Person����
Person.objects.exclude(name__contains = "WZ")

# 11. �ҳ����ƺ���abc, �����ų�������23���
Person.objects.filter(name__contains="abc").exclude(age = 23)




