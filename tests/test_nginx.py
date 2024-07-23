"""Test ngnix reloading.

This has two underscores due to test pollution that I can't figure out...
"""

import logging

import pytest

from allowlistapp import create_app


def test_nginx_reload(tmp_path, get_test_config, caplog: pytest.LogCaptureFixture):
    """Unit test _warn_unexpected_keys."""
    with caplog.at_level(logging.INFO):
        create_app(get_test_config("valid_nginx.toml"), tmp_path)
        assert "Couldn't restart nginx" in caplog.text
