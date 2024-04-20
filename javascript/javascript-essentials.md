# JavaScript Essentials

1. Destructuring Arrays and Objects
```js
var [a, b] = [1, 2, 3];
console.log(a, b); // 1 2

var [a, b, c] = [1, 2];
console.log(a, b, c); // 1 2 undefined

var item = {
    key1: "A",
    key2: "B",
    key3: "C",
};
var {key2, key1, key4} = item;
console.log(key1, key2, key4); // A B undefined
```

2. Rest/Spread Operator
```js
var [a, b, ...c] = [1, 2, 3, 4, 5];
console.log(a, b, c); // 1 2 [3, 4, 5]

var my_list = [...[1, 2, 3], 4, 5];
console.log(my_list); // [1, 2, 3, 4, 5]

var item = {
    key1: "A",
    key2: "B",
};
var updated = {...item, key3: "C", key2: "changed"};
console.log(updated); // {key1: 'A', key2: 'changed', key3: 'C'}
```

3. Template Literals
```js
var item = {
    name: "John",
    age: 30,
};
console.log(`${item.name} is ${item.age} years old, he is ${item.age > 18 ? "adult" : "menor"}.`);
// John is 30 years old, he is adult.
```

4. Arrow Functions
```js
function getYearFunction(str) {
    return str.split("-")[0];
}
console.log(getYearFunction("2024-01-15")); // 2024

const getYearExpression = (str) => str.split("-")[0];
console.log(getYearExpression("2024-01-15")); // 2024
```

5. Short-Circuiting
```js
/*
 * Falsy - 0, '', null, undefined
 * Truthy - everything else
 */

/* And (returns first falsy or last truthy) */
console.log(true && "Some string"); // Some string
console.log(false && "Some string"); // false

var isTrue = true;
console.log(isTrue && "Some string"); // Some string
console.log(true && true && 'Hello'); // Hello
console.log(true && null && 'Hello'); // null

console.log("string 1" && "string 2"); // string 2
console.log(0 && "Some string"); // Some string

/* Or (returns first truthy or last falsy) */
console.log(true || "Some string"); // true
console.log(false || "Some string"); // Some string

var item = {};
console.log(item.undedinesProperty || "Property doesn't exist"); // Property doesn't exist

/*
 * Nullish coalescing operator (??)
 * null or undefined - returns the second value.
 * 0 or '' - first value is returned.
 */
var count = 0;
console.log(count || 'no data'); // No data
console.log(count ?? 'no data'); // 0
```

6. Optional Chaining
```js
var item = {
    key1: {
        key2: "Hello",
    }
};
console.log(item.key1.key2.key3.key4); // Cannot read properties of undefined (reading 'key4')
console.log(item.key1?.key2?.key3?.key4); // undefined
```

7. The Array Map Method
```js
var doubled = [1, 2, 3].map(x => x * 2);
console.log(doubled); // [2, 4, 6]

var items = [
    {key1: "A", key2: "B"},
    {key1: "A", key2: "B"},
    {key1: "A", key2: "B"},
];
var mapped = items.map(item => item.key1);
console.log(mapped); // ['A', 'A', 'A']

var mapped = items.map(item => ({key1: item.key1}));
console.log(mapped); // [{key1: 'A'}, {key1: 'A'}, {key1: 'A'}]
```

8. The Array Filter Method
```js
var filtered = [1, 2, 3].filter(x => x > 1);
console.log(filtered); // [2, 3]

var movies = [
    {title: "Movie-1", genres: ["drama", "detective"]},
    {title: "Movie-2", genres: ["detective", "fantasy"]},
    {title: "Movie-3", genres: ["drama"]},
];
var detectives = movies.filter(movie => movie.genres.includes("detective"));
console.log(detectives); // Movie-1 Movie-2
```

9. The Array Reduce Method
```js
/*
 * Reduces the entire array into one value.
 * Array.reduce(callback(couner, item), initialValue);
 */
var movies = [
    {title: "Movie-1", duration: 120},
    {title: "Movie-2", duration: 90},
    {title: "Movie-3", duration: 75},
];
var totalDuration = movies.reduce((counter, movie) => counter + movie.duration, 0);
console.log(totalDuration); // 285
```

10. Array sort
```js
var data = [5, 3, 1, 4, 2];

data.sort((a, b) => a - b);
console.log(data); // [1, 2, 3, 4, 5]

data.sort((a, b) => b - a);
console.log(data); // [5, 4, 3, 2, 1]

// When we don't want to mutate (change) original array, we create a copy first.
var data = [5, 3, 1, 4, 2];
var sorted = data.slice().sort((a, b) => a - b);
console.log(data); // [5, 3, 1, 4, 2]
console.log(sorted); // [1, 2, 3, 4, 5]

var movies = [
    {title: "Movie-1", duration: 120},
    {title: "Movie-2", duration: 90},
    {title: "Movie-3", duration: 75},
];
var sortedMovies = movies.slice().sort((a, b) => a.duration - b.duration);
console.log(sortedMovies); // Movie-3 (75), Movie-2 (90), Movie-1 (120)
```

11. Promises
```js
fetch('https://api.adviceslip.com/advice')
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        console.log(data.slip.advice);
    });

fetch('https://api.adviceslip.com/advice')
    .then(res => res.json())
    .then(data => console.log(data.slip.advice));
```

12. Async / Await
```js
async function getAdvice() {
    const response = await fetch('https://api.adviceslip.com/advice');
    const data = await response.json();
    console.log(data.slip.advice);
}
getAdvice();
```

13. Timeouts
```js
setTimeout(() => { console.log("Hello!"); }, 3000);
```
