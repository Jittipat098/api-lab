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