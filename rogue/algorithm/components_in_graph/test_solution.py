import pytest
from rogue.algorithm.components_in_graph.solution import components_in_graph


@pytest.mark.parametrize(
    "queries, result",
    [
        ([[1, 6], [2, 7], [3, 8], [4, 9], [2, 6]], [2, 4]),
    ],
)
def test_components_in_graph(queries, result):
    assert components_in_graph(queries) == result
