# React Betting App Notes (Markdown)

# Fetching Data from an API & Displaying Results

## Goal of This Lesson

The application design has changed slightly.

Instead of:

* **Layer 1:** Showing the bet buttons
* **Layer 3:** Showing another section

The new design is:

```
+--------------------------------+
| Layer 1                        |
| Status                         |
| (Loading / You Bet Up / Down)  |
+--------------------------------+
| Layer 2                        |
| Up Button      Down Button     |
+--------------------------------+
| Layer 3                        |
| Result                         |
| Winner / Loser + Random Number |
+--------------------------------+
```

This makes the UI more meaningful because:

* The selected button already tells us the user's bet.
* The top can show the current application status.
* The bottom can show the game result.

---

# Why Use an API?

Instead of generating a random number inside JavaScript, the instructor uses an API.

Why?

Because almost every React application does the following:

* Fetch data
* Display data
* Update data

Learning API calls is much more valuable than learning JavaScript random numbers.

---

# Axios

The project uses **Axios** for HTTP requests.

Import it:

```tsx
import axios from "axios";
```

---

# Making the Function Asynchronous

Since fetching data takes time, the function becomes asynchronous.

```tsx
const handlePlaceBet = async () => {

}
```

Inside an async function we can use:

```tsx
await
```

which waits until the API responds.

---

# Default Winner State

Initially assume the user loses.

```tsx
let isWinner = false;
```

Later, if conditions are satisfied:

```tsx
isWinner = true;
```

---

# API URL

Store the API URL inside a variable.

```tsx
const url = "...";
```

Using a variable makes the code easier to read and easier to maintain.

---

# Fetching Data

```tsx
await axios.get(url)
```

This sends a GET request.

The API returns a response.

---

# Using `.then()`

```tsx
await axios.get(url).then((response) => {

});
```

`.then()` executes only after the API successfully returns data.

---

# Checking the Response

Good practice:

```tsx
if(response.status === 200){
    console.log(response.data);
}
```

HTTP Status Code **200** means:

> The request succeeded.

---

# Handling Errors

Always add `.catch()`.

```tsx
.catch((error)=>{
    console.log(error.message);
});
```

This prevents your application from crashing if something goes wrong.

---

# Response Object

The API returns a response object.

Important properties:

```tsx
response.status
```

Example:

```
200
```

Meaning:

```
Success
```

---

```tsx
response.data
```

Example:

```
73
```

This is the actual random number.

---

# API Flow

```
Button Click

      ↓

handlePlaceBet()

      ↓

axios.get(url)

      ↓

API Server

      ↓

Response

      ↓

response.data

      ↓

Random Number
```

---

# Example Returned Numbers

```
73
53
58
23
51
```

Every click produces a new random number.

---

# Store the Number

Instead of repeatedly writing:

```tsx
response.data
```

store it in a variable.

```tsx
const val = response.data;
```

Example:

```
val = 73
```

---

# Betting Logic

The application has two possible bets:

```
UP
DOWN
```

Winning rules:

```
If number >= 50

AND

User selected UP

↓

Winner
```

---

Second rule:

```
If number < 50

AND

User selected DOWN

↓

Winner
```

Otherwise:

```
Loser
```

---

# Code

```tsx
if(val >= 50 && betDirection === "up"){
    isWinner = true;
}
else if(val < 50 && betDirection === "down"){
    isWinner = true;
}
```

---

# Save Winner State

After checking conditions:

```tsx
setHasWon(isWinner);
```

React updates the state.

---

# Why Use a Variable?

Instead of writing:

```tsx
setHasWon(true);
```

or

```tsx
setHasWon(false);
```

many times,

the code calculates everything first.

Finally:

```tsx
setHasWon(isWinner);
```

Cleaner and easier to maintain.

---

# Debugging

The instructor prints values to the console.

```tsx
console.log(val);
```

Shows:

```
35
64
77
55
37
```

---

Also:

```tsx
console.log(hasWon);
```

Shows:

```
true
false
```

---

# Why Doesn't `useEffect` Print Every Time?

Suppose:

```
hasWon = false
```

Another losing bet:

```
hasWon = false
```

Nothing changed.

React doesn't rerun the effect because the dependency value stayed the same.

Example:

```
false

↓

false
```

No change.

---

But:

```
false

↓

true
```

React detects a change.

`useEffect` runs again.

---

# Dependency Array

```tsx
useEffect(()=>{
    console.log(hasWon);
}, [hasWon]);
```

This means:

> Run only when `hasWon` changes.

---

# Example

User bets **UP**

API returns:

```
35
```

Condition:

```
35 >= 50

False
```

Result:

```
Loser
```

---

Next click:

```
64
```

Condition:

```
64 >= 50

True
```

Result:

```
Winner
```

---

Next click:

```
77
```

Still a winner.

```
true

↓

true
```

No state change.

No `useEffect`.

---

Now bet **DOWN**

API returns:

```
55
```

```
55 < 50

False
```

Lose.

```
true

↓

false
```

React detects the change.

`useEffect` runs.

---

Another click:

```
37
```

```
37 < 50

True
```

Winner.

```
false

↓

true
```

`useEffect` runs again.

---

# Future UI

## Layer 1

Will display status.

Examples:

```
Loading...
```

```
You Bet Up
```

```
You Bet Down
```

---

## Layer 2

Contains:

```
↑ Up Button

↓

Down Button
```

---

## Layer 3

Displays results.

Example:

```
Random Number: 73

Winner
```

or

```
Random Number: 22

Loser
```

---

# Complete Flow

```
User Clicks Button

        ↓

handlePlaceBet()

        ↓

Axios GET Request

        ↓

Random Number API

        ↓

Receive Number

        ↓

Store in val

        ↓

Compare with Bet Direction

        ↓

Determine Winner

        ↓

Update React State

        ↓

React Re-renders

        ↓

UI Shows

Status
Random Number
Winner/Loser
```

---

# Important Concepts Learned

## React

* `useState`
* `useEffect`
* Component state
* Parent-managed state
* Re-rendering

---

## JavaScript

* Async functions
* `await`
* Variables
* `if / else`
* Boolean logic

---

## Axios

* `axios.get()`
* `.then()`
* `.catch()`
* `response.status`
* `response.data`

---

## API Concepts

* GET Request
* HTTP Status Code 200
* API Response
* Error Handling
* Fetching Data

---
