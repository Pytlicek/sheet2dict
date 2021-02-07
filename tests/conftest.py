import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(".").absolute().parent))

from sheet2dict import Worksheet


@pytest.fixture(scope="module")
def worksheet():
    return Worksheet()
