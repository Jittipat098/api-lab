# api-lab
API Testing with pytest and requests
18
Step 0.3, status code of the request without a token: 401

## Part A: Input Space Partitioning for Ratings

#### Step A1–A2: Input Domain Model and Base Choice Coverage

API under test: `POST /api/ratings`

| Characteristic | Block | Test name |
|---|---|---|
| C1: Value of stars | Below 1 (0) | `test_stars_out_of_range[0]` |
| C1: Value of stars | 1 to 5 (Base: 3) | `test_base_choice_is_saved` |
| C1: Value of stars | Above 5 (6) | `test_stars_out_of_range[6]` |
| C2: Type of stars | Whole number (Base: 3) | `test_base_choice_is_saved` |
| C2: Type of stars | Decimal (3.5) | `test_decimal_stars_are_refused` |
| C2: Type of stars | Text ("3") | `test_text_stars_are_refused` |
| C2: Type of stars | Missing | `test_missing_stars_are_refused` |
| C3: Pizza | Exists (Base) | `test_base_choice_is_saved` |
| C3: Pizza | Does not exist (999999999) | `test_nonexistent_pizza_is_refused` |
| C4: Token | User's own token (Base) | `test_base_choice_is_saved` |
| C4: Token | Missing | `test_missing_token_is_refused` |
| C4: Token | Wrong length | `test_short_token_is_refused` |

**Input rules:**
- `stars` must be an integer between 1 and 5 inclusive.
- `pizza_id` must refer to an existing pizza.
- The Authorization token must belong to the logged-in user.

**A2 result:** 9 tests passed.
