#!/usr/bin/node

class Rectangle{
  constructor(w,h){
    if(w > 0 && h > 0){
    this.width = w;
    this.height = h;
    }
  }
  print(){
    for(i = 0; i < h; i++){
      for(j = 0;j < w; j++){
          console.log('X');
      }
    }
  }
}
module.exports = Rectangle;
