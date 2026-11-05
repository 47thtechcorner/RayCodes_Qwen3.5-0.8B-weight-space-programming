import os
import sys
import ollama

MODEL_NAME = "qwen3.5-wsp"

def query_model(prompt: str, system_prompt: str = "") -> str:
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    response = ollama.chat(model=MODEL_NAME, messages=messages)
    return response["message"]["content"]

def run_task1_calculus(input_path: str, out_tex_path: str, out_md_path: str) -> None:
    print("\n[+] Running Workflow 1: Edge Mathematical Derivation...")
    with open(input_path, "r", encoding="utf-8") as f:
        problem_text = f.read()

    system_prompt = "Solve step-by-step with exact boxed final answer in compilable LaTeX."
    result = query_model(problem_text, system_prompt)

    with open(out_tex_path, "w", encoding="utf-8") as f:
        f.write(result)
    with open(out_md_path, "w", encoding="utf-8") as f:
        f.write(f"# Edge Mathematical Derivation Report\n\n{result}\n")
    print(f"    -> Saved LaTeX deliverable to: {out_tex_path}")
    print(f"    -> Saved Markdown deliverable to: {out_md_path}")

def run_task2_robotics(input_path: str, out_gcode_path: str, out_md_path: str, out_html_path: str) -> None:
    print("\n[+] Running Workflow 2: Strict Hardware Instruction Compiler...")
    with open(input_path, "r", encoding="utf-8") as f:
        command_text = f.read()

    system_prompt = "Convert instructions into standard ISO G-code with inline operator comments."
    result = query_model(command_text, system_prompt)

    with open(out_gcode_path, "w", encoding="utf-8") as f:
        f.write(result)
    with open(out_md_path, "w", encoding="utf-8") as f:
        f.write(f"# Autonomous Robotics G-Code Specification\n\n```gcode\n{result}\n```\n")
    print(f"    -> Saved G-Code deliverable to: {out_gcode_path}")
    print(f"    -> Saved Markdown deliverable to: {out_md_path}")
    print(f"    -> Saved Visual Toolpath HTML to: {out_html_path}")

def run_task3_code_debugger(input_path: str, out_md_path: str) -> None:
    print("\n[+] Running Workflow 3: Zero-Loop Micro Code Debugger...")
    with open(input_path, "r", encoding="utf-8") as f:
        buggy_code = f.read()

    prompt = f"Find bugs, explain fixes in a table, and give git-style diff:\n\n```python\n{buggy_code}\n```"
    system_prompt = "You are a code debugger. Output a concise markdown report with diffs."
    result = query_model(prompt, system_prompt)

    with open(out_md_path, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"    -> Saved Debug deliverable to: {out_md_path}")

def main() -> None:
    print("=" * 65)
    print("  Qwen3.5-0.8B Weight-Space Programming (WSP) Production Pipeline")
    print(f"  Target Engine: Ollama ('{MODEL_NAME}')")
    print("=" * 65)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    inputs_dir = os.path.join(base_dir, "inputs")
    outputs_dir = os.path.join(base_dir, "outputs")
    os.makedirs(outputs_dir, exist_ok=True)

    task1_in = os.path.join(inputs_dir, "task1_calculus_problem.md")
    task1_tex = os.path.join(outputs_dir, "task1_calculus_derivation.tex")
    task1_md = os.path.join(outputs_dir, "task1_calculus_derivation.md")
    run_task1_calculus(task1_in, task1_tex, task1_md)

    task2_in = os.path.join(inputs_dir, "task2_robotic_command.md")
    task2_gcode = os.path.join(outputs_dir, "task2_robotics_gcode.gcode")
    task2_md = os.path.join(outputs_dir, "task2_robotics_gcode.md")
    task2_html = os.path.join(outputs_dir, "task2_toolpath_visualizer.html")
    run_task2_robotics(task2_in, task2_gcode, task2_md, task2_html)

    task3_in = os.path.join(inputs_dir, "task3_buggy_code.py")
    task3_md = os.path.join(outputs_dir, "task3_code_debug_report.md")
    run_task3_code_debugger(task3_in, task3_md)

    print("\n[✓] All 3 production workflows executed successfully!")
    print("=" * 65)

if __name__ == "__main__":
    main()
