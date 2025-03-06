import pytest
from rogue.pandas.groupby.solution import groupby


@pytest.mark.parametrize(
    "csv_string, result",
    [
        (
            """country,department,num_worker\nUS,DOJ,60\nJP,BOJ,60\nUS,CB,70\nGB,CB,60""",
            "US: 130",
        ),
    ],
)
def test_groupby(csv_string, result):
    assert groupby(csv_string) == result
