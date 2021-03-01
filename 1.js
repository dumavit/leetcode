const { eventNames } = require("process");

class EventEmitter {
    constructor() {

        this.eventCallbacks = {};
    }

    on = (eventName, callback) => {
        if (eventName in this.eventCallbacks) {
            this.eventCallbacks[eventName].push(callback);
        } else {
          this.eventCallbacks[eventName] = [callback];
        }

        return () => this.eventCallbacks[eventName] = this.eventCallbacks[eventName].filter(cb => cb !== callback);
    }

    emit = (eventName) => {
        if (eventName in this.eventCallbacks) {
            this.eventCallbacks[eventName].forEach(cb => cb());
        }
    }   

    // unsubscribe = (eventName, callback) => {
    //   const callbacks = this.eventCallbacks[eventName];
    //   if (callbacks) {
    //     this.eventCallbacks[eventName] = this.eventCallbacks[eventName].filter(cb => cb !==callback);
    //   }
    // }
}


const eventEmitter = new EventEmitter();



// eventEmitter.on('meow', () => console.log('cat says meow'));
const unsubscribeFromBark1 = eventEmitter.on('bark', () => console.log('bark bark'));
eventEmitter.on('bark', () => console.log('other dog barks'));


eventEmitter.emit('bark');
// eventEmitter.unsubscribe('bark', bark1);
unsubscribeFromBark1();
eventEmitter.emit('bark');








