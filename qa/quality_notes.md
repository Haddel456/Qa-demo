# Perf / Accessibility Quick Notes

**Limited Product Quantity**

- Observation: Users can only add one item per product; no quantity selector is available.
- Possible Fix: Add a quantity input or increment/decrement buttons for each product in the cart.

**Outdated UX/UI in Microsoft Edge (non-V version)**

- Observation: Cart and product pages in https://www.saucedemo.com/
  look outdated and misaligned in Microsoft Edge compared to the modern /v1/ version.

- Possible Fix: Update CSS and frontend styling in Edge to match /v1/ layout and UX.

Missing Product Images for problem_user

- Observation: Some product images fail to load, especially for problem_user.
- Possible Fix: Check image paths and conditional rendering logic in frontend code; ensure all images have valid sources.

**Accessibility Gaps for Users with Special Needs**

- Observation: The website does not provide features for users with visual or hearing difficulties:
  -- No option to enlarge fonts
  -- No high-contrast mode
  -- No support for screen readers or audio cues
- Possible Fix: Implement accessibility features such as adjustable font sizes, high-contrast mode, and proper ARIA support to comply with accessibility standards.
