from gensim import models

#jsentence = models.doc2vec.LabeledSentence(
#j    words=[u'so`bme', u'words', u'here'], tags=["SENT_0"])
#jsentence1 = models.doc2vec.LabeledSentence(
#j    words=[u'here', u'we', u'go'], tags=["SENT_1"])
#j
#jsentence = models.doc2vec.LabeledSentence(
#j    words=['human', 'interface', 'computer'], tags=["SENT_0"])
#jsentence1 = models.doc2vec.LabeledSentence(
#j    words=['survey', 'user', 'computer', 'system', 'response', 'time'], tags=["SENT_1"])
#j
#jsentences = [sentence, sentence1]
#jprint(sentences)

class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        for uid, line in enumerate(open(filename)):
            yield LabeledSentence(words=line.split(), labels=['SENT_%s' % uid])

#docs = [
#    ['human', 'interface', 'computer'], #1
#    ['survey', 'user', 'computer', 'system', 'response', 'time'], #2
#    ['eps', 'user', 'interface', 'system'], #3
#    ['system', 'human', 'system', 'eps'], #4
#    ['user', 'response', 'time'], #5
#    ['trees'], #6
#    ['graph', 'trees'], #7
#    ['graph', 'minors', 'trees'], #8
#    ['graph', 'minors', 'survey'], #9
#    ['human', 'interface', 'computer'], #1
#]
#
#titles = [
#    ["SENT_1"],
#    ["SENT_2"],
#    ["SENT_3"],
#    ["SENT_4"],
#    ["SENT_5"],
#    ["SENT_6"],
#    ["SENT_7"],
#    ["SENT_8"],
#    ["SENT_9"],
#    ["SENT_10"],
#]

titles = []
with open('title.txt' ,'r') as f:
    for l in f:
        titles.append([l[:-1]])

docs = []
with open('body.txt' ,'r') as f:
    for l in f:
        docs.append(l[:-1].split(' '))


sentences = []

for i,title in enumerate(titles):
    sentences.append(models.doc2vec.LabeledSentence(docs[i], title))

#print(sentences)
            
#model = models.Doc2Vec(dm=1, dm_mean=1, size=100, window=10, negative=5, alpha=.025, min_alpha=.025, min_count=0)
#model.build_vocab(sentences)
#for epoch in range(100):
#    model.train(sentences)
#    model.alpha -= 0.002  # decrease the learning rate`
#    model.min_alpha = model.alpha  # fix the learning rate, no decay

model = models.Doc2Vec(sentences, dm=1, dm_mean=1, size=100, window=2, negative=5, min_count=0)

model.save("my_model.doc2vec")
model_loaded = models.Doc2Vec.load('my_model.doc2vec')

#print(model.docvecs.most_similar(["SENT_1"]))
#print(model_loaded.docvecs.most_similar(["SENT_2"]))
print(model_loaded.docvecs.most_similar(["言語"]))
