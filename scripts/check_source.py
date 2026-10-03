#!/usr/bin/env python3
"""Hardware-free checks for the archived ROS 2 workspace (stdlib only)."""
from pathlib import Path
import ast
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
workspace = ROOT / "project3-team3_workspace" / "src"
expected = (
    workspace / "control_pkg" / "setup.py",
    workspace / "perception_pkg" / "setup.py",
    ROOT / "myarm_workspace" / "joint_tcp_server.py",
    ROOT / "myarm_workspace" / "suction_tcp_server.py",
    ROOT / "docs" / "Project_Report.pdf",
)
errors = []
for p in expected:
    if not p.is_file():
        errors.append(f"Missing file: {p.relative_to(ROOT)}")
pyfiles = sorted([*workspace.rglob("*.py"), *(ROOT / "myarm_workspace").glob("*.py")])
for path in pyfiles:
    try:
        compile(path.read_text(encoding="utf-8"), str(path), "exec")
    except (SyntaxError, UnicodeDecodeError) as exc:
        errors.append(f"Python parse failed: {path.relative_to(ROOT)}: {exc}")
for path in workspace.rglob("package.xml"):
    try:
        ET.parse(path)
    except ET.ParseError as exc:
        errors.append(f"Package XML parse failed: {path.relative_to(ROOT)}: {exc}")
for package in ("control_pkg", "perception_pkg"):
    setup = workspace / package / "setup.py"
    if not setup.is_file():
        continue
    text = setup.read_text(encoding="utf-8")
    for entrypoint in re.findall(r"[\w_]+\s*=\s*" + package + r"\.(\w+):main", text):
        target = workspace / package / package / f"{entrypoint}.py"
        if not target.is_file():
            errors.append(f"Entry point module not found: {target.relative_to(ROOT)}")
if errors:
    print("CHECK FAILED")
    for item in errors:
        print(" -", item)
    sys.exit(1)
print(f"CHECK OK: {len(pyfiles)} Python sources parsed; package XML and entry points inspected.")
