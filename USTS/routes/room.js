var express = require('express');
var router = express.Router();
var passport = require('passport'), LocalStrategy = require('passport-local').Strategy;;
var db = require('../public/javascripts/db.js');
var bcrypt = require('bcrypt');
var sanitizeHtml = require('sanitize-html');
var auth = require('../public/javascripts/auth.js')

var saltRounds = 10;

router.get('/room_create', function(request, response){
  response.render('room_create');
})

router.post('/room_create_process', function(request, response){
  var roomName = sanitizeHtml(request.body.userName);
  var password = sanitizeHtml(request.body.password);

  bcrypt.hash(password, saltRounds, function(error, hash){
    if(error){
      throw error;
    }

    roomID = auth.getUUID()

    db.query('INSERT INTO room(roomID, roomName, participantAmount, password) VALUES(?,?,1,?)', [roomID, roomName, hash], function(error2, result){
      if(error2){
        throw error2;
      }
      response.redirect('/'+roomID);
    })
  })
})

router.get('/chat/:id', function(request, response){
  roomID = sanitizeHtml(request.params.id)

  db.query('SELECT * FROM room WHERE roomID=?', [roomID], function(error, result){
    if(error){
      throw error
    }
    if(result===null){
      print('no such room!')
      response.redirect('/')
    }
    
    response.render('room', {title:result.roomName})
  })
})

router.get('/room_search', function(request, response){
  response.render('room_search')
})

router.get('/room_search_process', function(request, response){
  roomName = sanitizeHtml(request.body.roomName)
  password = sanitizeHtml(request.body.password)

  db.query('SELECT * FROM room WHERE roomID=?', [room])
})

module.exports = router;