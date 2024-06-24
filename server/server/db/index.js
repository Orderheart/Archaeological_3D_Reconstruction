// 导入mysql模块
const mysql = require('mysql');

// 创建数据库连接对象
const db = mysql.createPool({
    host: '',
    user:'',
    password:'',
    database:''
})

module.exports = db
