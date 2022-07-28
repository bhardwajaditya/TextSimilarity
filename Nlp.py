from datasketch import MinHash, MinHashLSH
from nltk import ngrams

questions = [
     "Which of the following are energy fruits",
     "Which of the following are strong fruits",
     "Which of the following is not a fruit",
     "Which of the following is a vegetable"
]

target = "What are strong fruits"

data = ['minhash is a probabilistic data structure for estimating the similarity between datasets',
  'finhash dis fa frobabilistic fata ftructure for festimating the fimilarity fetween fatasets',
  'weights controls the relative importance between minizing false positive',
  'wfights cfntrols the rflative ifportance befween minizing fflse posftive',
]



# Create an MinHashLSH index optimized for Jaccard threshold 0.5,
# that accepts MinHash objects with 128 permutations functions
lsh = MinHashLSH(threshold=0.7, num_perm=128)

# Create MinHash objects
minhashes = {}
for index, value in enumerate(questions):
  minhash = MinHash(num_perm=128)
  for gram in ngrams(value, 3):
    minhash.update("".join(gram).encode('utf-8'))
  lsh.insert(index, minhash)
  minhashes[index] = minhash

minhash = MinHash(num_perm=128)
for d in ngrams(target, 3):
  minhash.update("".join(d).encode('utf-8'))
lsh.insert(len(questions), minhash)
minhashes[len(questions)] = minhash

result = lsh.query(minhashes[len(questions)])
print("Candidates with Jaccard similarity > 0.5 for input", target, ":", result)