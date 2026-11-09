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