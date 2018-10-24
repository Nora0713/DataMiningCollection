var express = require('express');
var bodyParser = require('body-parser');

var router = express.Router();

var jsonParser = bodyParser.json()

var aim="http://118.89.234.98:9200/insur/heal/_search?q=company:";

// 创建 application/x-www-form-urlencoded 解析
var urlencodedParser = bodyParser.urlencoded({ extended: false })

/* GET users listing. */
router.post('/', function(req, res, next) {
	var tmp=req.body.company;
	aim=aim+tmp;
	aim=encodeURI(aim);
	var superagent=require('superagent');
	superagent
	.post(aim)
	.end(function(err,response){
		if(err||!response.ok){
			res.send(err.message);
		}else{
			res.send(response.body);
		}
	})
  });

module.exports = router;
