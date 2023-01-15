class Table():
    css = '''<style>
      * {
        margin: 0;
      }
      table {
        width: 100%;
        border-collapse: collapse;
        border: solid #ccc 1px;
      }
      table td,
      table,
      th {
        border-left: 1px solid #ccc;
        border-top: 1px solid #ccc;
        padding: 4px 8px;
        white-space: nowrap;
      }
      table tr:hover {
        background: #eee;
        color: #e94041;
      }
      table tr:nth-child(odd) {
        background-color: #f3f3f3;
      }
      a {
        color: #000;
        text-decoration: none;
      }
      a:hover {
        color: #e94041;
      }
      </style>'''

    column = []

    data = []

    def __init__(self, col, data) -> None:
        self.setColumn(col)
        self.setData(data)

    def setColumn(self, col):
        self.column = col

    def setData(self, data):
        self.data = data

    def table_head(self):
        table_th = []
        for item in self.column:
            table_th.append(f'<th>{item}</th>')

        return f'<tr>{"".join(table_th)}</tr>'

    def table_body(self, cell):
        tr = ''
        for item in self.data:
            row = ''
            if cell:
                row = cell(item)
            else:
                for td in item:
                    row += f'<td>{td}</td>'
            tr += f'<tr>{row}</tr>'
        return tr

    def render(self, title, cell):
        head = self.table_head()
        body = self.table_body(cell)

        html = f'<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"><title>{title}</title><style></style></head><body><table>{head}{body}</table></body></html>'.replace(
            '<style></style>', self.css)
        return html

    def to_html(self, path, title, cell=None):
        '''
        @path: path
        @title: html页面标题
        @return: 生成html文件
        '''
        p = path
        html = self.render(title, cell)
        with open(f'{p}.html', 'w+') as f:
            f.write(html)
