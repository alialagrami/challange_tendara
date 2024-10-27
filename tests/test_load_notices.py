from tendara_ai_challenge.matching.utils import load_notices

def test_load_notices():
    """Test that all notices are loaded correctly from the actual JSON file."""
    notices = load_notices()
    
    # Verify we have the expected number of notices
    assert len(notices) == 100