import re
from collections import Counter
import math

def text_to_vector(text):
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

def cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def main():
    file1 = input("Enter path to first file: ")
    file2 = input("Enter path to second file: ")

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    similarity = cosine_similarity(vector1, vector2)

    print(f"Similarity between the documents: {similarity}")

if __name__ == "__main__":
    main()
