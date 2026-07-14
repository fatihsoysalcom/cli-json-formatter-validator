import json
import sys

def main():
    """
    A simple command-line JSON formatter and validator.
    This tool helps developers avoid opening browser tabs for quick JSON checks,
    improving focus and reducing context switching.
    """
    if len(sys.argv) > 2:
        print("Usage: python json_tool.py [input_file.json]", file=sys.stderr)
        print("       Or pipe JSON: echo '{\"key\": \"value\"}' | python json_tool.py", file=sys.stderr)
        sys.exit(1)

    input_data = ""
    if len(sys.argv) == 2:
        # Read from file
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                input_data = f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {sys.argv[1]}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Read from stdin
        if sys.stdin.isatty():
            print("Paste JSON and press Ctrl+D (Unix) or Ctrl+Z then Enter (Windows):", file=sys.stderr)
        input_data = sys.stdin.read()

    if not input_data.strip():
        print("Error: No JSON input provided.", file=sys.stderr)
        sys.exit(1)

    try:
        # Attempt to parse and pretty-print the JSON.
        # This step implicitly validates the JSON structure.
        parsed_json = json.loads(input_data)
        pretty_json = json.dumps(parsed_json, indent=2, ensure_ascii=False)
        print(pretty_json)
        # This CLI tool demonstrates how to perform a common developer task
        # (JSON formatting/validation) directly in the terminal.
        # By using a command-line alternative, developers avoid opening a new
        # browser tab for an online formatter, thereby reducing context switching
        # and improving overall productivity as discussed in the article.

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
