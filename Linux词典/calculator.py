'''
GTK 和 WEBVIEWGTK最初是GIMP的专用开发库（GIMP Toolkit），后来发展为Unix-like系统下开发图形界面的应用程序的主流开发工具之一。
GTK是自由软件，并且是GNU计划的一部分。GTK的许可协议是LGPL。GTK使用C语言开发，但是其设计者使用面向对象技术。 
也提供了C++（gtkmm）、Perl、Ruby、Java和Python（PyGTK）绑定。在这门课程中，我们将使用pygtk进行开发。

1. GTK中的布局GTK图形界面也像其他图形程序一样，由窗口，容器，控件，以及各种事件处理函数组成。
其中窗口布局管理是很重要的一部分内容，因为这决定了我们的图形程序长什么样子。所谓布局管理就是在窗口中布置各种控件。
各种控件可以放在一个“包”中进行统一显示处理，这种包就是GTK中的容器，其实它也是一个控件，只是不是可见的，它的作用就是用于包含其各种控件。GTK中有各种各样的容器控件，
'''

import pygtk
pygtk.require('2.0')
import gtk

class Calculator(gtk.Window):
    def __init__(self):
        super(Calculator, self).__init__()
        self.set_title("Calculator")
        self.set_size_request(250, 230)
        self.set_position(gtk.WIN_POS_CENTER)
        '''
        使用vbox = gtk.VBox(False, 2) 我们创建了一个垂直的容器( vertical container box)，其中参数False指明了该容器中的控件不会是均匀大小的，参数2指明了该容器子部件之间的距离，单位是像素。
        '''
        vbox = gtk.VBox(False, 2)
        '''
        我们使用 Table 容器部件创建了一个计算器的框架。table = gtk.Table(5, 4, True)我们创建了一个 5 行 4 列的 table 容器部件。第三个参数是同质参数，如果被设置为 ture，table 中所有的部件将是相同的尺寸。而所有部件的尺寸与 table 容器中最大部件的尺寸相同。
        '''
        table = gtk.Table(5, 4, True)
        '''
        table.attach(gtk.Button("Cls"), 0, 1, 0, 1)我们附加了一个按钮到 table 容器中，其位置在表格的左上单元（cell）。前面两个参数代表这个单元的左侧和右侧，后两个参数代表这个单元的上部和下部。Table中的单元是依靠这 个单元的四个点的位置来确定的。
        '''
        table.attach(gtk.Button("Cls"), 0, 1, 0, 1)
        table.attach(gtk.Button("Bck"), 1, 2, 0, 1)
        table.attach(gtk.Label(), 2, 3, 0, 1)
        table.attach(gtk.Button("Close"), 3, 4, 0, 1)
        table.attach(gtk.Button("7"), 0, 1, 1, 2)
        table.attach(gtk.Button("8"), 1, 2, 1, 2)
        table.attach(gtk.Button("9"), 2, 3, 1, 2)
        table.attach(gtk.Button("/"), 3, 4, 1, 2)
        table.attach(gtk.Button("4"), 0, 1, 2, 3)
        table.attach(gtk.Button("5"), 1, 2, 2, 3)
        table.attach(gtk.Button("6"), 2, 3, 2, 3)
        table.attach(gtk.Button("*"), 3, 4, 2, 3)
        table.attach(gtk.Button("1"), 0, 1, 3, 4)
        table.attach(gtk.Button("2"), 1, 2, 3, 4)
        table.attach(gtk.Button("3"), 2, 3, 3, 4)
        table.attach(gtk.Button("-"), 3, 4, 3, 4)
        table.attach(gtk.Button("0"), 0, 1, 4, 5)
        table.attach(gtk.Button("."), 1, 2, 4, 5)
        table.attach(gtk.Button("="), 2, 3, 4, 5)
        table.attach(gtk.Button("+"), 3, 4, 4, 5)
        vbox.pack_start(gtk.Entry(), False, False, 0)
        '''
        vbox.pack_end(table, True, True, 0)我们将table 容器部件放置到垂直箱子容器中。最后我们使用窗口的shwo_all()方法，显示了所有的控件。
        '''
        vbox.pack_end(table, True, True, 0)
        self.add(vbox)
        self.connect("destroy", gtk.main_quit)
        self.show_all()

Calculator()
gtk.main()