# Mini Test plan - saucedemo

**scope:**

- Target app: Sauce Demo (single-page demo online shopping)
- Analysis Type:
  -- Main Pages : login , Products and Cart pages
  -- Navigation : all items , about , logout , reset app state

- Key Features:
  for a standard user: auth, product browsing, sorting, filtering (sort dropdown), add/remove cart, checkout (happy path and basic negative cases), and order completion confirmation.

- Environments:
  https://www.saucedemo.com/v1/ (desktop primary with Microsoft edget), responsive/mobile
  viewport.

  https://www.saucedemo.com/ (desktop primary with Google Chrome ), responsive/mobile
  viewport.

**out of scope**
Payment gateway integrations (no real payments on demo site).
Internationalization implementation (site is LTR English-only).

**key risks**

1. Authentication failures due to locked/invalid test accounts.
2. Checkout form validation.
3. when the user add the items to cart , does not show thw image for the prodect

**note** the user can not registering (sign up)

**test data**

- Standard test user (provided by site):
  -- username: standard_user
  -- password: secret_sauce

- Locked user: locked_out_user / secret_sauce
- Problem user: problem_user / secret_sauce (site-specific behaviour different items with the same images )
- Performance test: add max items then navigate / refresh.

**entry criteria**
App reachable at https://www.saucedemo.com/v1/
Test accounts work (sanity login succeeds for standard_user).

**exit criteria**
All critical and high severity bugs fixed or mitigated.

**Expected RTL risks (Arabic/Hebrew)**

- Even though Sauce Demo is an LTR demo, below are concrete RTL risk points observed on the UI elements inspected that would likely break when localized to Arabic/Hebrew:

- Header & nav items (top-left logo, menu) — fixed LTR spacing; in RTL the logo may collide with nav items and expected left/right paddings won't flip.

- Product grid cards — image alignment, price and Add to cart button placement assume LTR; caret/chevron icons near the product title would need mirroring.

- Sort dropdown ("Name (A to Z)") — dropdown arrow and selected item alignment may remain left-aligned; caret might not mirror and reading order will be wrong.

- Form input validation messages (Checkout: First/Last) — messages appear left of inputs or anchored to LTR flows; in RTL they must be right-aligned and not overlap icons.
