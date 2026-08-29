import pytest

def test_app_import():
    """Basic smoke test to ensure the app can be imported."""
    try:
        import app
        assert True
    except Exception as e:
        pytest.fail(f"App import failed: {e}")

def test_basic_functionality():
    """Basic test to ensure the app runs without crashing."""
    # Since app.py currently only has print statements, 
    # this just verifies it doesn't throw an error on execution.
    import subprocess
    result = subprocess.run(['python', 'app.py'], capture_output=True, text=True)
    assert result.returncode == 0
