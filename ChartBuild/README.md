## 绘制图表

利用开源的HTML5工具，绘制Canvas图表

----------

### 图表效果

```
var ctx = document.getElementById("myChart");
var chartInstanc = new Chart(ctx, {
    type: "bar",
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [{
            label: "lable",
            data: [12, 19, 3, 5, 2, 3]
        }]
    },
    options: {
        scales: {
            yAxes: [{ticks: {beginAtZero: true}}]
        },
    }
});
```

### 前端工具

> Simple HTML5 Charts using the canvas element chartjs.org

GitHub:  https://github.com/chartjs/Chart.js
CSDN:    https://cdnjs.com/libraries/Chart.js
Doc:     http://www.chartjs.org/docs/latest/


### 文件索引

 - demo.html（chart.js使用示范 - Chart.js use demonstration）

### 参考博客
[【segmentfault farmerz】chart.js 文档翻译][1]


  [1]: https://segmentfault.com/a/1190000008498664