# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module libranet_django.__init__."""
import packaging.version


def test_version() -> None:
    from libranet_django import __version__

    assert isinstance(__version__, str)
    assert packaging.version.parse(__version__) >= packaging.version.parse("0.0")


# def test_copyright() -> None:
#     from libranet_django import __copyright__

#     assert isinstance(__copyright__, str)
#     assert "Copyright" in __copyright__


def test_license() -> None:
    import libranet_django
    # from libranet_django import __license__

    assert isinstance(libranet_django.__license__, str)
    assert "MIT" in libranet_django.__license__
