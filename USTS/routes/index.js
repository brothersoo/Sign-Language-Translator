var express = require('express');
var router = express.Router();
var db = require('../public/javascripts/db.js');
var auth = require('../public/javascripts/auth.js');
var config = require('../public/javascripts/config.js')

router.use(express.json());

/* GET home page. */
router.get('/', function (request, response, next) {
  var userBar = config.userBar(request, response);

  response.render('index', {userBar: userBar});
});

module.exports = router;
