"""Quick test for the paraphrase engine. Run: python test_paraphrase.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from plagiarism_app.paraphrase_engine import deep_paraphrase, deep_paraphrase_paragraph
from difflib import SequenceMatcher

original = (
    "A paragraph is a distinct unit of writing, consisting of one or more sentences, "
    "that develops a single, cohesive idea or topic. It is a foundational element of writing "
    "that offers structure and clarity, usually featuring a topic sentence, supporting details, "
    "and a concluding sentence. Properly organized, paragraphs help readers follow the author's "
    "logic and break up text for better readability."
)

print("=" * 70)
print("ORIGINAL:")
print("=" * 70)
print(original)

for i in range(5):
    result = deep_paraphrase_paragraph(original, original)
    sim = SequenceMatcher(None, original.lower(), result.lower()).ratio()
    print(f"\n{'=' * 70}")
    print(f"REWRITE #{i+1}  (similarity to original: {sim:.0%})")
    print(f"{'=' * 70}")
    print(result)
