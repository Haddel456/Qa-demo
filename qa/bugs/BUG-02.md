# BUG-02 — Image Missing in Cart

- Title: Items added to the cart do not display product images

- Environment: https://www.saucedemo.com/ — Chrome on Windows 11

- Environment: https://www.saucedemo.com/v1/ — Microsoft Edget on Windows 11

**Steps to Reproduce:**

1. Go to the Sauce Demo Login Page.
2. Log in using valid credentials (e.g., standard_user / secret_sauce).
3. Add any product (e.g., “Sauce Labs Backpack”) to the cart.
4. Click the Cart icon in the top-right corner.
   Observe the cart page.

**Expected Result:**
Each product listed in the cart should display its image alongside the product name, price, and quantity.

**Actual Result:**
The product image is missing — only the product name and price appear and insted of the image it show the number

**Severity:**
High (UI / Functional) – Users rely on images for visual confirmation of their selected products. Missing images can cause confusion or incorrect orders.

**Suspected Area:**
Frontend rendering issue in the cart page component (cart_item.html or corresponding React template). Possibly missing or incorrect img source binding ot did not think to show image.

**Evidence:**
Screenshot (2025-10-28 111258.png)
