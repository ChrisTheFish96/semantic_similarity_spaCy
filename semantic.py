# Program to show the usage of spaCy module.
# Import the module.
import spacy
# Load the a more advanced language module than used in previous tasks.
nlp = spacy.load('en_core_web_md')

# First example, checking the similarity between three words.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.text, word2.text, word1.similarity(word2))
print(word3.text, word2.text, word3.similarity(word2))
print(word3.text, word1.text, word3.similarity(word1))

'''An interesting note is that cat and monkey have a high similarity because they are both
animals. Banana and monkey have a higher similarity than banana and cat because cats don't
eat bananas but I would have expected monkey and banana to have a bit higher similarity than
it does, but at least it is higher than banana and cat.'''

# First example with new words, checking the similarity between three words.
word1 = nlp("pizza")
word2 = nlp("pasta")
word3 = nlp("apple")
print(word1.text, word2.text, word1.similarity(word2))
print(word3.text, word2.text, word3.similarity(word2))
print(word3.text, word1.text, word3.similarity(word1))

# Similarity in sentences.
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
    
tokens2 = nlp('pizza banana dog pasta')
for token1 in tokens2:
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))

# Similarity between projects.
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Loading the simpler language model.
nlp = spacy.load('en_core_web_sm') 

# Rerun of example above.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.text, word2.text, word1.similarity(word2))
print(word3.text, word2.text, word3.similarity(word2))
print(word3.text, word1.text, word3.similarity(word1))

word1 = nlp("pizza")
word2 = nlp("pasta")
word3 = nlp("apple")
print(word1.text, word2.text, word1.similarity(word2))
print(word3.text, word2.text, word3.similarity(word2))
print(word3.text, word1.text, word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
    
tokens2 = nlp('pizza banana dog pasta')
for token1 in tokens2:
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

''' All similarities when running the example file on a simpler model seem to be higher than it is on
the more advanced language model. The results also don't seem as reliable on a simpler model, like the
words cat and banana now have a similarity above 0.5 which is very different from the 0.2 from 
the advanced model.
I also receive a type of warning when using the simpler model stating that the results may not be
useful with its similarity judgements.'''