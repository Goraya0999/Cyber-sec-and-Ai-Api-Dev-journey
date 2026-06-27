# React: Button Component, State (`useState`), Events & Props (Lecture Notes)


---

# 1. Creating a Button

In React, HTML elements are written using JSX.

```tsx
<button>Place Bet</button>
```

Output:

```
[ Place Bet ]
```

Initially the button has the browser's default styling.

---

# 2. Styling with Tailwind CSS

Instead of writing CSS manually, Tailwind provides utility classes.

Example:

```tsx
<button
  className="
    border
    border-black
    px-4
    py-2
    rounded-sm
    bg-indigo-500
    text-white
  "
>
    Place Bet
</button>
```

Result:

* Black border
* Padding
* Rounded corners
* Indigo background
* White text

---

# 3. Why React Uses `className`

HTML uses

```html
class=""
```

React JSX uses

```tsx
className=""
```

Example

```tsx
<button className="bg-indigo-500">
```

Reason:

`class` is a reserved JavaScript keyword, so React uses `className`.

---

# 4. Common Tailwind Classes Used

| Class               | Meaning                  |
| ------------------- | ------------------------ |
| border              | Adds border              |
| border-black        | Black border             |
| px-4                | Horizontal padding       |
| py-2                | Vertical padding         |
| rounded-sm          | Slightly rounded corners |
| bg-indigo-500       | Indigo background        |
| text-white          | White text               |
| hover:bg-indigo-600 | Change color on hover    |
| transition-all      | Animate all properties   |
| duration-300        | 300 ms animation         |

---

# 5. Margin vs Padding

## Padding

Padding is **inside** an element.

```
+----------------------+
|    Padding           |
|   +--------------+   |
|   |   Content    |   |
|   +--------------+   |
+----------------------+
```

Tailwind

```tsx
px-4
py-2
```

---

## Margin

Margin is **outside** an element.

```
Margin

      ↓
+------------------+
|                  |
|   Element        |
|                  |
+------------------+
```

Example

```tsx
mt-4
```

Means

```
margin-top: 1rem;
```

---

# 6. Container and Centering

Container:

```tsx
<div className="container mx-auto">
```

Explanation

| Class     | Meaning                          |
| --------- | -------------------------------- |
| container | Fixed-width responsive container |
| mx-auto   | Centers horizontally             |

---

# 7. Making Button Full Width

```tsx
className="w-full"
```

Result

```
+------------------------------+
|       PLACE BET              |
+------------------------------+
```

---

# 8. Hover Effect

```tsx
hover:bg-indigo-600
```

When the mouse enters

```
Indigo 500
↓

Indigo 600
```

---

# 9. Smooth Animation

Instead of changing instantly

```tsx
transition-all duration-300
```

Now it smoothly fades.

---

# 10. Handling Click Events

React uses

```tsx
onClick
```

Example

```tsx
function myFunction() {
    console.log("Clicked!");
}

<button onClick={myFunction}>
    Place Bet
</button>
```

When clicked

```
Clicked!
```

appears in the browser console.

---

# 11. Console Output

```tsx
console.log("Hello")
```

During development (`yarn dev`)

```
Hello
Hello
```

During production (`yarn preview`)

```
Hello
```

React Strict Mode intentionally renders components twice in development to detect side effects.

---

# 12. React Hooks

A Hook is a special React function beginning with `use`.

Examples

* useState
* useEffect
* useRef
* useMemo

---

# 13. What is `useState`?

State stores information that can change while the application is running.

Example

```tsx
const [hasWon, setHasWon] = useState(false);
```

Meaning

```
hasWon
↓

Current value

false
```

```
setHasWon()

↓

Updates value
```

---

# 14. Understanding the Syntax

```tsx
const [value, setValue] = useState(initialValue);
```

Example

```tsx
const [count, setCount] = useState(0);
```

Initially

```
count = 0
```

After

```tsx
setCount(1)
```

React updates

```
count = 1
```

---

# 15. Updating State

```tsx
function handleClick() {
    setHasWon(true);
}
```

Now clicking the button changes

```
false

↓

true
```

---

# 16. React Re-render

Changing state causes React to re-render the component.

Example

```tsx
console.log("Hello");
```

Click button

```
Hello
```

prints again.

Why?

Because React runs the component again from top to bottom.

---

# 17. React Rendering Flow

```
Component renders

↓

Button clicked

↓

State changes

↓

React re-renders component

↓

Updated UI appears
```

---

# 18. Why `console.log()` Shows Old State

Example

```tsx
setHasWon(true);

console.log(hasWon);
```

Output

```
false
```

Why?

React updates state **asynchronously**.

The component has not re-rendered yet.

Correct sequence

```
setHasWon(true)

↓

React schedules update

↓

Component renders again

↓

hasWon becomes true
```

---

# 19. Parent and Child Components

Initially

```
Controller

└── Button
```

The button exists inside Controller.

It is **not** a separate component.

---

# 20. Creating a Separate Component

Create

```
components/

    Button.tsx
```

Example

```tsx
export default function Button() {
    return (
        <button>
            Place Bet
        </button>
    );
}
```

---

# 21. Importing Button

```tsx
import Button from "./components/Button";
```

Then

```tsx
<Button />
```

---

# 22. Passing Functions Using Props

Parent

```tsx
<Button runFunction={handlePlaceBet} />
```

Child

```tsx
type Props = {
    runFunction: any
}

function Button({ runFunction }: Props) {

    return (
        <button onClick={runFunction}>
            Place Bet
        </button>
    );
}
```

---

# 23. Data Flow

```
Controller

↓

passes function

↓

Button

↓

Button clicked

↓

runFunction()

↓

handlePlaceBet()

↓

State changes
```

---

# 24. Why Props Are Needed

The child component cannot directly access the parent's functions.

Without props

```
Button

×

Cannot find handlePlaceBet()
```

With props

```
Controller

↓

handlePlaceBet

↓

Button

↓

Button executes it
```

---

# 25. Component Hierarchy

```
App

↓

Controller

├── Button

├── BetBox

└── Other Components
```

---

# 26. Multiple Buttons

Once Button is reusable

```tsx
<Button runFunction={handlePlaceBet} />

<Button runFunction={handlePlaceBet} />
```

Output

```
[ Place Bet ]

[ Place Bet ]
```

Reusable components reduce duplicate code.

---

# 27. Development vs Production

Development

```bash
yarn dev
```

Features

* Hot reload
* Strict Mode
* Double render
* Easier debugging

---

Production Preview

```bash
yarn build

yarn preview
```

Features

* Optimized build
* Single render
* Faster performance

---

# 28. Complete Example

## Controller.tsx

```tsx
import { useState } from "react";
import Button from "./components/Button";

export default function Controller() {

    const [hasWon, setHasWon] = useState(false);

    function handlePlaceBet() {
        setHasWon(true);
    }

    return (
        <>
            <Button runFunction={handlePlaceBet} />
        </>
    );
}
```

---

## Button.tsx

```tsx
type Props = {
    runFunction: any;
};

export default function Button({ runFunction }: Props) {
    return (
        <button
            onClick={runFunction}
            className="
                border
                border-black
                px-4
                py-2
                rounded-sm
                bg-indigo-500
                hover:bg-indigo-600
                transition-all
                duration-300
                text-white
            "
        >
            Place Bet
        </button>
    );
}
```
