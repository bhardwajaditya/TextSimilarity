from datasketch import MinHash, MinHashLSH
from nltk import ngrams

def getSimilarQuestion(questions, target):

    # Create an MinHashLSH index optimized for Jaccard threshold 0.4,
    # that accepts MinHash objects with 128 permutations functions
    lsh = MinHashLSH(threshold=0.4, num_perm=128)

    # Create MinHash objects
    minhashes = {}
    for index, value in enumerate(questions):
        print(value)
        minhash = MinHash(num_perm=128)
        for gram in ngrams(value['text'], 3):
            minhash.update("".join(gram).encode('utf-8'))
        lsh.insert(index, minhash)
        minhashes[index] = minhash

    minhash = MinHash(num_perm=128)
    for d in ngrams(target, 3):
        minhash.update("".join(d).encode('utf-8'))
    lsh.insert(len(questions), minhash)
    minhashes[len(questions)] = minhash

    result = lsh.query(minhashes[len(questions)])
    print("Candidates with Jaccard similarity > 0.4 for input", target, ":", result)
    result = [questions[i] for i in range(len(questions)) if i in result]
    return result