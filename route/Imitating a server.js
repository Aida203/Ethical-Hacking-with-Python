const http = require('http')  

http.createServer((req , res)=>{
    // localhost:3000 
    if(req.url === '/'){
        // set success status code ==> 200 ok
        //res.writeHead(200 , {'Content-Type' : 'text/html'})
        res.statusCode = 200;
        // set response content
        res.write(`<html><body> 
                <h1>Hello and Welcome to my website</h1>
            </body></html>`)
        res.end();
    }
    // localhost:3000/about
    else if(req.url=== '/about'){
        res.writeHead(200 , {'Content-Type' : 'text/html'})
        // set response content
        res.write(`<html><body> 
                <h1>Welcome From About Page</h1>
            </body></html>`)
        res.end();
    }else{
        res.write("<div style='background-color : orange; color: #2d2d2d; padding:12px'> Sorry .. Error 404 Page Not Found</div>")
        res.end()
    }
}).listen(3000 , ()=> console.log("Server Running .... "));