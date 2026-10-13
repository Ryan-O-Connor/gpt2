import time
import re
import torch


def verdict():
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    print("Total number of characters {}".format(len(raw_text)))
    print(raw_text[:99])
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [s for s in preprocessed if s.strip()]
    print(len(preprocessed))
    print(preprocessed[:30])


def test_tokenize():
    text = "Hello, World. Is this-- a test?"
    result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    result = [s for s in result if s.strip()]
    print(result)


def main():
    verdict()


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Run time: {:.2f} seconds".format(end - start))