const ejs = require('ejs');
const fs = require('fs');

const html = fs.readFileSync('./template/atable.html', { encoding: 'utf-8' });

const data = require('../json/dqbg.json');

const config = { key: 'dqbg', title: '上市公司-定期报告', data };

const res = ejs.render(html, {
  data: config.data,
  title: config.title,
  cellWidth: '',
  cellFixed: 1
});

fs.writeFileSync(`./html/${config.key}.html`, res);
