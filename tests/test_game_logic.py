from logic_utils import check_guess, parse_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    result, message = check_guess(60, 50)
    assert result == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    result, message = check_guess(40, 50)
    assert result == "Too Low"
    assert "HIGHER" in message