import sys
from pathlib import Path

# Add repo root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from legacy.legacy_script import run

def test_current_behavior():
    data = [5, 12, 20]
    result = run(data)
    assert result == 39.7

