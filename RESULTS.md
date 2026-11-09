## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: An Old Calzone

## Step 0.12: Login without a Session

Test: `test_log_in_without_a_session`

| Run | Result | HTTP Status |
|---|---|---|
| 1 | FAILED | 401 |
| 2 | FAILED | 401 |
| 3 | FAILED | 401 |

**Conclusion:**

All three attempts successfully created a user (HTTP 201), but login failed with HTTP 401 because separate requests did not share session cookies. This demonstrates why using a persistent requests.Session is important when working with the API behind a load balancer.

## Step 0.16: Bug hunt checkpoint

- Blocks tested for the number of excluded tools:
  - 0 tools excluded: PASSED
  - 1 tool excluded: PASSED
  - 2 tools excluded: PASSED
  - 3 tools excluded: XFAIL

## Defect report

- **Title:** Excluding all three pizza tools returns HTTP 500.
- **Request:** POST `/api/pizza` with `excludedTools` set to `["Knife", "Pizza cutter", "Scissors"]`.
- **Expected result:** HTTP 400 Bad Request with a JSON error message explaining that no tool is available.
- **Actual result:** HTTP 500 Internal Server Error. The response body is empty.
- **Severity:** High (suggested). The API returns an unexpected server error for an input it should handle gracefully.
- **Test:** `test_all_tools_excluded_returns_bad_request`
- **Status:** XFAIL (known defect).

### Part A4: Rating Ownership Tests

Tested whether a different authenticated user can access a rating created by its owner.

| Test | Actual HTTP Status | Result |
|---|---:|---|
| Read another user's rating | 404 | Passed |
| Update another user's rating | 400 | Passed |
| Delete another user's rating | 400 | Passed |

**Conclusion:** A different authenticated user cannot read, update, or delete the rating. All three ownership tests passed.


### Part A4: Rating Ownership

Tested whether a different authenticated user could access
another user's rating.

| Action | HTTP Status | Result |
|---|---:|---|
| Read another user's rating | 404 | Rejected |
| Update another user's rating | 400 | Rejected |
| Delete another user's rating | 400 | Rejected |

All three ownership tests passed.

**7. What happens when using the made-up token? Is this a defect?**

The request returned **HTTP 200 OK** and a JSON response containing a list of ratings, even though the token was made up.

Yes, this is a security defect. The API appears to accept an invalid token and allows access to rating data without proper authentication. On a real system, an unauthorized person could potentially access data they should not be allowed to see. This is an authentication or access-control issue.

The fake token was used only for a GET request. No data was created, changed, or deleted.

## Part B: Reflection Questions

**1. What can real API tests find that unit tests with stubs cannot? Why are unit tests with stubs still useful?**

Real API tests can find integration problems, network issues, authentication problems, and errors in communication with the actual server. Unit tests with stubs are still useful because they are faster, easier to control, and help test individual functions without depending on an external server.

**2. Why does every test create its own user with a new name rather than use the public token? How will you apply the same idea to Project 2?**

Each test creates its own user to avoid sharing data, interfering with other tests, or depending on a public account. In Project 2, I would create a separate test account and unique test data for each test, then clean up the data when possible.

**3. Why do the tests send every request through one session? What happened in the three Step 0.12 runs?**

A single session preserves cookies between requests. This helps maintain the same session and allows requests to reach the same backend instance when session persistence is required. In Step 0.12, all three runs failed during login with HTTP 401 because the requests did not maintain the required session.

**4. Which excluded-tools block revealed the defect? Why is HTTP 500 with an empty body worse than HTTP 400 with a message? Why keep the test as xfail?**

The block that excluded all three tools (Knife, Pizza cutter, and Scissors) revealed the defect. The expected response was HTTP 400 with a JSON error message, but the actual response was HTTP 500 with an empty body. A 500 indicates a server error and provides no useful explanation for the API client. The test remains marked as xfail to document the known defect and detect when it is fixed.

**5. How many tests are needed for base choice coverage and all combinations coverage? Show the calculation.**

Base choice coverage needs 9 tests:
- 1 base test
- C1 has 3 blocks, so 2 additional tests.
- C2 has 4 blocks, so 3 additional tests.
- C3 has 2 blocks, so 1 additional test.
- C4 has 3 blocks, so 2 additional tests.

Total: 1 + 2 + 3 + 1 + 2 = **9 tests**.

All combinations coverage needs 3 × 4 × 2 × 3 = **72 tests**.

**6. Which status codes did you get when another user read, changed, and deleted the rating? Which codes would you expect? Is the difference a defect?**

The actual status codes were:
- Read: HTTP 404
- Update: HTTP 400
- Delete: HTTP 400

I expected all operations to be rejected with a 4xx client error because the rating belongs to another user. These responses do not necessarily indicate a defect because the API can use different 4xx status codes to reject unauthorized access. The important point is that the other user could not access or modify the rating.

**7. What happened when using the made-up token? Is this a defect, and what could a stranger do with it on a real system?**

The request returned HTTP 200 OK and a JSON response containing a list of ratings, even though the token was made up.

Yes, this is a security defect. The API appears to accept an invalid token and allows access to rating data without proper authentication. On a real system, an unauthorized person could potentially access data they should not be allowed to see.

The fake token was used only for a GET request. No data was created, changed, or deleted.

**8. Name one thing an API test checks better than a test through web pages, and one thing only a test through web pages can check.**

An API test is better for checking HTTP status codes, JSON responses, authentication, and input validation directly. A web page test can check visual appearance, layout, navigation, and user interaction in a browser.
