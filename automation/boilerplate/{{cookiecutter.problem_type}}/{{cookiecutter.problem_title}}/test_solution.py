import pytest
from rogue.{{cookiecutter.problem_type}}.{{cookiecutter.problem_title}}.solution import {{cookiecutter.problem_title}}


@pytest.mark.parametrize(
    "input1, input2,... result",
    [
        (#input1, #input2,... #result),
    ],
)
def test_{{cookiecutter.problem_title}}(input1, input2,... result):
    assert {{cookiecutter.problem_title}}(input1, input2...) == result
