# BUG-01 — Locked user login message unclear

- Title: Locked out user shows generic error without suggested next steps

- Environment: https://www.saucedemo.com/ — Chrome on Windows 11

- Environment: https://www.saucedemo.com/v1/ — Microsoft Edget on Windows 11

**Steps to Reproduce:**

1. Go to login page.
2. Enter username locked_out_user and password secret_sauce.
3. Click Login.

**Expected Result:**
Clear message: "Epic sadface: Sorry, this user has been locked out." with distinctive UI.

**Actual Result:**
Generic error message shown: "Epic sadface: Sorry, this user has been locked out." — message is terse and lacks remediation.

**Severity:**
(Medium to Hight )

**Suspected Area:**
Authentication error messaging / UI text.

**Evidence:**
Screenshot: (Screenshot 2025-10-28 105527.png)
