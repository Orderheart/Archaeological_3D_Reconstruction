// 这是服务器主页

// 导入服务器
const express = require('express');
// 导入跨域资源共享
const cors = require('cors');
const path = require('path')

// 注册服务器实例
const app = express();
// 导入数据库
const db = require('./db/index.js');
const { addAbortListener } = require('events');

// 解决跨域问题
app.use(cors());
// 解析数据中间件
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.set('view engine', 'ejs')
// 托管静态资源
app.use(express.static('public'));

//在路由前挂载res.cc
app.use((req, res, next) => {
  res.cc = function(err, status = 1){
      res.send({
          status,
          message: err instanceof Error ? err.message : err
      })
  }
  next();
})

// 主页
app.get('/index',(req, res) => {
  res.sendFile(path.join(__dirname, './public/html/index.html')  );
})

// 查询数据
app.get('/ask-data',(req, res) => {
  const sql = 'select * from new_table';

  db.query(sql, (err, results) => {
      if(err)
      {
          return res.send({status:1 , message: err.message});
      }

      res.send(JSON.stringify(results));

  });

})

// 上传ply文件
app.post('/upload-ply', async (req, res) => {
      if(!req.files) {
          res.send({
              status: false,
              message: 'No file uploaded'
          });
      } else {
          let ply = req.files.ply;
          
          avatar.mv('./public/model/' + ply.name);

          const sql = `select * from pos`;
          db.query(sql, (err, results) => {
              if(err)
              {
                  return res.send({status:1 , message: err.message});
              }

              var id = results.length + 1;
              const sql = 'insert into pos set ?';
              db.query(sql, {id: id, position: ply.name}, (err, results) => {

                  if(err)
                  {
                      return res.send({status:1 , message: err.message});
                  }

                  res.send({
                      status: true,
                      message: 'File is uploaded',
                      data: {
                          name: ply.name,
                          mimetype: ply.mimetype,
                          size: ply.size
                      }
                  });
              });

          });
      }
});

// 上传描述信息
app.post('/upload-msg', async (req, res) => {
  if(!req.files) {
    res.send({
        status: false,
        message: 'No file uploaded'
    });
} else {
  let msg = req.body;
  let avatar = req.files.avatar;
  const sql  = `select * from pos where pos=?`;
  db.query(sql, [msg.name], (err, results) => {
      if(err)
      {
          return res.send({status:1 , message: err.message});
      }
      if(results.length !== 1){
          return res.send({status:1 , message: '文件不存在'});
      }

      avatar.mv('./public/choose/images/' + avatar.name);

      const sql = 'insert into new_table set ?';
      db.query(sql, {index: results.id ,name: msg.name, imageSrc: 'images/' + avatar.name, role: msg.role, description: msg.description}, (err, results) => {

          if(err)
          {
              return res.send({status:1 , message: err.message});
          }

          res.send({
              status: true,
              message: 'File is uploaded',
              data: {
                  name: msg.name,
                  role: msg.role,
                  description: msg.description
              }
          });
      });


  })
  


}

});

// 获取对应的位置
app.get('/get-pos', (req, res) => {
  const sql = `select * from pos where id=?`;
  
  db.query(sql, [req.query.id], (err, results) => {
      if(err)
      {
          return res.send({status:1 , message: err.message});
      }

      res.send(JSON.stringify(results));
  });

});


// 错误级别中间件
app.use((err, req, res, next) => {

  // token验证失败的错误
  if(err.name === 'UnauthorizedError') return res.cc('UnauthorizedError');
   
  // 未知错误
  res.cc(err);
})


// 监听端口
app.listen(8940, () => {
    console.log('server is running');
})