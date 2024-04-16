#!/usr/bin/node

class Rectangle{
    constructor(w,h){
      if(w > 0 && h > 0){
      this.width = w;
      this.height = h;
      }
    }
    print(){
      let i,j;
      let line = ''
      for(i = 0; i < this.height; i++){
        line += '\n'
        for(j = 0;j < this.width; j++){
            line += 'X'
        }
      }
      console.log(line.slice(1));
    }
  }

module.exports = Rectangle;
