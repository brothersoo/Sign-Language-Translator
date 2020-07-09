var express = require('express');
var router = express.Router();
var passport = require('passport'), LocalStrategy = require('passport-local').Strategy;;
var db = require('../public/javascripts/db.js');
var bcrypt = require('bcrypt');
var sanitizeHtml = require('sanitize-html');
var auth = require('../public/javascripts/auth.js')

var saltRounds = 10;

router.get('/signup', function(request, response){
  response.render('signup');
})

router.post('/signup_process', function(request, response){
  var userName = sanitizeHtml(request.body.userName);
  var password = sanitizeHtml(request.body.password);

  bcrypt.hash(password, saltRounds, function(error, hash){
    if(error){
      throw error;
    }

    userID = auth.getUUID()

    db.query('INSERT INTO user(userID, userName, password) VALUES(?,?,?)', [userID, userName, hash], function(error2, result){
      if(error2){
        throw error2;
      }
      response.redirect('/');
    })
  })
})

router.get('/login', function(request, response){
  console.log('log in page');
  response.render('login');
})

router.post('/login_process', passport.authenticate('local', {failureRedirect: '/auth/login', failureFlash: true}), function(request, response){
  console.log('If this function gets called, authentication was successful.')
  response.redirect('/');
})

router.get('/logout', function(request, response){
  request.logout();
  response.redirect('/');
})

module.exports = router;