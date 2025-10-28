- ID :TC-01
- Title:Login
- Preconditions: Site reachable ,user name and password
- Steps:

  1.  Go to https://www.saucedemo.com/v1/
  2.  enter the user name standard_user
  3.  enter the password secret_sauce
  4.  click the login button

- Expected:
  User lands on Products page (URL contains /inventory.html), product list visible
- Actual:
  The user login in and see the Products page
- Status: Psss
- Suite Type: functional and secirty

---

- ID :TC-02
- Title:Login - Invalid creds
- Preconditions: Site reachable, user name and password not in the list
- Steps:

  1.  Go to https://www.saucedemo.com/v1/
  2.  enter the user name Hadeel
  3.  enter the password Hadeel123
  4.  click the login button

- Expected:
  faild to login
- Actual:
  Epic sadface: Username and password do not match any user in this service
- Status:pass
- Suite Type: functional and secirty
- Notes: show error massage

---

- ID :TC-03
- Title:Login - Locked out user
- Preconditions:Site reachable, user name and password
- Steps:

  1.  Go to https://www.saucedemo.com/v1/
  2.  enter the user name locked_out_user
  3.  enter the password secret_sauce
  4.  click the login button

- Expected:
  Error message shown about user being locked out
- Actual:
  Epic sadface: Sorry, this user has been locked out.
- Status:Pass
- Suite Type: functional and secirty
- Notes:

---

- ID :TC-04
- Title: Login - problem user
- Preconditions:Site reachable ,user name and password
- Steps:

  1.  Go to https://www.saucedemo.com/v1/
  2.  enter the user name problem_user
  3.  enter the password secret_sauce
  4.  click the login button

- Expected:
  Observe UI anomalies (images broken or slow loads) — detect differing behaviour
- Actual:
  The user successfully login but it show problem in the Products items page
- Status:pass
- Suite Type: functional
- Notes:

---

- ID :TC-05
- Title:Add to cart & Cart count
- Preconditions:Logged in
- Steps:

  1.  Click "Add to cart" on first product
  2.  Observe cart badge

- Expected:
  Badge increments to 1 and cart contains the item
- Actual: the items add to cart successfully and the cart badge increment
- Status:Pass
- Suite Type: Functional
- Notes:

---

- ID :TC-06
- Title:Remove from cart
- Preconditions: Login , Item in cart
- Steps:

  1.  Open Cart
  2.  Click Remove on item
      or click in remove that show in the item card

- Expected:
  Item removed, badge decrements
- Actual: the items removed and badge decrements
- Status:Pass
- Suite Type: Functional
- Notes:

---

- ID :TC-07
- Title: Product Sorting - Name A→Z
- Preconditions:Logged in
- Steps:

  1.  login
  2.  On Products page,
  3.  open Sort dropdown
  4.  Select "Name (Z to A)"

- Expected:
  Products sorted alphabetically in descending order.
- Actual:
  The Products sorted successfully from z to A fist shoe the T the S
- Status:Pass
- Suite Type: Functional
- Notes:

---

- ID :TC-08
- Title: Product Sorting - Price Low→High
- Preconditions: Logged in
- Steps:

  1.  login
  2.  On Products page,
  3.  open Sort dropdown
  4.  Select "Name (A to Z)"

- Expected:
  Products sorted alphabetically ascending
- Actual:
  Products sorted from A to Z
- Status:Pass
- Suite Type:
  Functional
- Notes:
  do fisrt TC-07 then TC-08 , its the defalut

---

- ID :TC-09
- Title: Product Sorting - Price Low→High
- Preconditions:Logged in
- Steps:

  1.  login
  2.  On Products page,
  3.  open Sort dropdown
  4.  Select "Price (low to high)"

- Expected:
  Products sorted by price ascending
- Actual:
  The low Price items show first
- Status:Pass
- Suite Type: Functional
- Notes:

---

- ID :TC-10
- Title: Responsive: Mobile viewport product grid
- Preconditions: Logged in
- Steps:

  1.  mulate mobile viewport (360x800)
  2.  Load Products page

- Expected:
  Product grid stacks appropriately, buttons visible and tappable
- Actual:Optimize page for mobile — scale down and preserve UI/UX
- Status:Pass
- Suite Type: Responsive
- Notes:

---

- ID :TC-11
- Title: Checkout - Missing First Name required fields
- Preconditions: Login , Items in cart
- Steps:

  1.  login
  2.  On Products page, click on cart items
  3.  click in Checkout buttom
  4.  Leave fields empty,
  5.  click Continue

- Expected:
  Form validation errors shown, cannot proceed
- Actual:
  First Name is required
- Status:Pass

- Notes:

---
