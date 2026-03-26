# Design System Document: The Architectural Editorial

## 1. Overview & Creative North Star
**Creative North Star: "The Digital Estate"**

This design system rejects the cluttered, "utility-first" look of traditional real estate portals. Instead, it adopts a **High-End Editorial** approach, treating property listings like features in a luxury architectural magazine. We move beyond "trustworthy blue boxes" by utilizing **intentional asymmetry**, **layered depth**, and **dramatic typographic scales**.

The goal is to evoke a sense of "Established Modernity." We achieve this through "The Breathing Layout"—using expansive white space (the 16 and 20 spacing tokens) to let high-resolution photography dominate, while UI elements act as sophisticated, quiet anchors rather than loud distractions.

---

## 2. Colors & Tonal Depth
Our palette is anchored in a commanding `primary` (#00236f) and a vibrant, life-affirming `secondary` (#006c49). However, the "luxury" feel is created in the neutrals.

### The "No-Line" Rule
**Strict Mandate:** Designers are prohibited from using 1px solid borders to section off content. Boundaries must be defined solely through:
1.  **Background Shifts:** Place a `surface-container-low` section against a `surface` background.
2.  **Tonal Transitions:** Use a soft gradient from `surface-container-lowest` to `surface-container` to define the end of a hero area.

### Surface Hierarchy & Nesting
Treat the UI as a series of stacked, physical materials.
*   **Base:** `surface` (#f7f9fb) for the main page body.
*   **The Content Bed:** `surface-container-low` (#f2f4f6) for large section backgrounds (e.g., the search filter tray).
*   **The Elevated Card:** `surface-container-lowest` (#ffffff) for property cards and interactive modals. This creates a "natural lift" without heavy shadows.

### The "Glass & Gradient" Rule
To avoid a flat, "Bootstrap" appearance:
*   **Glassmorphism:** Navigation bars and floating action headers must use `surface_bright` at 80% opacity with a `backdrop-blur` of 12px.
*   **Signature Gradients:** Main CTAs should utilize a subtle linear gradient from `primary` (#00236f) to `primary_container` (#1e3a8a) at a 135-degree angle. This adds "soul" and a tactile, premium finish.

---

## 3. Typography: The Editorial Voice
We use a dual-font system to balance authority with modern utility.

*   **Display & Headlines (Manrope):** This is our "Editorial Voice." High-contrast, wide-tracking, and bold. Use `display-lg` for hero statements to command attention.
*   **Interface & Body (Inter):** Our "Utility Voice." Inter provides maximum readability for technical data, contract text, and property specs.

**Hierarchy Tip:** Always pair a `headline-sm` (Manrope) for property titles with a `label-md` (Inter) in `on_surface_variant` (#444651) for the address to create a clear "Title vs. Metadata" distinction.

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are often "dirty." We use light and tone to imply height.

*   **The Layering Principle:** Instead of a shadow, place a `surface-container-lowest` object inside a `surface-container-high` wrapper. The delta in luminance creates an organic edge.
*   **Ambient Shadows:** For floating elements (Search Bars, Property Hovers), use a custom shadow: `0px 20px 40px rgba(25, 28, 30, 0.06)`. Note the extremely low opacity; it should feel like ambient room light, not a dark glow.
*   **The "Ghost Border" Fallback:** If a border is required for accessibility (e.g., form inputs), use the `outline_variant` token at **20% opacity**. Never use a 100% opaque border.
*   **Glassmorphism:** Use `surface_variant` with 40% opacity for secondary floating chips (like "Luxury" or "New Construction" badges) to let the property imagery "bleed" through the UI.

---

## 5. Components

### Cards & Listings
*   **Standard:** Use `surface-container-lowest`. **Do not use dividers.** 
*   **Separation:** Use the `3` (1rem) spacing token to separate image, title, and price metadata. 
*   **Hover State:** Shift background from `surface-container-lowest` to `surface-bright` and apply the Ambient Shadow.

### Buttons
*   **Primary:** Gradient of `primary` to `primary_container`. Corner radius: `md` (0.375rem).
*   **Secondary (Action/Available):** Solid `secondary` (#006c49). Use for "Schedule Tour" or "Available" status indicators.
*   **Tertiary:** No background. Use `on_surface` text with a subtle `primary` underline on hover.

### Input Fields & Search Filters
*   **Search Bar:** Use `full` (9999px) roundedness. Background: `surface-container-lowest`. 
*   **States:** On focus, transition the `outline` token to `primary` at 40% opacity—never a harsh 100% blue box.

### Professional Document Styling
*   **Contracts:** Use `surface-container-lowest` as the "paper." 
*   **Typography:** Strict adherence to `body-md` for legibility. 
*   **Accents:** Use `secondary_container` for highlighted clauses or signed areas to provide a "friendly/safe" emerald green signal.

### Property Badges (Custom Component)
*   Small chips using `secondary_fixed` (#6ffbbe) with `on_secondary_fixed` (#002113) text for "For Rent" status. These should feel like premium labels on a luxury garment.

---

## 6. Do's and Don'ts

### Do:
*   **Do** use asymmetrical margins. For example, a property description might be offset by the `12` (4rem) spacing token from the left to create an editorial "white space lung."
*   **Do** use `surface_dim` for footer backgrounds to ground the page with a sense of weight.
*   **Do** use large image ratios (16:9 or 4:3) to emphasize the architectural nature of the marketplace.

### Don't:
*   **Don't** use 1px solid lines for dividers. Use a `1px` height `surface-variant` block with 30% opacity if absolutely necessary.
*   **Don't** use "pure black" (#000000) for text. Always use `on_surface` (#191c1e) to keep the aesthetic professional and soft.
*   **Don't** cram content. If a section feels tight, double the spacing token (e.g., move from `6` to `12`).