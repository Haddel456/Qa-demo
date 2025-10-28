# BUG-05 — Broken Product Images for problem_user

- Title: Product images fail to load for problem_user account

- Environment: https://www.saucedemo.com/ — Chrome on Windows 11

- Environment: https://www.saucedemo.com/v1/ — Microsoft Edget on Windows 11

**Steps to Reproduce:**

1. Go to the Sauce Demo Login Page.
2. Log in using the credentials:
   Username: problem_user
   Password: secret_sauce
3. Observe the product listing page after login.
   in https://www.saucedemo.com/ show dog image for all items

   in https://www.saucedemo.com/v1 show broken image

**Expected Result:**

All product images should display correctly for every logged-in user.

**Actual Result:**
Several product images are missing or broken (showing broken image icons instead of product photos).

in https://www.saucedemo.com/ show dog image for all items

in https://www.saucedemo.com/v1 show broken image

**Severity:**
High (Functional / UI) – Product images are critical for usability and user confidence in online shopping. Missing images may reduce trust and cause confusion.

**Suspected Area:**
Incorrect image file path or conditional loading based on user type in front-end logic (inventory_item_image component).

**Evidence:**
Screenshot: (Screenshot 2025-10-28 112642.png)
Screenshot: (Screenshot 2025-10-28 112701.png)
