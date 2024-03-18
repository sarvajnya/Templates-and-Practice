"use strict";
//a = prompt('Enter here');
console.log("Jai Shree Ram");

//console.log(Math.sin(0));
//console.log(window, this);
function add(a, b) {
  console.log(a + b);
}
/*
function name(param1, param2, ...) {
}
/*
// const private = 100;
// console.log(private);
/*console.log('Done');
add(20, 30);
var a = String(10e90);
console.log(typeof a, a);
*/
let a = 10,
  b = 20;
//const ans = (a,b) => a+b ;

// if(a>b) {
//     console.log(a);
// } else {
//     console.log(b);
// }
const ans1 = a >= b ? a : b;
// console.log(`The larger value is ${ans1}`);
// console.log(ans);
const ans2 = (a, b) => {
  const ans = a * b;
  return ans;
};

const ans3 = function (a, b) {
  return a * b;
};
// console.log(ans2(a, b), ans3(a,b));
/*
let -> block scoped
var -> function scoped
use let always
*/
// console.log(another);
// var another;

// //switch-case
// const day = 5;
// switch(day)
// {
//     case 1:
//         console.log('Mon');
//         break;
//     case 2:
//         console.log('Tue');
//         break;
//     case 3:
//         case 4:
//         console.log('hurray!');
//         break;
//     default: console.log('None');
// }

//Objects
const obj1 = {
  firstName: "Sar",
};

const obj2 = {
  firstName: "Sar",
};
function dem(a, b) {
  console.log(this);
}

dem(10, 102);
// console.log(obj1['firstName'], obj2.firstName);

const arr = [1, "e", 3, 0.8];
// console.log(JSON.stringify(arr));

// //scope chain
// let temp1 = 100;
// function temp2() {
//     function temp3() {
//         temp1 = 200;
//     }
//     temp3();
//     console.log(temp1);
//     temp1 = 300;
// }
// //temp3(); -> Error
// temp2()

// console.log(temp1);

const objj = {
  age: 100,
  temp: function temp1() {
    console.log(this.age);
  },
};
objj.temp();

/*Arrow fn does not get 'this' and 'arguments', access from parent scope
'this' inside an object works for 1st method only
for nested method, this = undefined

*/

//To copy objects new = Object.assign({}, old);

//to custom sort
const fun1 = (x) => x[1]; //callback fun
console.log("Grand Theft Auto: Vice City Stories");
console.log(
  [
    [134, 12],
    [33243420, -1],
  ].sort((a, b) => fun1(a) - fun1(b))
);

console.log("done bhai");
