const ejs = require('ejs')
const fs = require('fs')

const html = `
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title><%= title %></title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="keywords" content="" />
    <meta name="description" content="" />
    <style>
      *,
      ::after,
      ::before {
        box-sizing: border-box;
      }
      body,
      html {
        height: 100%;
        margin: 0;
        padding: 0;
        border: 0;
      }
      body {
        width: 100%;
        min-height: 100vh;
        vertical-align: baseline;
        word-wrap: break-word;
        color: #282a2d;
        background: #f9f9f9;
      }

      a {
        color: #282a2d;
        outline: 0 !important;
        text-decoration: none;
      }

      a:hover {
        text-decoration: none;
        color: #e94041;
      }

      .sticky {
        position: sticky;
        top: 0;
        z-index: 1080;
      }
      .overflow-hidden {
        overflow: hidden;
      }
      .mt24 {
        margin-top: 24px
      }
      .border-top {
        border-top: 1px solid #dee2e6;
      }

      .sidebar-nav {
        position: fixed;
        top: 0;
        font-size: 14px;
        width: 200px;
        height: 100vh;
        z-index: 1081;
        background: #f0f2f4;
        box-shadow: 0 0 32px 0 rgba(0,0,0,0.1);
      }
      .sidebar-logo {
        height: 74px;
        border-bottom: 1px solid #dee2e6;
        background: #fff;
        text-align: center;
        line-height: 74px;
        font-size: 22px;
      }
      .sidebar-nav ul {
        margin: 0;
        padding: 0;
      }
      .sidebar-item {
        position: relative;
        display: block;
      }
      .sidebar-item > a:hover {
        background: rgba(0, 0, 0, 0.1);
        border-radius: 5px;
        color: #e94041;
      }
      .sidebar-nav .flex-bottom a,
      .sidebar-menu-inner a {
        display: flex;
        overflow: hidden;
        padding: 8px 10px;
        margin: 1.5px 8px;
        color: #515c6b;
        font-size: 16px;
        align-items: center;
        white-space: nowrap;
        transition: all 0.3s;
      }
      .sidebar-menu ul:first-child > li > a {
        padding: 12px 10px;
      }
      .sidebar-nav-inner {
        max-width: 200px;
        display: flex;
        flex-direction: column;
        height: 100%;
      }
      .sidebar-nav-inner .flex-fill {
        overflow-y: auto;
        overflow-x: hidden;
        -webkit-overflow-scrolling: touch;
      }

      .header-nav {
        position: fixed;
        right: 0;
        left: 200px;
        background: rgb(255 255 255 / 77%);
      }

      .main-content {
        flex-direction: column;
        display: flex;
      }

      .flex-fill {
        flex: 1 1 auto;
      }

      .container {
        margin: auto;
      }
      .main-content {
        margin-left: 200px;
      }

      @media (min-width: 992px) {
      }

      @media (min-width: 1200px) {
        .container {
          max-width: 1140px;
        }
      }

      .customize-width {
        max-width: 1900px;
      }

      .flex {
        display: flex;
        flex-wrap: wrap;
      }
      .flex-item {
        flex: 0 0 20%;
        border: 1px solid transparent;
        padding: 0 12px;
        overflow: hidden;
        white-space: nowrap;
      }
      .card {
        position: relative;
        display: flex;
        flex-direction: column;
        word-wrap: break-word;
        background-color: #eee;
        margin-bottom: 12px;
      }
      .card-body {
        position: relative;
        padding: 12px;
        text-overflow: ellipsis;
        overflow: hidden;
      }
      .column {
        flex: 1 1 100%;
        padding: 0 12px;
        margin-top: 24px;
      }
      .column .card {
        border-left: 4px solid #e94041;
        background: transparent;
      }
      .column .card-body {
        padding: 0 0 0 12px;
      }
    </style>
  </head>
  <body>
    <div class="sidebar-nav sticky">
      <div class="sidebar-nav-inner">
        <div class="sidebar-logo">
          <div class="logo overflow-hidden"><%= title %></div>
        </div>
        <div class="sidebar-menu flex-fill">
          <div class="sidebar-scroll">
            <div class="sidebar-menu-inner">
              <ul>
                <% for (var i=0;i<column.length;i++)  { %>
                <li class="sidebar-item">
                  <a href="#<%= column[i] %>"><span><%= column[i] %></span></a>
                </li>
                <% } %>
              </ul>
            </div>
          </div>
        </div>
        <div class="border-top">
          <div class="flex-bottom">
            <ul>
              <li class="sidebar-item">
                <a href="#"><span>网站提交</span></a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div class="main-content flex-fill">
      <div class="container customize-width">
        <div class="header-nav"></div>
        <div class="content">
          <div class="flex">
            <% for (var i=0;i<data.length;i++)  { %>
            <div id="<%= data[i].name %>" class="<%= data[i].url?'flex-item':'column' %>"><a class="card" href="<%= data[i].url ? data[i].url : '#'+data[i].name %>" title="<%= data[i].name %>" <%= data[i].url ? 'target="_blank' : '' %>"><div class="card-body"><%= data[i].name %></div></a></div>
            <% } %>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>

`



function toJSON(text) {
  const column = [];
  const list = text.split('\n').filter(item => item.length).map(item => {
    const [name, url] = item.split(',');

    if (!url) {
      column.push(name)
    }

    return {
      name: name,
      url: url
    }
  });

  return {
    list: list,
    column: column
  }
}

function main(topic) {
  topic.map(t => {
    const source = './csv/' + t.type + '.csv';
    const target = './html/' + t.type + '.html';
    const title = t.title;


    const data = fs.readFileSync(source, { encoding: 'utf-8' });
    const d = toJSON(data);

    const res = ejs.render(html, { title: title, data: d.list, column: d.column });
    fs.writeFileSync(target, res);
    console.log('完成', title, target);
  });

  // 生成首页
  renderHome(topic);
}

function renderHome(data) {
  const target = './index.html';
  const title = '导航主页';

  const list = data.map(item => ({ name: item.title, url: './html/' + item.type + '.html' }))

  const res = ejs.render(html, { title: title, data: list, column: [] });
  fs.writeFileSync(target, res);
  console.log('完成', title, target);
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
  },
  {
    title: "院校导航",
    type: 'school',
  },
  {
    title: "电商美工",
    type: 'meigong',
  },
  {
    title: "电商运营",
    type: 'coonav',
  },
  {
    title: "生活娱乐",
    type: 'shenghuo',
  },
  {
    title: "新媒体",
    type: 'xinmeiti',
  },
  {
    title: "coonav",
    type: 'coonav',
  },
  {
    title: "dyqu",
    type: 'dyqu',
  },
  {
    title: "law",
    type: 'law',
  },
  {
    title: "science",
    type: 'science',
  },
  {
    title: "shenghuo",
    type: 'shenghuo',
  },
  {
    title: "study",
    type: 'study',
  },
  {
    title: "xxx",
    type: 'xxx',
  }
]

main(topic);
