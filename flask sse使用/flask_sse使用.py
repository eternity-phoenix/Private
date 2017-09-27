'''
Web即时通信

所谓Web即时通信，就是说我们可以通过一种机制在网页上立即通知用户一件事情的发生，是不需要用户刷新网页的。Web即时通信的用途有很多，比如实时聊天，即时推送等。如当我们在登陆浏览 知乎时如果有人回答了我们的问题，知乎就会即时提醒我们，再比如现在电子商务的在线客服功能。这些能大大提高用户体验的功能都是基于Web即时通信实现的。

普通HTTP流程
客户端从服务器端请求网页
服务器作出相应的反应
服务器返回相应到客户端
而由于HTTP请求是无状态的，也就是说每次请求完成后，HTTP链接就断开了，服务器和浏览器互相之间是完全不可知的，只有下一次再发起一次请求 才能更新相应的信息。谈到这里我们就不难想到，我们可以简单的让浏览器每隔一个周期就发起一次请求，这样就能在一定程度上模拟实时效果了，这也就是轮训，术语叫做Polling。

Polling流程
客户端使用普通的http方式向服务器端请求网页
客户端执行网页中的JavaScript轮询脚本，定期循环的向服务器发送请求（例如每5秒发送一次请求），获取信息
服务器对每次请求作出响应，并返回相应信息，就像正常的http请求一样
通过轮训的方式我们就可以相对即时的获取信息。但是由于轮训的原理是使浏览器频繁的向服务器发起请求，这在一定程度上会造成性能效率问题。为了优化 这些性能问题，人们又想到了一种方法。那就是在服务器接收到请求的时候不理解返回，而是只有当有数据变化（或者超时）的时候才返回。这样一来，我们就可以 利用一次请求最大可能的保持连接的有效性，大大的减少了Polling中的请求次数。这个方法叫做长轮训，也叫做Long-Polling。

以上方法是实现Web实时通信的常用方法。当然在HTML5出来之后，我们就有更好的选择啦。在HTML5中，我们可以使用SSE或者是WebSocket。SSE的全称是Server Send Event，听名字就很好理解啦。也就是由服务器来推送数据。看到这里是不是兴奋呢？其实很多情况下，我们只需要这种简单的功能：由服务器推送数据到浏览器。比如推送比赛信息、股价的变化等等。

如果SSE还不能满足我们的需求的话，我们完全就可以使用WebSocket啦。当使用WebSocket时，浏览器和服务器之间就建立了一个全双工通道，互相都可以发送消息，完全的做到了及时，就像使用tcp socket一样。

SSE和WebSocket的简单对比：
WebSocket是全双工通道，可以双向通信，功能更强；SSE是单向通道，只能服务器向浏览器端发送。
WebSocket是一个新的协议，需要服务器端支持；SSE则是部署在HTTP协议之上的，现有服务器软件都支持。
SSE是一个轻量级协议，相对简单；WebSocket是一种较重的协议，相对复杂。
'''
#!/usr/bin/env python
import datetime
import flask
import redis


app = flask.Flask(__name__)
app.secret_key = 'asdf'
red = redis.StrictRedis(host='localhost', port=6379, db=6)


def event_stream():
    '''
    Redis是很流行的一个内存数据库，可以用于实现缓存，队列等服务。在这门项目课程中我们将使用的Redis的发布/订阅功 能。简单来说，我们所谓订阅功能就是我们可以订阅一些频道，然后当这些频道有新的消息的时候我们就可以自动接收这些信息。当服务器接收到浏览器POST过 来的消息的时候，会将这些信息发布到特定的频道中。接着我们之前订阅了这些频道的客户端就回自动收到这些消息，最后我们就将这些消息通过SSE推送到客户端。
    '''
    pubsub = red.pubsub()
    pubsub.subscribe('chat')
    # TODO: handle client disconnection.
    for message in pubsub.listen():
        print(message)
        # SSE协议要求的信息的格式也非常简单，就是前缀data:加上发送的数据内容，然后以\n\n结尾。
        yield 'data: %s\n\n' % message['data']


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        flask.session['user'] = flask.request.form['user']
        return flask.redirect('/')
    return '<form action="" method="post">user: <input name="user">'


@app.route('/post', methods=['POST'])
def post():
    message = flask.request.form['message']
    user = flask.session.get('user', 'anonymous')
    now = datetime.datetime.now().replace(microsecond=0).time()
    red.publish('chat', u'[%s] %s: %s' % (now.isoformat(), user, message))
    return flask.Response(status=204)


@app.route('/stream')
def stream():
    # 浏览器怎么样知道这是一个服务器事件流呢？其实很简单啦，就是将HTTP的头部Content-Type设置成text/event-stream就可以了。
    # 下面的代码是受到flask支持的,flask发现mimetype设置为text/event-stream,而且参数是一个iterable对象
    # 就会自动调用这个iter的next来不断返回数据,而不是关闭链接
    return flask.Response(event_stream(),
                          mimetype="text/event-stream")


@app.route('/')
def home():
    if 'user' not in flask.session:
        return flask.redirect('/login')
    return u"""
        <!doctype html>
        <title>chat</title>
        <script src="http://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
        <style>body { max-width: 500px; margin: auto; padding: 1em; background: black; color: #fff; font: 16px/1.6 menlo, monospace; }</style>
        <p><b>hi, %s!</b></p>
        <p>Message: <input id="in" /></p>
        <pre id="out"></pre>
        <script>
            function sse() {
                var source = new EventSource('/stream');
                var out = document.getElementById('out');
                source.onmessage = function(e) {
                    // XSS in chat is fun
                    out.innerHTML =  e.data + '\\n' + out.innerHTML;
                };
            }
            $('#in').keyup(function(e){
                if (e.keyCode == 13) {
                    $.post('/post', {'message': $(this).val()});
                    $(this).val('');
                }
            });
            sse();
        </script>
    """ % flask.session['user']


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8989, threaded=True)
