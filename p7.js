
const {EventEmitter} = require('events');
  
const Emitter = new EventEmitter();
 
Emitter.on('Message logged', function() {
   console.log("Listner called");
});
Emitter.emit('myEvent', "First event");


// cheack Double bcoz it not show the result on Terminal
