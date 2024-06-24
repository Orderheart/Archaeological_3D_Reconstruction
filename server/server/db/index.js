// 导入mysql模块
const mysql = require('mysql');

// 创建数据库连接对象
const db = mysql.createPool({
    host: '8.137.125.44',
    user:'root',
    password:'Zw110404.',
    database:'db_show'
})

module.exports = db