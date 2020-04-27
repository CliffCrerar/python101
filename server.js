const 
    express = require('express'),
    path = require('path'),
    app = express();

app.use('/',express.static(path.join(__dirname)));
// app.use('/brython',express.static(brython));
// app.use('/brython_stdlib',express.static(brythonStd));
// app.use('/index',express.static(path.join(__dirname,'./index.py')));

// app.get('/',(req,res)=>fs.createReadStream('./index.html').pipe(res.status(200)));

app.listen(3000,startApp);

function startApp(){
    console.log('Python Web App Started');
}

