const express = require('express');
const router = express.Router();

const images = [
    { src: "http://localhost:8940/Image_1700622386433.jpg", alt: '图片1', description: '图片1说明：这是第一张图片的说明文字。' , id:1},
    { src: 'http://localhost:8940/图片1.jpg', alt: '图片2', description: '图片2说明：这是第二张图片的说明文字。' , id:2},
    { src: 'image3.jpg', alt: '图片3', description: '图片2说明：这是第二张图片的说明文字。' , id:3},
    // 更多图片数据...
]

router.get('/index', (req, res) => {

    res.render('index', { images });
})



module.exports = router