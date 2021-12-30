const dgram       = require('dgram')
const enchufe_udp = dgram.createSocket('udp4')
const net         = require('net')
const xmlrpc      = require('xmlrpc')
const mongoose    = require('mongoose')
const http        = require('http')
const fs          = require('fs')
const path        = require('path')
const express     = require('express')
const app         = express()

// server web//////////////////////////////////////////////////////////////////////////////////////////////////////

//Configuracion server
app.set('port',1000);


//Archivos estaticos
app.use(express.static(path.join(__dirname,'public')))


// inciar server
const server = app.listen(app.get('port'), ()=> {
    console.log("servidor en el puerto", app.get('port'));
});


//Crear socket.io
const socketIO = require('socket.io')
const io       = socketIO(server)

// websockets
io.on('connection',(socket) =>{
    console.log('new connection', socket.id);
});

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//conexion mongodb

mongoose.connect ('mongodb://localhost/solenme3', function (err) {
    if (!err) {
        console.log ('Se ha conectado a mongo')
    }
    else {
        throw err
    }
});

Sensor = new mongoose.Schema({
    medida: Number
}, { collection: 'Sensor' })

Sensor = mongoose.model('prueba1', Sensor)

Sensor1 = new mongoose.Schema({
    medida: Number
}, { collection: 'Sensor1' })

Sensor1 = mongoose.model('prueba2', Sensor1)

Sensorx = new mongoose.Schema({
    medida: Number
}, { collection: 'Sensorx' })

Sensorx = mongoose.model('prueba3', Sensorx)

//recibir udp/////////////////////////////////////////////////////////////////////////////////////////////////
enchufe_udp.on('message',function(msg,info){
    var data_u=msg.toString('utf-8');
    console.log("Sensor UDP:"+ data_u);

        io.emit('canal1',data_u);

    /// se añade a mongodb////
    Sensor.collection.insert({medida:data_u}, function(err,response){
        if(err) throw err;
    });
});

enchufe_udp.bind(2000,"192.168.18.3")

//recibir tcp//////////////////////////////////////////////////////////////////////////////////////////////////

var enchufe_tcp = new net.Socket();
enchufe_tcp.connect(5000, "192.168.18.3");
enchufe_tcp.on('data',function(data){
    datat = data.toString();
    console.log('Sensor TCP:' + datat);

    io.emit('canal2',datat);

    Sensor1.collection.insert({medida:datat},function(err,response){
        if(err)throw err;
  });


        data1=parseInt(datat);
        setTimeout(function(){
            var cliente = xmlrpc.createClient({host:'192.168.18.3',port:9000, path:'/'})
            cliente.methodCall('agregar',[data1],function(error, value){
                console.log('respuesta RPC:' + value);
            })
        },1000);

        io.emit('canal3',data1);

        Sensorx.collection.insert({medida:data1},function(err,response){
            if(err)throw err;
        });
});