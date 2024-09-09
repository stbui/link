const { readFile, utils } = require('xlsx');
const path = require('path');
const fs = require('fs');
const ejs = require('ejs');

const config = {
  sh_yqqy: '上海市-园区企业-20240830',
};

Object.keys(config).map((field) => {
  const title = config[field];
  const inputfile = path.join(process.cwd(), `./xlsx/${field}.xlsx`);

  const wb = readFile(inputfile);
  const ws = wb.Sheets[wb.SheetNames[0]];
  const aoa = utils.sheet_to_json(ws, {
    header: 1,
    raw: true,
  });

  const templateFile = path.join(process.cwd(), './template/xlsx.html');
  const html = ejs.compile(
    fs.readFileSync(templateFile, { encoding: 'utf-8' }),
  );

  const content = html({
    title: title,
    data: aoa,
    column: aoa[0],
  });

  const outFile = path.join(process.cwd(), `./html/${field}.html`);
  fs.writeFileSync(outFile, content);
  console.log('完成', title, outFile);
});
