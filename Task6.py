from collections import Counter
import string

def analyze_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # Basic counts
        lines = text.splitlines()
        num_lines = len(lines)
        num_words = len(text.split())
        num_chars = len(text)

        # Word frequency analysis
        # Normalize: lowercase, remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        words = text.lower().translate(translator).split()
        word_counts = Counter(words)
        most_common = word_counts.most_common(10)

        # Display results
        print("\n📊 Text File Analysis Report")
        print(f"🔹 Total Lines     : {num_lines}")
        print(f"🔹 Total Words     : {num_words}")
        print(f"🔹 Total Characters: {num_chars}\n")

        print("🧠 Top 10 Most Common Words:")
        print(f"{'Word':<15}{'Count'}")
        print("-" * 25)
        for word, count in most_common:
            print(f"{word:<15}{count}")

    except FileNotFoundError:
        print("❗ Error: File not found.")
    except Exception as e:
        print(f"❗ Unexpected error: {e}")

# Main execution
if __name__ == "__main__":
    filename = input("📁 Enter the path to your text file: ").strip()
    analyze_file(filename)
