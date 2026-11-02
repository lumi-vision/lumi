"""Check the repository layout only; does not process video."""
import json
from pathlib import Path
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    errors = []
    if sys.version_info < (3, 10):
        errors.append("Python 3.10 or newer is required.")
    for folder in ("src/lumi", "configs", "scripts", "tests", "experiments",
                   "docs", "data", "models", "outputs"):
        if not (root / folder).is_dir():
            errors.append(f"Missing directory: {folder}")
    try:
        config = json.loads((root / "configs/example.json").read_text(encoding="utf-8"))
        if not isinstance(config, dict):
            errors.append("Example configuration must be a JSON object.")
        else:
            for key in ("input_video", "model_path", "output_dir"):
                if key not in config:
                    errors.append(f"Missing configuration key: {key}")
    except (OSError, ValueError) as error:
        errors.append(f"Cannot read example configuration: {error}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("OK: repository layout and example configuration are ready.")
    print("Video processing and model training are not implemented in this scaffold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
