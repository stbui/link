const ejs = require('ejs');
const fs = require('fs');
const path = require('path');
const csv = require('csv');

const config = {
  school_crgd: '全国成人高等学校名单（截至2024年6月20日）',
  school_ptgd: '全国普通高等学校名单（截至2024年6月20日）',
  sh_cyw: '上海市-产业园区-20240830',
  sh_yqqy: '上海市-园区企业-20240830',
};

Object.keys(config).map((field) => {
  const title = config[field];
  const inputfile = path.join(process.cwd(), `./xlsx/${field}.csv`);

  fs.createReadStream(inputfile).pipe(
    csv.parse({ skip_empty_lines: true }, (err, data) => {
      if (err) {
        return console.log('error', field, err.message);
      }

      const templateFile = path.join(process.cwd(), './template/xlsx.html');
      const html = ejs.compile(
        fs.readFileSync(templateFile, { encoding: 'utf-8' }),
      );
      const content = html({
        title: title,
        data: data,
        column: data[0],
      });

      const outFile = path.join(process.cwd(), `./html/${field}.html`);
      fs.writeFileSync(outFile, content);
      console.log('完成', title, outFile);
    }),
  );
});
