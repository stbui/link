import fs from 'fs';
import * as cheerio from 'cheerio';

const file = './csv/hunan.csv';

const text = fs.readFileSync(file, { encoding: 'utf-8' });
let rows = text.split('\n').filter((item) => item !== '');

const titlePromise = (url) =>
  fetch(url)
    .then((res) => res.text())
    .then((res) => {
      const $ = cheerio.load(res);
      const txt = $('title')
        .text()
        .replace(/(^\s*)|(\s*$)/g, '');
      console.log(txt);
      return txt;
    });

const promises = rows.map(async (row) => {
  const [title, url, t2] = row.split(',');
  if (url && url !== '#') {
    try {
      const title2 = await titlePromise(url);
      return [title, url, title2];
    } catch (e) {
      return [title, url];
    }
  }
  return [title, url];
});

let rest = await Promise.all(promises);
rest = rest.map((a) => a.join(',')).join('\n');
fs.writeFileSync(file, rest);
console.log(rest);
