//==============================================================================
// app.js
//==============================================================================
var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var bodyParser = require('body-parser');
var app = express(); //*********
app.set('views', path.join(__dirname, 'views'));
// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

//==============================================================================

              /*application gets/posts - ajax call responses.*/

//==============================================================================
app.get('/', function(req, res){
  console.log(__dirname);
  res.send(200, __dirname + '/public/index.html');
});
//==============================================================================
app.get('/index', function(req, res){
  res.send(200, __dirname + '/public/index.html');
});
//==============================================================================

/*
// TODO scrape stock data using python. 
var PythonShell = require('python-shell');

PythonShell.run('my_script.py', function (err) {
  if (err) throw err;
  console.log('finished');
});

*/






//=============================================================================
//                          error handlers
// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
  app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
      message: err.message,
      error: err
    });
  });
}
//=============================================================================
// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.render('error', {
    message: err.message,
    error: {}
  });
});
//=============================================================================
module.exports = app;
//=============================================================================
