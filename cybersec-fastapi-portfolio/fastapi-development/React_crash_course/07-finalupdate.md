# React Betting App - Loading State, API Integration & Result Display



# The application now:

- Fetches a random number from an API.
- Shows a loading status while waiting.
- Determines whether the player won.
- Displays the random number.
- Displays **WINNER** or **BAD LUCK**.

---

# Final UI

```
-------------------------------------
STATUS
Loading...
-------------------------------------

        ↑       ↓

-------------------------------------
Random Number Returned: 73
-------------------------------------

           WINNER
```

---

# Step 1 - Create Loading State

Inside `Controller.tsx`

```tsx
const [isLoading, setIsLoading] = useState(false);
```

## Why?

API requests take time.

While waiting for the response, we want the application to show:

```
Loading...
```

instead of showing old data.

Initially:

```tsx
false
```

because nothing is loading.

---

# Step 2 - Turn Loading On

Before calling the API:

```tsx
setIsLoading(true);
```

Flow:

```
User clicks Place Bet
        ↓
Loading starts
        ↓
Show Loading...
```

---

# Step 3 - Turn Loading Off

After the API finishes:

```tsx
setIsLoading(false);
```

Flow:

```
Loading...
        ↓
API Finished
        ↓
Show Result
```

---

# Step 4 - Pass Loading State to BetBox

Inside Controller

```tsx
<BetBox
    isLoading={isLoading}
/>
```

Props

```tsx
type Props = {
    isLoading: boolean;
}
```

Receive it

```tsx
function BetBox({ isLoading }: Props)
```

---

## Why use Props?

React components cannot directly access another component's state.

Controller owns

```
isLoading
```

BetBox needs that value.

Therefore:

```
Controller
      ↓
Props
      ↓
BetBox
```

---

# Step 5 - Conditional Rendering

Inside BetBox

```tsx
{
    isLoading
        ? "Loading..."
        : "Random Number Returned 1234"
}
```

This uses the **ternary operator**.

General syntax

```tsx
condition
    ? valueIfTrue
    : valueIfFalse
```

Example

```tsx
true
?
"Loading"
:
"Done"
```

Output

```
Loading
```

---

# Step 6 - Styling

Tailwind classes

```tsx
text-right
pr-5
bg-gray-800
text-white
py-4
```

Result

```
--------------------------
           Loading...
--------------------------
```

---

# Step 7 - Store the Random Number

Previously, the application only stored

```
Winner or Loser
```

It never stored

```
73
42
91
```

Create state

```tsx
const [valStored, setValStored] = useState(0);
```

---

## Why initialize with 0?

Before clicking Place Bet

there is no random number.

```
0
```

means

```
No result yet.
```

---

# Step 8 - Save the API Result

After receiving the response

```tsx
const val = response.data;
```

Store it

```tsx
setValStored(val);
```

Now React remembers

```
73
```

or

```
81
```

or

```
44
```

---

# Step 9 - Pass More Props

Controller

```tsx
<BetBox
    valStored={valStored}
    hasWon={hasWon}
/>
```

Props

```tsx
type Props = {
    valStored: number;
    hasWon: boolean;
}
```

---

# Step 10 - Display the Random Number

Instead of

```tsx
"Random Number Returned 1234"
```

Use

```tsx
`Random Number Returned ${valStored}`
```

This is called a **Template Literal**.

Instead of

```tsx
"Random Number Returned " + valStored
```

Use

```tsx
`Random Number Returned ${valStored}`
```

Cleaner and easier to read.

---

# Step 11 - Show Result Only After First Bet

Problem

Initially

```tsx
hasWon = false;
```

Without any condition,

the application immediately displays

```
BAD LUCK
```

even though the player has not played.

---

Solution

```tsx
valStored !== 0
```

Meaning

```
Only display Winner/Loser
after receiving a random number.
```

---

# Step 12 - Winner / Loser Logic

```tsx
{
valStored !== 0 &&
(
    hasWon
        ? "WINNER"
        : "BAD LUCK"
)
}
```

Two concepts are used together.

First

```tsx
valStored !== 0 &&
```

means

```
Only render if a number exists.
```

Then

```tsx
hasWon
?
"WINNER"
:
"BAD LUCK"
```

---

### Example 1

```tsx
valStored = 0
```

Output

```
Nothing
```

---

### Example 2

```tsx
valStored = 81
hasWon = true
```

Output

```
WINNER
```

---

### Example 3

```tsx
valStored = 35
hasWon = false
```

Output

```
BAD LUCK
```

---

# Step 13 - Dynamic Colors

Instead of fixed colors

```tsx
className={`
${
hasWon
?
"text-green-500"
:
"text-red-500"
}
`}
```

If

```
Winner
```

↓

Green

If

```
Loser
```

↓

Red

---

# Step 14 - Improve Styling

Added

```tsx
text-center
```

Centers the text.

Added

```tsx
text-4xl
```

Makes the text large.

Added

```tsx
font-bold
```

Makes the text bold.

Result

```
WINNER
```

or

```
BAD LUCK
```

becomes much more visible.

---

# Step 15 - API Request Flow

```
User clicks Place Bet
          │
          ▼
setIsLoading(true)
          │
          ▼
Axios API Request
          │
          ▼
Receive Random Number
          │
          ▼
Store Number
          │
          ▼
Check Win/Loss
          │
          ▼
Update hasWon
          │
          ▼
setIsLoading(false)
          │
          ▼
React Re-renders UI
          │
          ▼
Display Number
Display Winner/Bad Luck
```

---

# Complete Data Flow

```
User
 │
 ▼
Place Bet Button
 │
 ▼
handlePlaceBet()
 │
 ▼
setIsLoading(true)
 │
 ▼
Axios GET Request
 │
 ▼
Random.org API
 │
 ▼
Returns Random Number
 │
 ▼
Store Number (valStored)
 │
 ▼
Compare Number with betDirection
 │
 ▼
Set hasWon
 │
 ▼
setIsLoading(false)
 │
 ▼
Pass Props
 │
 ▼
BetBox
 │
 ├── Show Loading
 ├── Show Random Number
 └── Show Winner/Bad Luck
```

---

# React Concepts Learned

| Concept | Purpose |
|----------|----------|
| `useState()` | Store application state |
| Props | Pass data from parent to child |
| Conditional Rendering | Show different UI depending on state |
| Ternary Operator (`? :`) | Choose between two values |
| Logical AND (`&&`) | Render only when condition is true |
| Template Literals | Insert variables inside strings |
| Axios | Fetch data from APIs |
| Async/Await | Wait for asynchronous operations |
| Dynamic Tailwind Classes | Change styling based on state |

---

# Final Component Structure

```
App
│
└── Controller
      │
      ├── betDirection
      ├── hasWon
      ├── isLoading
      ├── valStored
      │
      ├── handlePlaceBet()
      │
      ▼
    BetBox
      │
      ├── Status
      ├── Random Number
      ├── Winner / Bad Luck
      │
      ▼
    BetButton
      ├── Up Button
      └── Down Button
```

---
