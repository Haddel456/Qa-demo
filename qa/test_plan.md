# Mini Test plan - saucedemo

**scope:**
Target app: Sauce Demo (single-page demo online shopping)

Analysis Type:
Main Pages : login , Products and Cart pages
Navigation : all items , about , logout , reset app state

Key Features:
for a standard user: auth, product browsing, sorting, filtering (sort dropdown), add/remove cart, checkout (happy path and basic negative cases), and order completion confirmation.

Environments:
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

Standard test user (provided by site):
username: standard_user
password: secret_sauce

Locked user: locked_out_user / secret_sauce

Problem user: problem_user / secret_sauce (site-specific behaviour different items with the same images )

Performance test: add max items then navigate / refresh.

**entry criteria**
App reachable at https://www.saucedemo.com/v1/
Test accounts work (sanity login succeeds for standard_user).

**exit criteria**
All critical and high severity bugs fixed or mitigated.
