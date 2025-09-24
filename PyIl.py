import argparse
import unicodedata

# Function to calculate the display width of a word
def display_width(word):
    """Calculate the display width of a word, where East Asian wide chars are width 2."""
    return sum(2 if unicodedata.east_asian_width(c) in ['W', 'F'] else 1 for c in word)

# Function to process a block of lines and align them, splitting into chunks if necessary
def process_block(lines, lines_per_block, max_length):
    # Check if the block has the correct number of lines
    if len(lines) != lines_per_block:
        print(f"Warning: Block has {len(lines)} lines, expected {lines_per_block}. Skipping.")
        return

    # Split each line into words
    all_words = [line.split() for line in lines]
    num_columns = len(all_words[0])  # Number of words in the first line

    # Verify all lines have the same number of words
    if any(len(words) != num_columns for words in all_words):
        print("Warning: Lines in block have different numbers of words. Skipping.")
        return

    # Calculate the maximum display width for each column
    max_widths = [max(display_width(line[col]) for line in all_words) for col in range(num_columns)]

    # Calculate total display width (sum of max widths + spaces between words)
    total_width = sum(max_widths) + len(max_widths) - 1  # Spaces between words

    # Determine chunk size based on max_length
    if total_width <= max_length:
        chunk_size = num_columns
    else:
        # Find the largest number of words that fit within max_length
        cum_width = 0
        for k in range(1, num_columns + 1):
            cum_width += max_widths[k - 1] + (1 if k > 1 else 0)
            if cum_width > max_length:
                chunk_size = k - 1
                break
        else:
            chunk_size = num_columns

    # Process each chunk
    for start in range(0, num_columns, chunk_size):
        end = min(start + chunk_size, num_columns)
        chunk_max_widths = max_widths[start:end]
        chunk_words = [words[start:end] for words in all_words]

        # Format and print each line in the chunk
        for words in chunk_words:
            parts = []
            for j, word in enumerate(words):
                width = display_width(word)
                padding = chunk_max_widths[j] - width
                parts.append(word + ' ' * padding)
                if j < len(words) - 1:
                    parts.append(' ')  # Space between words
            print(''.join(parts))
        print()  # Blank line after each chunk

# Main function to handle file input and process blocks
def main():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Align interlinear text from a file.")
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("--max-length", type=int, default=80, help="Maximum line length")
    parser.add_argument("--lines-per-block", type=int, default=2, help="Lines per block")
    args = parser.parse_args()

    # Read the file
    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{args.input_file}' was not found.")
        return

    # Split into blocks separated by blank lines
    blocks = content.split('\n\n')
    for i, block in enumerate(blocks):
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        if lines:
            if i > 0:
                print()  # Extra blank line between blocks
            process_block(lines, args.lines_per_block, args.max_length)

if __name__ == "__main__":
    main()
