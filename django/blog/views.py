from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm

# Create your views here.

def add2(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def index(request):
    if request.method == 'POST':
        # 当表单以 POST 方式提交的时候
        form = AddForm(request.POST)
        if form.is_valid():
            # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        # 正常方位时
        form = AddForm()

    return render(request, 'index.html', {'form': form})