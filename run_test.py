import subprocess

steps = ["step2", "step5", "step6"]

for step in steps:
    print(f"\n=== RUNNING {step.upper()} ===")
    subprocess.run(
        ["python", f"tests/test_{step}.py"],
        check=False
    )

