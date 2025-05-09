var varSize = "Hello World!";
console.log(varSize.length);
function getLength(obj) {
    var len = obj.length;
    var type = typeof obj;
    console.log("Type: ".concat(type, " - Length: ").concat(len));
    return obj.length;
}
console.log(getLength(varSize));
console.log(getLength([1, 2, 3, 4, 5]));
