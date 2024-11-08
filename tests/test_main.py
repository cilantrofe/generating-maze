from src.main import main
from unittest.mock import patch


@patch("builtins.input", side_effect=["5", "5", "1", "1 1", "3 3", "1"])
def test_main(mock_input) -> None:
    main()
