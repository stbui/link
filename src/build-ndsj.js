const ejs = require('ejs');
const fs = require('fs');

const html = fs.readFileSync('./template/atable.html', { encoding: 'utf-8' });

const data = require('../json/ndsj.json');

const config = { key: 'ndsj', title: '全国统计年鉴', data };

const res = ejs.render(html, {
  data: config.data,
  title: config.title,
  cellWidth: '',
  cellFixed: 0
});

fs.writeFileSync(`./html/${config.key}.html`, res);
console.log(config);
