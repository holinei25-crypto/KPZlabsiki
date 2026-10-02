import pytest
from validator import validate_brackets

def test_valid_string():
    assert validate_brackets("<div><p>{ test }</p></div>") is True

def test_unbalanced_brackets():
    with pytest.raises(ValueError) as exc_info:
        validate_brackets("<div><p>{ test }}</p></div>")
    assert "Дужки незбалансовані на позиціях" in str(exc_info.value)
