# # Example function to be tested
# def calculate_discount(price, discount):
#     """
#     Calculate the final price after applying a percentage discount.
#     """
#     return price - (price * (discount / 100))

# # Functional Test
# def test_functional_discount():
#     """
#     Functional Test: Validate the calculate_discount function with correct inputs.
#     """
#     result = calculate_discount(100, 10)
#     assert result == 90, f"Expected 90, got {result}"

# # Regression Test
# def test_regression_discount():
#     """
#     Regression Test: Ensure the function behaves correctly with old inputs.
#     """
#     test_cases = [
#         (100, 10, 90),  # Old case 1
#         (200, 25, 150), # Old case 2
#         (50, 20, 40),   # Old case 3
#     ]

#     for price, discount, expected in test_cases:
#         result = calculate_discount(price, discount)
#         assert result == expected, f"Expected {expected}, got {result}"
