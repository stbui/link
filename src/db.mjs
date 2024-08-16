import sqllite from 'sqlite3';

function createTable(db) {}

function insert(db, data) {
  //   const field = {
  //     title1: '1',
  //     link: '1',
  //     method: '1',
  //   };

  const fields = Object.keys(data);
  const feldsText = data.join(',');
  const valuesText = fields.map(() => '?').join(',');

  const values = fields.map((f) => data[f]);

  const sql = `INSERT INTO link(${feldsText}) VALUES(${valuesText})`;

  db.run(sql, values, (err) => {
    if (err) {
      return console.log('insert data error: ', err.message);
    }
    console.log('insert data: ', this);
  });
}

const db = new sqllite.Database('./link.db', function (err) {
  if (err) {
    return console.log(err.message);
  }
  console.log('connect database successfully');
});

db.run(
  'INSERT INTO link(title,link,method) VALUES(?,?,?)',
  ['1', '3', '3'],
  function (err) {
    if (err) {
      return console.log('insert data error: ', err.message);
    }
    console.log('insert data: ', this);
  },
);
