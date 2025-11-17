import os

def print_tree(base_path, level=0, max_depth=3):
    if level >= max_depth:
        return
    prefix = "│   " * level
    try:
        items = sorted(os.listdir(base_path))
    except PermissionError:
        return

    ignore = {'.git', 'venv', '__pycache__'}

    for i, item in enumerate(items):
        if item in ignore:
            continue
        full_path = os.path.join(base_path, item)
        connector = "└── " if i == len(items) - 1 else "├── "
        print(f"{prefix}{connector}{item}")

        if os.path.isdir(full_path):
            print_tree(full_path, level + 1, max_depth)

if __name__ == "__main__":
    root = os.getcwd()
    print(f"\n📂 Estrutura de arquivos até 3 níveis em: {root}\n")
    print_tree(root, max_depth=3)