def is_leap_year(year):
    # Step 1: Check if it's divisible by 4
    if year % 4 == 0:
        # Step 2: Check if it's divisible by 100
        if year % 100 == 0:
            # Step 3: Check if it's divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Testing the function (Hard-coded values)
print(is_leap_year(2000)) # Should return True
print(is_leap_year(2100)) # Should return False
print(is_leap_year(2024)) # Should return True