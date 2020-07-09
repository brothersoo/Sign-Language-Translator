var sanitizeHtml = require('sanitize-html');
var uuid4 = require('uuid4')

module.exports = {
  isLoggedin: function(request, response){
    if(request.user){
      return true;
    } else {
      return false;
    }
  },
  getUUID: function(request, response){
    const tokens = uuid4().split('-')
    return tokens[2]+tokens[1]+tokens[0]+tokens[3]+tokens[4]  
  }
}