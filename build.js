const ejs = require('ejs')
const fs = require('fs')

const html = `
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title><%= title %></title>
        <style>
            * {
                margin: 0;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                border: solid #ccc 1px;
            }

            table td, table, th {
                border-left: 1px solid #ccc;
                border-top: 1px solid #ccc;
                padding: 4px 8px;
                white-space: nowrap;
            }

            table tr:hover {
                background: #eee;
            }

            table tr:nth-child(odd) {
                background-color: #f3f3f3;
            }

            a {
                color: #000;
                text-decoration: none;
            }
            a:hover {
                color: #05a687;
            }
            .text-center {
                text-align: center;
            }
            .center {
                margin: 0 auto;
                width: 1440px;
            }
            .title {
                font-size: 18px;
                padding: 24px 0 12px;
            }
            .flex {
                display: flex;
                flex-wrap: wrap;
            }
            .flex-item {
                width: 202px;
                background-color: #f3f3f3;
                border: 1px solid transparent;
                padding: 12px;
                margin: 6px;
            }
            .flex-item:hover { 
                border: 1px solid #05a687;
                color: #05a687;
            }
            .flex-fill {
                width: 100%;
                max-width: 100%;
                min-width: 100%;
                background: transparent;
                padding: 0 0 0 12px;
                margin-top: 24px;
                border: 0;
                border-left: 4px solid #05a687;
            }
            .flex-fill:hover {
                border: 0;
                border-left: 4px solid #05a687;
            }
        </style>
    </head>
    <body>
        <div class="title text-center"><%= title %></div>
        <div class="center">
            <div class="flex">
            <% for (var i=0;i<data.length;i++)  { %>
                <div class="flex-item <%= data[i].url?'':'flex-fill' %>"><a href="<%= data[i].url %>" target="_blank"><%= data[i].name %></a></div>
            <% } %>
            </div>
        </div>
    </body>
</html>
`




function toJSON(text) {
    return text.split('\n').filter(item => item.length).map(item => {
        const s = item.split(',')
        return {
            name: s[0],
            url: s[1]
        }
    })
}

function main(topic) {
    topic.map(t => {
        const source = './csv/' + t.type + '.csv';
        const target = './html/' + t.type + '.html';
        const title = t.title;

        const data = fs.readFileSync(source, { encoding: 'utf-8' })
        const res = ejs.render(html, { title: title, data: toJSON(data) });
        fs.writeFileSync(target, res)
        console.log('完成', title, target)
    })
}

const topic = [
    {
        title: "股市财经",
        type: 'broker',
    },
    {
        title: "电视直播",
        type: 'iptv',
    },
    {
        title: "政府网站",
        type: 'office',
    }
]

main(topic)