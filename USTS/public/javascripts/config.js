var sanitizeHtml = require('sanitize-html');
var auth = require('./auth.js');
var db = require('./db.js');

module.exports = {
  userBar: function(request, response){
    if(!auth.isLoggedin(request, response)){
      return `<a href='/auth/signup'>sign up </a> |  <a href='/auth/login'>log in</a>`
    } else {
      var userName = sanitizeHtml(request.user.userName);
      return `${userName} | <a href='/users/myinfo'> my info</a> | <a href='/auth/logout'>logout</a>`
    }
  }
}