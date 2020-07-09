var passport = require('passport')
  , LocalStrategy = require('passport-local').Strategy;
var db = require('./db.js');
var bcrypt = require('bcrypt');

module.exports = function(app) {
  app.use(passport.initialize());
  app.use(passport.session());

  passport.serializeUser(function(user, done){
    console.log('session data stored!', user);
    done(null, user);
  })
  
  passport.deserializeUser(function(user, done){
    console.log('session data read!', user);
    done(null, user);
  })
  
  //configuring my local strategy
  passport.use(new LocalStrategy({
    usernameField: 'userName',
    passwordField: 'password',
    passReqToCallback: true
  }, function(request, userName, password, done){
    console.log('passport configuration');
    db.query('SELECT * FROM user WHERE userName=?', [userName], function(error, result){
      if(error){
        console.log('error: ' + error);
        return done(false, null);
      } else {
        if(result.length === 0){
          console.log('not existing username');
          return done(false, null);
        } else {
          if(!bcrypt.compareSync(password, result[0].password)){
            console.log('password incorrect!');
            return done(false, null);
          } else {
            console.log('login success!');
            return done(null, {
              userID: result[0].userID,
              userName: result[0].userName
              //send data for session to method ' serializeUser''s callback function
            })
          }
        }
      }
    })
  }))
}
