"""Code Generation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_from_spec():
    """Test Generate full module from a technical specification."""
    tools = AgentTools()
    result = await tools.generate_from_spec(specification="test", target_stack="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_api_endpoint():
    """Test Generate a complete API endpoint with validation, service, and tests."""
    tools = AgentTools()
    result = await tools.generate_api_endpoint(endpoint_spec="test", framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_database_schema():
    """Test Generate database migration and ORM models from entity description."""
    tools = AgentTools()
    result = await tools.generate_database_schema(entities="test", orm="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_crud():
    """Test Generate full CRUD operations for an entity."""
    tools = AgentTools()
    result = await tools.generate_crud(entity_name="test", fields="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.code_generation_agent_agent import CodeGenerationAgentAgent
    agent = CodeGenerationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
