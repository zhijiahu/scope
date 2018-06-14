import asyncio
import pytest

from scope.monitor import Monitor


@pytest.mark.asyncio
async def test_examples():
    monitor = Monitor('examples', 3)
    await monitor.start()
