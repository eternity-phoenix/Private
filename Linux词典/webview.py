'''
webview其实就是浏览器控件，所谓浏览器控件是指这个控件可以用来解析html字符串，就像网页一样显示。
'''

import gtk 
import webkit 

view = webkit.WebView() 

sw = gtk.ScrolledWindow() 
sw.add(view) 

win = gtk.Window(gtk.WINDOW_TOPLEVEL) 
win.add(sw) 
win.set_title("shiyanlou")
win.show_all() 

view.open("http://www.shiyanlou.com") 
gtk.main()