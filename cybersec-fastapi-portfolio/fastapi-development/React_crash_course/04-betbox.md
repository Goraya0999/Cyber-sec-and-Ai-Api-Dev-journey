# BetBox Layout with Tailwind CSS (React + TypeScript)



# 1. Creating the BetBox Component

### Step 1: Create a new component

```
components/
│── Button.tsx
│── BetBox.tsx
```

Generate the component:

```tsx
import React from "react";

const BetBox = () => {
  return (
    <div>
      BetBox
    </div>
  );
};

export default BetBox;
```

---

### Step 2: Import it into Controller

```tsx
import BetBox from "./components/BetBox";

function Controller() {
    return (
        <>
            <Button />
            <BetBox />
        </>
    )
}
```

Result:

```
Place Bet Button

BetBox
```

---

# 2. Responsive Layout

Instead of using Tailwind's `container`, the instructor creates a responsive width.

```tsx
<div className="
    lg:w-[1200px]
    md:w-[850px]
    w-full
    px-5
">
```

### Explanation

| Tailwind Class  | Meaning                         |
| --------------- | ------------------------------- |
| `lg:w-[1200px]` | Width = 1200px on large screens |
| `md:w-[850px]`  | Width = 850px on medium screens |
| `w-full`        | Full width on mobile            |
| `px-5`          | Horizontal padding              |

---

## Responsive Behavior

Large Screen

```
┌────────────────────────1200px────────────────────────┐
```

Medium Screen

```
┌──────────────850px──────────────┐
```

Mobile

```
┌────────────100%────────────┐
```

---

# 3. Increase Button Size

Old

```tsx
py-2
```

New

```tsx
py-12
```

Result

```
┌──────────────────────────────┐
│                              │
│          PLACE BET           │
│                              │
└──────────────────────────────┘
```

---

# 4. Build BetBox Structure

The instructor first ignores styling and builds the HTML structure.

```tsx
<div>

    <div>
        Layer 1
    </div>

    <div>
        Layer 2
    </div>

    <div>
        Layer 3
    </div>

</div>
```

Output

```
Layer 1

Layer 2

Layer 3
```

---

# 5. Understanding the Layout

The final design contains three vertical sections.

```
+------------------------------------+
|             Layer 1                |
+------------------------------------+
|             Layer 2                |
+------------------------------------+
|             Layer 3                |
+------------------------------------+
```

---

# 6. Add Padding and Borders

Each layer receives padding and borders.

```tsx
className="py-2 border"
```

Result

```
+----------------------+
| Layer 1              |
+----------------------+

+----------------------+
| Layer 2              |
+----------------------+

+----------------------+
| Layer 3              |
+----------------------+
```

---

# 7. Add Controller Padding

Instead of adding margin to the button, padding is added to the Controller.

```tsx
py-12
```

Benefits

* More consistent spacing
* Easier responsive design
* Parent controls layout instead of child

---

# 8. Give Each Layer a Different Color

Temporary colors make layout debugging easier.

```tsx
Layer 1

bg-red-100

Layer 2

bg-blue-100

Layer 3

bg-fuchsia-100
```

Visual

```
🟥 Layer 1

🟦 Layer 2

🟪 Layer 3
```

These colors are only for development.

---

# 9. Separate Button and BetBox

Margin is added above BetBox.

```tsx
mt-5
```

Result

```
Place Bet


Layer 1

Layer 2

Layer 3
```

---

# 10. Build Layer 2 with Flexbox

Layer 2 contains two betting buttons.

Instead of stacking vertically:

```
Button 1

Button 2
```

Use Flexbox.

```tsx
<div className="flex">

    <div>
        Bet Button 1
    </div>

    <div>
        Bet Button 2
    </div>

</div>
```

Result

```
Bet Button 1      Bet Button 2
```

---

# 11. flex-row vs flex-col

Default

```tsx
flex-row
```

Output

```
Button 1      Button 2
```

---

Vertical

```tsx
flex-col
```

Output

```
Button 1

Button 2
```

---

# 12. justify-between

```tsx
justify-between
```

This pushes children to opposite ends.

Without

```
Button1 Button2
```

With

```
Button1               Button2
```

---

# 13. Give Each Button Full Width

```tsx
w-full
```

Result

```
+---------------+---------------+
|               |               |
|   Button 1    |   Button 2    |
|               |               |
+---------------+---------------+
```

Each occupies roughly half of the available space.

---

# 14. Add Vertical Padding

```tsx
py-12
```

Result

```
+---------------+---------------+
|               |               |
|               |               |
|   Button 1    |   Button 2    |
|               |               |
|               |               |
+---------------+---------------+
```

---

# 15. Center Text

```tsx
text-center
```

Before

```
Button 1
```

After

```
     Button 1
```

---

# Final BetBox Structure

```
+--------------------------------------------------+

                 PLACE BET

+--------------------------------------------------+

🟥 Layer 1

+--------------------------------------------------+

🟦 Layer 2

+----------------------+---------------------------+
|                      |                           |
|                      |                           |
|    BET BUTTON 1      |      BET BUTTON 2         |
|                      |                           |
|                      |                           |
+----------------------+---------------------------+

🟪 Layer 3

+--------------------------------------------------+
```

---

# Tailwind Classes Used

| Class             | Purpose             |
| ----------------- | ------------------- |
| `w-full`          | Full width          |
| `lg:w-[1200px]`   | Large screen width  |
| `md:w-[850px]`    | Medium screen width |
| `px-5`            | Horizontal padding  |
| `py-12`           | Vertical padding    |
| `mt-5`            | Margin top          |
| `border`          | Border              |
| `bg-red-100`      | Red background      |
| `bg-blue-100`     | Blue background     |
| `bg-fuchsia-100`  | Purple background   |
| `flex`            | Enable Flexbox      |
| `flex-row`        | Horizontal layout   |
| `flex-col`        | Vertical layout     |
| `justify-between` | Push children apart |
| `text-center`     | Center text         |

---
