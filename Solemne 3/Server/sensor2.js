var net = require("net");

var server = net.createServer(function(socket){
    function generate(){
        limite=0;
        var r = Math.random()*100;
        r=r.toFixed(1);
        limite=limite+1;
        console.log("sensor 2: %s",r);
        socket.write(r.toString());
        if(limite = 200){
            setTimeout(generate,500);
        }
    return r;
    }
    generate();
});
server.listen(5000,"192.168.18.3");