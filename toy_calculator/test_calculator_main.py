import os
import runpy


def test_script_main_outputs(capsys):
    script_path = os.path.join(os.path.dirname(__file__), "calculator.py")

    runpy.run_path(script_path, run_name="__main__")

    out = capsys.readouterr().out

    assert "🧮 Calculator Demo" in out
    assert "==============================" in out  # 30 '=' characters
    assert "5 + 3 = 8" in out
    assert "10 - 4 = 6" in out
    assert "6 × 7 = 42" in out
    assert "15 ÷ 3 = 5.0" in out
    assert "Error: Cannot divide by zero" in out
    assert "Calculator functions are ready to use" in out
