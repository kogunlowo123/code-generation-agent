"""Test configuration for Code Generation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "code-generation-agent", "category": "Software Engineering"}
