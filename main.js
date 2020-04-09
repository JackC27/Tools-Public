//Recursion allows js to return a function

const temp = () => {
  let ind = 0;
  let arr = [0, 2, 4, 5, 9];
  return () => { 
    let result = arr[ind];
    ind++;
    return result;
  }
}

let a = temp();
console.log(a());
console.log(a());
console.log(a());
console.log(a());
console.log(a());
console.log(a());

//END Recursion

