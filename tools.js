const config = require('./config.json');
const fs = require('fs')

const column = {
    "title": "孕婴童导航",
    "type": "yyt"
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
