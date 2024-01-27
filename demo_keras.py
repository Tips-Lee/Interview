import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
from tensorflow.contrib.legacy_seq2seq.python.ops.seq2seq import embedding_attention_seq2seq
from tensorflow.contrib.crf import crf_log_likelihood, crf_decode, crf_sequence_score, crf_binary_score, crf_log_norm
import gensim

gensim.models.word2vec.Word2Vec