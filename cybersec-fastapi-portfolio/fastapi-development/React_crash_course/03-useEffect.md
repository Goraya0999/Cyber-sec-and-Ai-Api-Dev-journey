# React `useEffect` Hook – Complete Notes

---

# What is `useEffect`?

`useEffect` is a **React Hook** that allows you to perform **side effects** in functional components.

A **side effect** is any operation that happens outside of rendering the UI, such as:

* Fetching data from an API
* Logging values to the console
* Updating the DOM
* Setting timers
* Listening for events
* Synchronizing with external systems

---

# Basic Syntax

```tsx
useEffect(() => {
    // Side effect code
}, [dependencies]);
```

The `useEffect` Hook has **two parts**:

1. **Callback Function**

   * Contains the code that React executes.

2. **Dependency Array**

   * Controls **when** the callback should execute.

---

# Structure

```tsx
useEffect(() => {

    // Your side effect

}, [dependency1, dependency2]);
```

---

# Three Ways to Use `useEffect`

## 1. Without a Dependency Array

```tsx
useEffect(() => {
    console.log("Runs every render");
});
```

### Runs

* Initial render
* Every re-render

Flow:

```
Render

↓

useEffect()

↓

Render Again

↓

useEffect()
```

---

## 2. Empty Dependency Array

```tsx
useEffect(() => {
    console.log("Runs once");
}, []);
```

### Runs

* Only after the component is mounted.

Flow:

```
Component Mount

↓

useEffect()

↓

Never Runs Again
```

Example:

```tsx
useEffect(() => {
    console.log("Hello");
}, []);
```

Development Mode

```
Hello
Hello
```

Production Mode

```
Hello
```

---

## 3. Dependency Array

```tsx
useEffect(() => {
    console.log(hasWon);
}, [hasWon]);
```

Runs:

* Initial render
* Every time `hasWon` changes

Flow:

```
hasWon Changes

↓

useEffect()

↓

Console Updates
```

---

# Understanding Dependencies

Example

```tsx
const [count, setCount] = useState(0);

useEffect(() => {
    console.log(count);
}, [count]);
```

Whenever `count` changes

```
count changes

↓

useEffect Executes

↓

Console prints new value
```

---

# Why Doesn't State Update Immediately?

Example

```tsx
const [hasWon, setHasWon] = useState(false);

const handlePlaceBet = () => {
    setHasWon(true);

    console.log(hasWon);
};
```

Output

```
false
```

Why?

Because React updates state **asynchronously**.

Execution Order

```
Button Click

↓

setHasWon(true)

↓

console.log(hasWon)

↓

React Updates State

↓

Component Re-renders
```

The console still prints the **old state**.

---

# Correct Way

```tsx
const [hasWon, setHasWon] = useState(false);

const handlePlaceBet = () => {
    setHasWon(true);
};

useEffect(() => {
    console.log(hasWon);
}, [hasWon]);
```

Flow

```
Button Click

↓

State Updated

↓

Component Re-renders

↓

useEffect()

↓

Console prints updated state
```

---

# Toggling State

Instead of

```tsx
setHasWon(true);
```

Use

```tsx
setHasWon(!hasWon);
```

If

```
false
```

becomes

```
true
```

If

```
true
```

becomes

```
false
```

---

# Complete Example

```tsx
import { useState, useEffect } from "react";

function App() {

    const [hasWon, setHasWon] = useState(false);

    const handlePlaceBet = () => {
        setHasWon(!hasWon);
    };

    useEffect(() => {
        console.log("Current State:", hasWon);
    }, [hasWon]);

    return (
        <button onClick={handlePlaceBet}>
            Place Bet
        </button>
    );
}

export default App;
```

Console Output

```
Current State: false

↓

Click

↓

Current State: true

↓

Click

↓

Current State: false
```

---

# Component Lifecycle

```
Component Loads

↓

Render JSX

↓

useEffect()

↓

User Clicks Button

↓

State Changes

↓

Component Re-renders

↓

useEffect()
```

---

# React Re-render Flow

```
User Clicks Button

↓

setState()

↓

React Marks Component Dirty

↓

Component Function Executes Again

↓

New JSX Created

↓

Virtual DOM Compared

↓

Real DOM Updated

↓

useEffect Executes
```

---

# Why "Hello" Prints Twice in Development?

Example

```tsx
useEffect(() => {
    console.log("Hello");
}, []);
```

Output

```
Hello
Hello
```

Reason:

React **Strict Mode** intentionally renders components twice in development to detect side effects and potential bugs.

Development

```
Render

↓

Render Again

↓

useEffect()
```

Production

```
Render

↓

useEffect()
```

---

# Parent and Child Components

## Parent Component

```tsx
<Controller>
    <Button />
</Controller>
```

The parent owns the state.

```
Controller

↓

Button
```

The child should not modify the parent's state directly.

Instead, the parent passes a function.

---

## Parent

```tsx
<Button runFunction={handlePlaceBet} />
```

---

## Child

```tsx
type Props = {
    runFunction: any;
};

function Button({ runFunction }: Props) {

    return (
        <button onClick={runFunction}>
            Place Bet
        </button>
    );
}
```

Flow

```
Button Click

↓

runFunction()

↓

handlePlaceBet()

↓

setHasWon()

↓

Controller Re-renders
```

---

# State Flow

```
Controller

↓

State (hasWon)

↓

Passed to Child

↓

Button Click

↓

runFunction()

↓

setHasWon()

↓

Component Re-renders

↓

useEffect()

↓

Console Updated
```

---

# Important React Hooks

## `useState`

Stores and updates component state.

```tsx
const [count, setCount] = useState(0);
```

---

## `useEffect`

Performs side effects.

```tsx
useEffect(() => {

}, []);
```

---

# Key Terms

| Term             | Meaning                                                                                               |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| Hook             | A special React function that adds state or lifecycle features to functional components.              |
| useState         | Stores and updates component state.                                                                   |
| useEffect        | Executes side effects after rendering.                                                                |
| Dependency Array | Controls when `useEffect` executes.                                                                   |
| State            | Data managed by a component that can change over time.                                                |
| Re-render        | React executes the component function again to generate updated UI.                                   |
| Side Effect      | Operations such as API requests, timers, logging, or DOM manipulation.                                |
| Strict Mode      | React development feature that intentionally performs extra renders/effect executions to detect bugs. |

---

# Best Practices

* Use `useEffect` only for side effects.
* Include all required dependencies in the dependency array.
* Keep each effect focused on a single responsibility.
* Avoid unnecessary state updates inside `useEffect`.
* Remember that state updates are asynchronous.
* Clean up subscriptions, timers, and event listeners when necessary by returning a cleanup function from `useEffect`.

