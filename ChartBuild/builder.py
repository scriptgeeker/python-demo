import os
import json
import hashlib
import webbrowser

# HTML 模板
HTML_CHART = '''
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>{chartName}</title></head>
<body><div style="margin: auto;width: 900px"><canvas id="my-chart"></canvas></div></body>
<script src="{chartjs}"></script>
<script type="text/javascript">
new Chart(document.getElementById("my-chart"), {{
    type: "{chartType}",
    data: {{
        labels: {labels},
        datasets:{datasets}
    }},
    options: {{
        title: {{display:true,text:"{chartName}"}},
        legend: {{display:false}},layout: {{padding:30}},
        scales: {{yAxes:[{{ticks:{{beginAtZero:true}}}}]
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
CHART_TYPE = {'bar': '柱状图', 'line': '折线图', 'pie': '饼图', 'doughnut': '环形图',
              'horizontalBar': '条形图', 'radar': '雷达图', 'polarArea': '极地图', }


class ChartBuilder():
    CDNJS = 'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js'
    BAR, LIN, PIE, DOU, HOR, RAD, POL = range(len(CHART_TYPE))

    def __init__(self, title: str, type: int, data: map):
        self.__chartType = list(CHART_TYPE.keys())[type]
        self.__chartName = title + CHART_TYPE[self.__chartType]
        self.__labels = list(data.keys())
        self.__data = list(data.values())
        self.__background = BG_COLOR
        self.__chartjs = self.CDNJS

    def setLibrary(self, library: str):
        self.__chartjs = library
        return self

    def setColor(self, color: list):
        self.__background = color
        return self

    def build(self):
        chartjs = self.__chartjs
        charType = self.__chartType
        labels = self.__labels
        chartName = self.__chartName
        datasets = json.dumps([{'data': self.__data, 'backgroundColor': self.__background}])
        html = HTML_CHART.format(chartjs=chartjs, chartType=charType, labels=labels,
                                 datasets=datasets, chartName=chartName)
        return html

    def save(self, path='./chart', name=''):
        path = os.path.abspath(path).replace('\\', '/')
        if name == '':
            name = self.__chartName + '.html'
        filepath = os.path.join(path, name)
        os.makedirs(os.path.dirname(filepath), mode=0o777, exist_ok=True)
        with open(filepath, 'w', encoding='utf8') as fw:
            fw.write(self.build())
        return filepath

    def show(self):
        md5 = hashlib.md5()
        md5.update(self.__chartName.encode())
        filename = md5.hexdigest() + '.html'
        filepath = self.save(path='./cache', name=filename)
        webbrowser.open('file:///' + filepath)


if __name__ == '__main__':
    data = {"Red": 15, "Blue": 24, "Yellow": 12, "Green": 6, "Purple": 9, "Orange": 3}
    color = ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(255, 206, 86, 0.6)',
             'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)']
    builder = ChartBuilder(title='颜色', type=ChartBuilder.BAR, data=data)
    builder.setColor(color=color)
    builder.show()
