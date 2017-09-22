from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

'''
模板中表单的渲染；
数据的验证工作，某一些输入不合法也不会丢失已经输入的数据；
还可以定制更复杂的验证工作，如果提供了 10 个输入框，必须要输入其中两个以上等功能，在 forms.py 中实现都是很容易的。
另外也有一些将 Django forms 渲染成 Bootstrap 的插件，使用起来十分方便。
'''
