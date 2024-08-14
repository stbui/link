const config = require('./config.json');
const fs = require('fs')

const column = {
    "title": "地方志",
    "type": "difangzhi"
}

function createColunm(column) {
    const hasC = config.find(c => c.type === column.type)
    if (hasC) {
        console.log('已存在', hasC)
        return
    }

    const path = './csv/' + column.type + '.csv';
    fs.writeFileSync(path, '')


    config.push(column)

    fs.writeFileSync('./config.json', JSON.stringify(config, null, 2))

    console.log('ok', column)
}

createColunm(column)
