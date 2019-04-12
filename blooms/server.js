var express = require("express");
var app = express();
var router = express.Router();
var path = __dirname + '/views/';
var PythonShell = require('python-shell');
var http =require('http');
var bodyParser = require('body-parser')
var fileUpload = require('express-fileupload');

app.use(fileUpload());
// support parsing of application/json type post data
app.use(bodyParser.json());

//support parsing of application/x-www-form-urlencoded post data
app.use(bodyParser.urlencoded({ extended: true }));

router.use(function (req,res,next) {
  next();
});

router.get("/",function(req,res){
  res.sendFile(path + "index.html");
});

router.post("/submit", function(req,res){
  if (!req.files)
    return res.status(400).send('No files were uploaded.');

  // The name of the input field (i.e. "sampleFile") is used to retrieve the uploaded file
  let sampleFile = req.files.sampleFile;

  // Use the mv() method to place the file somewhere on your server
  sampleFile.mv('./math.txt', function(err) {
    if (err)
      return res.status(500).send(err);

  //  res.send('File uploaded!');
    var options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
      };

    PythonShell.run('/my_script.py',options, function
    (err, results) {
        if (err) throw err;
      // results is an array consisting of messages collected during execution
      res.sendFile(path + 'results.html');
    });
  });
});


router.get("/about",function(req,res){
  res.sendFile(path + "about.html");
});

router.get("/contact",function(req,res){
  res.sendFile(path + "contact.html");
});

app.use("/",router);

app.use("*",function(req,res){
  res.sendFile(path + "404.html");
});

app.listen(3000,function(){
  console.log("Live at Port 3000");
});

app.post('/submit', function(req, res) {
  res.send(200);
});
