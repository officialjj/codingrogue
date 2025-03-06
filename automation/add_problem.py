from cookiecutter.main import cookiecutter
import argparse
from pathlib import Path


def run():
    """
    Create template code from boilerplate code.
    """
    parser = argparse.ArgumentParser(
        description="add a new problem"
    )
    parser.add_argument("--problem_title", "-ptitle", type=str, help="A unique problem title.")
    parser.add_argument("--problem_type", "-ptype", type=str, help="The type of problem.", choices=["algorithm", "data"])
    pa = parser.parse_args()

    template_path = (
        Path(__file__).parent
        / "boilerplate"
    )
    output_dir = Path(__file__).parent.parent / "rogue"

    context = {
        "problem_type": pa.problem_type,
        "problem_title": pa.problem_title,
    }

    cookiecutter(
        template=str(template_path),
        output_dir=str(output_dir),
        extra_context=context,
        no_input=True,
        overwrite_if_exists=True,
    )


if __name__ == "__main__":
    run()
