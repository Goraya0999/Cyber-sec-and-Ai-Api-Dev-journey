````md
# Creating and Styling a Button Component with React and Tailwind CSS



# Creating a Button Component

Inside the `Controller` component, create a button just like regular HTML.

```jsx
<button>Place Bet</button>
```

Output:

```
Place Bet
```

At this point, the button has no styling.

---

# Using `className` in React

Unlike HTML, React uses **`className`** instead of `class`.

❌ HTML

```html
<button class="btn">Place Bet</button>
```

✅ React (JSX)

```jsx
<button className="btn">Place Bet</button>
```

### Why?

- `class` is a reserved keyword in JavaScript.
- JSX uses `className` to assign CSS classes.

---

# Adding a Border

```jsx
<button className="border">
    Place Bet
</button>
```

Result:

- Thin border around the button.

---

# Changing Border Color

```jsx
<button className="border border-black">
    Place Bet
</button>
```

Result:

- Black border
- Easier to see

---

# Adding Padding

## Horizontal Padding

```jsx
className="px-4"
```

`px` = Padding Left + Right

---

## Vertical Padding

```jsx
className="py-2"
```

`py` = Padding Top + Bottom

Example:

```jsx
<button className="border border-black px-4 py-2">
    Place Bet
</button>
```

Result:

- Bigger button
- Better spacing

---

# Margin vs Padding

## Margin

Margin creates space **outside** an element.

```
+----------------------+
|      Margin          |
|  +---------------+   |
|  |   Element     |   |
|  +---------------+   |
+----------------------+
```

Example:

```css
margin-top:20px;
```

Tailwind:

```text
mt-4
```

---

## Padding

Padding creates space **inside** an element.

```
+----------------------+
|    Border            |
|  +---------------+   |
|  |   Padding     |   |
|  |  Content      |   |
|  +---------------+   |
+----------------------+
```

Example:

```css
padding:10px;
```

Tailwind:

```text
px-4
py-2
```

---

# Rounded Corners

```jsx
rounded-sm
```

Example

```jsx
<button className="rounded-sm">
```

Result:

Small rounded corners.

---

# Background Color

```jsx
bg-indigo-500
```

Example

```jsx
<button className="bg-indigo-500">
```

Result:

Indigo-colored button.

---

# Text Color

```jsx
text-white
```

Example

```jsx
<button className="bg-indigo-500 text-white">
```

Result:

White text on indigo background.

---

# Complete Styled Button

```jsx
<button
className="
border
border-black
px-4
py-2
rounded-sm
bg-indigo-500
text-white"
>
Place Bet
</button>
```

Result:

✔ Border

✔ Padding

✔ Rounded corners

✔ Indigo background

✔ White text

---

# Styling the Container

Initially:

```jsx
<div>
```

After adding Tailwind:

```jsx
<div className="container mx-auto bg-green-500">
```

### Explanation

| Class | Purpose |
|---------|----------|
| `container` | Creates a responsive fixed-width container |
| `mx-auto` | Centers the container horizontally |
| `bg-green-500` | Green background |

---

# Full Width Button

```jsx
w-full
```

Example

```jsx
<button className="w-full">
```

Result:

Button stretches across the entire container width.

---

# Adding Top Margin

```jsx
mt-4
```

Example

```jsx
<button className="mt-4">
```

Result:

Moves the button down from the top.

---

# Hover Effect

```jsx
hover:bg-indigo-600
```

Example

```jsx
<button
className="
bg-indigo-500
hover:bg-indigo-600"
>
```

Result:

When the mouse hovers over the button, the background changes from:

```
Indigo 500
↓

Indigo 600
```

---

# Smooth Transition

Without transition:

Hover color changes instantly.

With transition:

```jsx
transition-all duration-300
```

Example

```jsx
<button
className="
bg-indigo-500
hover:bg-indigo-600
transition-all
duration-300"
>
```

### Explanation

| Class | Meaning |
|---------|---------|
| `transition-all` | Animate every changing property |
| `duration-300` | Animation lasts 300 milliseconds |

Result:

Smooth fade animation during hover.

---

# Final Button Code

```jsx
<button
className="
border
border-black
px-4
py-2
rounded-sm
bg-indigo-500
text-white
w-full
mt-4
hover:bg-indigo-600
transition-all
duration-300"
>
Place Bet
</button>
```

---

# Tailwind Classes Used

| Class | Description |
|---------|-------------|
| `border` | Adds border |
| `border-black` | Black border |
| `px-4` | Horizontal padding |
| `py-2` | Vertical padding |
| `rounded-sm` | Small rounded corners |
| `bg-indigo-500` | Indigo background |
| `text-white` | White text |
| `container` | Responsive container |
| `mx-auto` | Center horizontally |
| `w-full` | Full width |
| `mt-4` | Margin top |
| `hover:bg-indigo-600` | Hover background color |
| `transition-all` | Smooth transition |
| `duration-300` | 300 ms animation |

---

# React Component Example

```jsx
function Controller() {
  return (
    <div className="container mx-auto bg-green-500">

      <button
        className="
        border
        border-black
        px-4
        py-2
        rounded-sm
        bg-indigo-500
        text-white
        w-full
        mt-4
        hover:bg-indigo-600
        transition-all
        duration-300"
      >
        Place Bet
      </button>

    </div>
  );
}

export default Controller;
```

---

# JSX vs HTML

| HTML | JSX (React) |
|------|-------------|
| `class` | `className` |
| `onclick` | `onClick` |
| `for` | `htmlFor` |
| Multiple root elements allowed | One parent element required |

---
