import os
import json
import random
import webbrowser

# HTML 模板
HTML_CHART = '''
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>{chartName}</title></head>
<body><div style="margin: auto;width: 900px"><canvas id="my-chart"></canvas></div></body>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js"></script>
<script type="text/javascript">
new Chart(document.getElementById("my-chart"), {{
    type: "{chartType}",
    data: {{
        labels: {labels},
        datasets:{datasets}
    }},
    options: {{
        title: {{display:true,text:"{chartName}",position:"bottom"}},
        layout: {{padding:30}},scales: {{yAxes:[{{ticks:{{beginAtZero:true}}}}]
        }}
    }}
}});
</script>
</html>
'''
# 绘图颜色
BG_COLOR = ["rgba(244, 67, 54, 0.5)", "rgba(233, 30, 99, 0.5)", "rgba(156, 39, 176, 0.5)", "rgba(103, 58, 183, 0.5)",
            "rgba(63, 81, 181, 0.5)", "rgba(33, 150, 243, 0.5)", "rgba(3, 169, 244, 0.5)", "rgba(0, 188, 212, 0.5)",
            "rgba(0, 150, 136, 0.5)", "rgba(76, 175, 80, 0.5)", "rgba(139, 195, 74, 0.5)", "rgba(205, 220, 57, 0.5)",
            "rgba(255, 235, 59, 0.5)", "rgba(255, 193, 7, 0.5)", "rgba(255, 152, 0, 0.5)", "rgba(255, 87, 34, 0.5)", ]

# 图表类型
CHART_TYPE = {'柱状图': 'bar', '折线图': 'line', '饼图': 'pie', '环形图': 'doughnut',
              '条形图': 'horizontalBar', '雷达图': 'radar', '极地图': 'polarArea', }

if __name__ == '__main__':
    chartTitle = input('图表标题：')  # 例如：编程语言排行榜
    chartType = input('图表类型：')  # 例如：柱状图
    chartName = chartTitle + chartType
    chartType = CHART_TYPE[chartType]
    # 输入具体数据
    labels = input('数据字段：').strip().split(',')  # 例如：java,php,python
    types = input('数据分类：').strip().split(',')  # 例如：2016,2017,2018
    datasets = list()
    for type in types:
        data = list()
        print('{:*^30}'.format(type))
        for label in labels:
            data.append(input(label + '：'))
        datasets.append({'label': type, 'data': data, 'backgroundColor': BG_COLOR})
    # 生成HTML文件
    html = HTML_CHART.format(chartType=chartType, labels=labels, datasets=json.dumps(datasets), chartName=chartName)
    filepath = os.path.abspath('./chart').replace('\\', '/') + '/' + chartName + '.html'
    os.makedirs(os.path.dirname(filepath), mode=0o777, exist_ok=True)
    with open(filepath, 'w', encoding='utf8') as fw:
        fw.write(html)
    # 调用浏览器打开
    webbrowser.open('file:///' + filepath)
