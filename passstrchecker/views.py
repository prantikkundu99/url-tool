from django.shortcuts import render
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def check_password_strength(password):
    score = 0

    # Length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Character Types
    if any(c in ascii_lowercase for c in password):
        score += 1

    if any(c in ascii_uppercase for c in password):
        score += 1

    if any(c in digits for c in password):
        score += 1

    if any(c in punctuation for c in password):
        score += 1

    # Decide Strength
    if len(password) < 4:
        return (
            "Very Weak",
            "Your password is too short. Use at least 8 characters."
        )

    elif score <= 2:
        return (
            "Weak",
            "Try adding uppercase letters, numbers, and special characters."
        )

    elif score == 3:
        return (
            "Moderate",
            "Good start! Increase the length or add more character types."
        )

    elif score in (4, 5):
        return (
            "Strong",
            "Your password is strong. A few more characters can make it even stronger."
        )

    else:
        return (
            "Very Strong",
            "Excellent! Your password is long and contains a good mix of uppercase, lowercase, numbers, and special characters."
        )
 


def passstrchecker(request):
    data = {
        "password": "",
        "strength": "",
        "message": "",
        "has_lower": False,
        "has_upper": False,
        "has_digit": False,
        "has_symbol": False,
    }

    if request.method == "POST":
        password = request.POST.get("password", "")

        strength, message = check_password_strength(password)

        has_lower = any(c in ascii_lowercase for c in password)
        has_upper = any(c in ascii_uppercase for c in password)
        has_digit = any(c in digits for c in password)
        has_symbol = any(c in punctuation for c in password)

        data.update({
            "password": password,
            "strength": strength,
            "message": message,
            "has_lower": has_lower,
            "has_upper": has_upper,
            "has_digit": has_digit,
            "has_symbol": has_symbol,
        })

    return render(
        request,
        "passstrchecker.html",
        data)