// 画布设定了200*200,但我们并不需要200*200这么精确的输入数据，20*20就很合适。
(function(window) {
    'use strict';

    class Info
    {
        constructor(p) {
            this.obj = p;
            this._style = this.style;
            this._innerText = this.obj.innerText;
        }

        info(message) {
            this.setStyle('color', 'yellow');
            this.show(message, 3000);
        }

        error(message) {
            this.setStyle('color', 'red');
            this.show(message, 3000);
        }

        setStyle(key, value) {
            let style = this.style;
            style[key] = value;

            let styleStr = "";
            for(let key in style) {
                styleStr += key + ':' + style[key] + ';';
            }
            this.obj.setAttribute('style', styleStr);
        }

        set style(value) {
            let styleStr = "";
            for(let key in value) {
                styleStr += key + ':' + value[key] + ';';
            }
            this.obj.setAttribute('style', styleStr);
        }

        get style() {
            let style = this.obj.getAttribute('style') || "";
            let styles = {};
            for(let item of style.split(";")) {
                let [key, value] = item.split(":");
                styles[key] = value || "";
            }
            return styles;
        }

        show(message, time) {
            this.obj.innerText = message;
            setTimeout(this.reset, time);
        }

        get reset() {
            return () => {
                this.style = this._style;
                this.obj.innerText = this._innerText;
            };
        }
    }

    var ocrDemo = {
        CANVAS_WIDTH: 200,
        TRANSLATE_WIDTH: 20,
        PIXEL_WIDTH: 10, // TRANSLATED_WIDTH = CANVAS_WIDTH / PIXEL_WIDTH

        BATCH_SIZE: 1,


        // 服务端参数
        PORT: 9000,
        HOST: 'http://localhost',

        // 颜色变量
        BLACK: '#000000',
        BLUE: '#0000FF',
        WHITE: '#FFFFFF',

        // 客户端训练数据集
        trainArray: [],
        trainingRequestCount: 0,

        onLoadFunction: function() {
            this.resetCanvas();
        },

        resetCanvas: function() {
            let canvas = document.getElementById('canvas');
            let ctx = canvas.getContext('2d');

            this.INFO = new Info(document.getElementById('info'));
            this.data = new Array(this.CANVAS_WIDTH * this.CANVAS_WIDTH);
            this.data.fill(0);

            ctx.fillStyle = this.BLACK;
            ctx.fillRect(0, 0, this.CANVAS_WIDTH, this.CANVAS_WIDTH);
            this.drawGrid(ctx);

            // 绑定事件操作
            canvas.onmousemove = e => { this.onMouseMove(e, ctx, canvas); };
            canvas.onmousedown = e => { this.onMouseDown(e, ctx, canvas); };
            canvas.onmouseup = e => { this.onMouseUp(e, ctx, canvas); };
        },

        // 在画布上加上网格辅助输入和查看：
        drawGrid: function(ctx) {
            ctx.strokeStyle = this.BLUE;
            for(let x = this.PIXEL_WIDTH, y = this.PIXEL_WIDTH;
                x < this.CANVAS_WIDTH;
                x += this.PIXEL_WIDTH, y += this.PIXEL_WIDTH) {
                    ctx.beginPath();
                    ctx.moveTo(x, 0);
                    ctx.lineTo(x, this.CANVAS_WIDTH);
                    ctx.stroke();

                    ctx.beginPath();
                    ctx.moveTo(0, y);
                    ctx.lineTo(this.CANVAS_WIDTH, y);
                    ctx.stroke();
            }
        },
        // 我们使用一维数组来存储手写输入，0代表黑色（背景色），1代表白色（笔刷色）。
        onMouseMove: function(e, ctx, canvas) {
            if(!canvas.isDrawing)
                return;
            this.fillSquare(ctx, e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop)
        },

        onMouseDown: function(e, ctx, canvas) {
            if(e.which !== 1) //左键
                return;
            canvas.isDrawing = true;
            this.fillSquare(ctx, e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
        },

        onMouseUp: function(e, ctx, canvas) {
            canvas.isDrawing = false;
        },

        fillSquare: function(ctx, x, y) {
            let xPixel = Math.floor(x / this.PIXEL_WIDTH);
            let yPixel = Math.floor(y / this.PIXEL_WIDTH);
            // 在这里存储输入
            this.data[((xPixel - 1) * this.TRANSLATE_WIDTH + yPixel) - 1] = 1;

            ctx.fillStyle = this.WHITE; // 白色
            ctx.fillRect(xPixel * this.PIXEL_WIDTH, yPixel * this.PIXEL_WIDTH, this.PIXEL_WIDTH, this.PIXEL_WIDTH);
        },

        train: function() {
            let digitvVal = document.getElementById('digit').value;
            // 如果没有输入标签或者没有手写输入就报错
            if(!digitvVal || this.data.indexOf(1) < 0) {
                this.INFO.error("Please type and draw a digit value in order to train the network");
                return;
            }
            // 将训练数据加到客户端训练集中
            this.trainArray.push({'y0': this.data, 'label': parseInt(digitvVal)});
            this.trainingRequestCount++;
            // 为什么要设置BATCH_SIZE呢？这是为了防止服务器在短时间内处理过多请求而降低了服务器的性能。
            if(this.trainingRequestCount === this.BATCH_SIZE)
            {
                this.INFO.info("Sending training data to server...");
                let json = {
                    trainArray: this.trainArray,
                    train: true
                };

                this.sendData(json);
                // 清空客户端训练集
                this.trainingRequestCount = 0;
                this.trainArray = [];
            }
        },

        // 发送预测请求
        test: function() {
            if(this.data.indexOf(1) < 0) {
                this.INFO.error('Please draw a digit in order to test the network');
                return;
            }
            let json = {
                image: this.data,
                predict: true
            };
            this.sendData(json);
        },

        // 处理服务器响应
        receiveResponse: function(xmlHttp) {
            if(xmlHttp.status !== 200) {
                this.INFO.error('Server returned status ' + xmlHttp.status);
                return;
            }
            let responseJson = JSON.parse(xmlHttp.responseText);
            if(xmlHttp.responseText && responseJson.type === 'test') {
                this.INFO.info("The neural network predicts you wrote a '" + responseJSON.result + "'");
            }
        },

        onError: function(xmlHttp) {
            this.INFO.error("Error occurred while connecting to server: " + xmlHttp.target.statusText);
        },

        sendData: function(json) {
            let xmlHttp = new XMLHttpRequest();
            let url = this.HOST + ':' + this.PORT;
            xmlHttp.open('POST', url, false);
            xmlHttp.onload = () => this.receiveResponse(xmlHttp);
            xmlHttp.onerror = () => this.onError(xmlHttp);
            let msg = JSON.stringify(json);
            //xmlHttp.setRequestHeader('Content-length', msg.length);
            //xmlHttp.setRequestHeader('Connection', 'close');
            xmlHttp.send(msg);
        }

    }


    window.ocrDemo = ocrDemo;
})(window);