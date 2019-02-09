import ksp_sample as proj_to_test
import pytest


def test_version_exists():
    assert hasattr(proj_to_test, "__version__")


def test_version_pattern():
    assert isinstance(proj_to_test.__version__, str)
    assert "." in proj_to_test.__version__
    parts = proj_to_test.__version__.split(".")
    for cur_part in parts:
        assert cur_part.isdigit()


if __name__ == "__main__":
    pytest.main([__file__, '-v', '-s'])

