var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var cookieSession = require('cookie-session');
var flash = require('connect-flash');

var indexRouter = require('./routes/index');
var authRouter = require('./routes/auth');
var roomRouter = require('./routes/room');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use(cookieSession({
  keys: ['keyboard cat'],
  cookie: {
    maxAge: 1000*60*60 //cookie valid time(1h)
  }
}));

app.use(flash());

require('./public/javascripts/passport.js')(app);

app.use('/', indexRouter);
app.use('/auth', authRouter);
app.use('/room', roomRouter)

/*** SOCKET.IO ***/
app.io = require('socket.io')()

app.io.on('connection', function(socket){
  console.log("user connected")
  socket.broadcast.emit("hi")

  socket.on("disconnect", function(){
  console.log("user disconnected")
  })

  socket.on("chat message", function(msg){
    console.log('message: ' + msg)
    app.io.emit("chat message", msg)
  })
})

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
