import numpy as np

class LDATestSample:
    def __init__(self,
                 num_doc_gen=50,
                 num_word_gen=100,
                 num_topic=10,
                 ave_len=200,
                 alpha=.1,
                 beta=.1):
        mcorpus = []
        Word = []
        Beta = np.random.dirichlet(beta * np.ones(num_word_gen), num_topic).transpose()
        Theta = np.random.dirichlet(alpha * np.ones(num_topic), num_doc_gen).transpose()

        for i in range(num_doc_gen):
            mcorpus.append([])
            doc_len = ave_len
            theta = Theta[:, i]
            doc_beta = Beta.dot(theta)

            w = np.random.multinomial(doc_len, doc_beta)
            Word.append(w)
            for j in range(num_word_gen):
                mcorpus[i].append((j, w[j]))
        self.Beta = Beta
        self.Theta = Theta
        self.Corpus = mcorpus
        self.Word = Word


if __name__ == '__main__':
    w = LDATestSample(2, 10, 2, 5)
    print w.Corpus
