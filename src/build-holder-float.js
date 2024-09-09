const ejs = require('ejs');
const fs = require('fs');

const html = fs.readFileSync('./template/xlsx.html', { encoding: 'utf-8' });

let config = { key: 'holder_float', title: '300十大流通股东-2024中报' };

const data = require(`../json/${config.key}.json`);
config.data = data;

const res = ejs.render(html, {
  data: config.data,
  title: config.title,
  column: [],
  cellWidth: '100px',
});

fs.writeFileSync(`./html/${config.key}.html`, res);
