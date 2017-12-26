import asyncio
import pytest

from scope.main import main


@pytest.mark.asyncio
async def test_examples(event_loop):
    assert event_loop.is_running()
