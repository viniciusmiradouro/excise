from pydantic import FilePath, PositiveInt


def excision(file_path: FilePath, start_line: PositiveInt, end_line: PositiveInt) -> None:
    """
    Extracts and prints an inclusive range of lines from a file.

    Args:
        file_path (FilePath): The path to the file.
        start_line (PositiveInt): The starting line number (1-based).
        end_line (PositiveInt): The ending line number (inclusive).

    Returns:
        None
    """
    lines = file_path.read_text().splitlines()
    selected_lines = '\n'.join(lines[start_line - 1:end_line])
    print(selected_lines)
