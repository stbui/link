const ejs = require('ejs');
const fs = require('fs');
const config = require('./config.json');

const html = fs.readFileSync('./template/table.html', { encoding: 'utf-8' })


function toJSON(text) {
  const column = [];
  const list = text
    .split('\n')
    .filter((item) => item.length)
    .map((item) => {
      const [name, url] = item.split(',');

      if (!url) {
        column.push(name);
      }

      if (name) {
        return {
          name: name,
          url: url,
        };
      }

      return {
        name: url,
        url: url,
      };
    });

  return {
    list: list,
    column: column,
  };
}

function main(topic) {
  topic.map((t) => {
    const source = './csv/' + t.type + '.csv';
    const target = './html/' + t.type + '.html';
    const title = t.title;

    const data = fs.readFileSync(source, { encoding: 'utf-8' });
    const d = toJSON(data);

    const res = ejs.render(html, {
      title: title,
      data: d.list,
      column: d.column,
    });
    fs.writeFileSync(target, res);
    console.log('完成', title, target);
  });

  // 生成首页
  renderHome(topic);
}

function renderHome(data) {
  const target = './index.html';
  const title = '导航主页';

  const list = data.map((item) => ({
    name: item.title,
    url: './html/' + item.type + '.html',
  }));

  const res = ejs.render(html, { title: title, data: list, column: [] });
  fs.writeFileSync(target, res);
  console.log('完成', title, target);
}



main(config);
