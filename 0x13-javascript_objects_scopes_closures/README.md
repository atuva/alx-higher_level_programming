## 0x13-javascript_objects_scopes_closures
Learning about Javascript

### 0-rectangle.js
An empty class `Rectangle` that defines a rectangle

### 1-rectangle.js
A class `Rectangle` that defines a rectangle
* The constructor takes 2 arguments `w` and `h`

### 2-rectangle.js
A class `Rectangle` that defines a rectangle
* The constructor takes 2 arguments `w` and `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object

### 3-rectangle.js
A class `Rectangle` that defines a rectangle
* The constructor takes 2 arguments `w` and `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object
* Contains an instance method `print()` that prints the rectangle using `X`

### 4-rectangle.js
A class `Rectangle` that defines a rectangle
* The constructor takes 2 arguments `w` and `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object
* Contains an instance method `print()` that prints the rectangle using `X`
* Contains an instance method `rotate()` that exchanges the `width` and the `height` of the rectangle
* Contains an instance method `double()` that multiplies the `width` and the `height` of the rectangle by 2

### 5-square.js
A class `Square` that defines a square and inherits form `Rectangle` of `4-rectangle.js`
* Constructor must take 1 argument: `size`
* The constructor of `Rectangle` must be called using `super()`

### 6-square.js
A class `Square` that defines a square and inherits form `Square` of `5-square.js`
* Contains an instance method `charPrint(c)` that prints the rectangle using character `c`
  * If `c` is `undefined` use the character `X`

### 7-occurrences.js
A function that returns the number of occurrences in a list:
* Prototype: `exports.nbOccurences = function (list, searchElement)`

### 8-esrever.js
A function that returns the reversed version of a list:
* Prototype: `exports.esrever = function (list)`

### 9-logme.js
A function that prints the number of arguments already printed and the new argument value.
* Prototype: `exports.logMe = function (item)`
* Output format: `<number arguments already printed>: <current argument value>`

### 10-converter.js
A function that converts a number from base 10 to another base passed as argument:
* Prototype: `exports.converter = function (base)`
* You are not allowed to import any file
* You are not allowed to declare any new variable (`var`, `let`, etc..)
