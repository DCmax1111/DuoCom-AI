
v1_code = """
# Minimal keyword-based chatbot for v1.0
from difflib import get_close_matches

dataset_path = 'data/korean_v1.txt'

english_sentences = []
korean_sentences = []

with open(dataset_path, 'r', encoding='utf-8') as f:
    for line in f:
        if '||' in line:
            eng, kor = line.strip().split('||')
            english_sentences.append(eng.strip())
            korean_sentences.append(kor.strip())

print(f"Loaded {len(english_sentences)} sentences")
print("First 5 pairs:")
for i in range(5):
    print(f"{english_sentences[i]} -> {korean_sentences[i]}")


def duocom_korean_bot(user_input):
    user_input = user_input.lower()
    closest_match = get_close_matches(user_input, [eng.lower() for eng in english_sentences], n=1, cutoff=0.5)
    if closest_match:
        idx = [eng.lower() for eng in english_sentences].index(closest_match[0])
        return f"{korean_sentences[idx]}, {user_input.capitalize()}"
    return "죄송합니다, 이해하지 못했어요 (Sorry, I don't understand)"
"""

with open('model/dc_korean_v1.py', 'w', encoding='utf-8') as f:
    f.write(v1_code)

print("DuoCom Korean v1.0 model code has been created in 'model/dc_korean_v1.py'")
