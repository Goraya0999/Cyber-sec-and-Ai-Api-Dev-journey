# React Betting App – BetButton Component & State Management (Markdown Notes)


# Project Component Structure

```
App
│
└── Controller
      │
      └── BetBox
            │
            ├── BetButton (Down)
            └── BetButton (Up)
```

The **Controller** owns the application's state.

The state is passed downward through the component tree.

```
Controller
      ↓
   BetBox
      ↓
 BetButton
```

This is called **Props Drilling**.

---

# Step 1 — Create BetButton Component

Create a new component.

```
components/
    BetButton.tsx
```

Generate boilerplate.

```tsx
const BetButton = () => {
    return <div>BetButton</div>;
}

export default BetButton;
```

---

# Step 2 — Import BetButton into BetBox

Replace placeholder text with reusable buttons.

Before

```tsx
<div>BET BUTTON 1</div>
<div>BET BUTTON 2</div>
```

After

```tsx
<BetButton />
<BetButton />
```

Result

```
BetButton
BetButton
```

Now both buttons are rendered from the same reusable component.

---

# Step 3 — Use Heroicons

Download icons from

```
https://heroicons.com
```

Search

```
Arrow Down
Arrow Up
```

Copy the JSX for each SVG.

Store them as constants.

```tsx
const buttonDown = (
    <svg>...</svg>
)

const buttonUp = (
    <svg>...</svg>
)
```

Now they can be reused anywhere.

---

# Step 4 — Render Icons

Simply render the JSX variable.

```tsx
return (
    <>
        {buttonDown}
    </>
)
```

Later we will display either the Up or Down icon depending on Props.

---

# Step 5 — Create Props

The button needs to know:

* Is it an Up button?
* Is it a Down button?

Create Props.

```tsx
type Props = {
    direction: string
}
```

Receive props.

```tsx
const BetButton = ({ direction }: Props) => {

}
```

---

# Step 6 — Conditional Rendering

Display different icons.

```tsx
{
    direction === "up"
        ? buttonUp
        : buttonDown
}
```

If

```
direction = "up"
```

Shows

```
↑
```

Otherwise

```
↓
```

---

# Step 7 — Pass Props

Inside BetBox.

```tsx
<BetButton direction="down" />
<BetButton direction="up" />
```

Result

```
↓      ↑
```

One reusable component behaves differently depending on its Props.

---

# Why Reusable Components?

Instead of making

```
UpButton
DownButton
```

You create

```
BetButton
```

and customize it.

Advantages

* Less code
* Easier maintenance
* Reusable
* More scalable

---

# Step 8 — Wrap Icons in Button Element

Instead of returning SVG directly.

```tsx
<button>
    {buttonUp}
</button>
```

Now the SVG becomes clickable.

---

# Step 9 — Tailwind Styling

Example styling

```tsx
className="
p-10
rounded-full
bg-gray-200
"
```

Useful classes

| Class              | Purpose         |
| ------------------ | --------------- |
| p-10               | Padding         |
| rounded-full       | Circular button |
| bg-gray-200        | Default color   |
| hover:bg-green-400 | Hover effect    |
| border             | Border          |

---

# Step 10 — Larger Icons

Increase SVG size.

Before

```
h-6
w-6
```

After

```
h-10
w-10
```

Result

```
Larger arrow
Better visibility
```

---

# Step 11 — Reusable Button

React allows unlimited reuse.

```tsx
<BetButton direction="up" />
<BetButton direction="down" />
<BetButton direction="up" />
<BetButton direction="down" />
```

Only one component exists.

---

# Step 12 — Where Should State Live?

Question:

Should BetButton store whether it is selected?

No.

Because then

```
Up = Green
Down = Red
```

could happen simultaneously.

That is incorrect.

Instead

```
Controller
```

stores the selected direction.

This is called

> **Lifting State Up**

---

# Step 13 — Create State

Inside Controller.

```tsx
const [betDirection, setBetDirection] =
useState("up")
```

State

```
betDirection
```

Possible values

```
up
down
```

---

# Step 14 — Pass State to BetBox

```tsx
<BetBox
    betDirection={betDirection}
    setBetDirection={setBetDirection}
/>
```

---

# Step 15 — Receive Props

```tsx
type Props = {
    betDirection: string
    setBetDirection: any
}
```

Receive them.

```tsx
const BetBox = ({
    betDirection,
    setBetDirection
}: Props)
```

---

# Step 16 — Pass Props Again

BetBox passes them to BetButton.

```tsx
<BetButton
    direction="up"
    betDirection={betDirection}
    setBetDirection={setBetDirection}
/>

<BetButton
    direction="down"
    betDirection={betDirection}
    setBetDirection={setBetDirection}
/>
```

Data flow

```
Controller
      ↓
BetBox
      ↓
BetButton
```

---

# Props Drilling

Passing data through multiple levels is called

> Props Drilling

Example

```
Controller
      ↓
BetBox
      ↓
BetButton
```

Later React offers better solutions

* useContext
* Redux
* Zustand

---

# Step 17 — Dynamic Tailwind Classes

Default button

```
Gray
```

Selected

```
Green
```

or

```
Red
```

Example

```tsx
className={`

p-10
rounded-full

${
betDirection === "up"
?
"bg-green-400"
:
"bg-gray-200"
}
`}
```

Meaning

```
If selected

↓

Green

Else

↓

Gray
```

---

# Down Button

```tsx
betDirection === "down"

?
"bg-red-400"

:
"bg-gray-200"
```

---

# Step 18 — Handle Click

Up button

```tsx
onClick={() =>
setBetDirection("up")
}
```

Down button

```tsx
onClick={() =>
setBetDirection("down")
}
```

Whenever user clicks

```
↑

↓

State changes
```

---

# Application Flow

```
Click Up

↓

State becomes

up

↓

Up Button

Green

↓

Down Button

Gray
```

Click Down

```
↓

State

down

↓

Down Button

Red

↓

Up Button

Gray
```

---

# Step 19 — Better Layout

Center button.

```tsx
mx-auto
```

Vertical spacing.

```tsx
py-12
```

Smooth animation.

```tsx
transition-all
duration-300
```

---

# Step 20 — Softer Colors

Instead of

```
green-500
```

Use

```
green-400
```

Instead of

```
red-500
```

Use

```
red-400
```

Creates a more pleasant UI.

---

# Step 21 — Monitor State

```tsx
console.log(betDirection)
```

Inside

```tsx
useEffect(() => {

console.log(betDirection)

}, [betDirection])
```

Output

```
up

↓

down

↓

up

↓

down
```

Runs every time the selected direction changes.

---

# Why Store State in Controller?

Because later

```
Submit Bet
```

needs to know

```
Did user bet UP?

or

Did user bet DOWN?
```

The Controller already has that information.

---

# Overall Data Flow

```
User Clicks

↓

BetButton

↓

setBetDirection()

↓

Controller State Updates

↓

Controller Re-renders

↓

BetBox Receives New Props

↓

BetButton Receives New Props

↓

UI Updates Automatically
```

-
