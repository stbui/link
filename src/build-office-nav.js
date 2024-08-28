const ejs = require('ejs');
const fs = require('fs');

const html = fs.readFileSync('./template/atable.html', { encoding: 'utf-8' });

const data = require('../json/office-nav.json');

const config = { key: 'office-nav', title: '全国政府部门站群', data };

const res = ejs.render(html, {
  data: config.data,
  title: config.title,
  cellWidth: 'w-200',
  cellFixed: 0
});

fs.writeFileSync(`./html/${config.key}.html`, res);
