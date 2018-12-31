# The-Chatbot-Project

In this project, we will build a chatbot using conversations from Cornell University's Movie Dialogue Corpus. The main features of our model are LSTM cells, a bidirectional dynamic RNN, and decoders with attention.
The conversations will be cleaned rather extensively to help the model to produce better responses. As part of the cleaning process, punctuation will be removed, rare words will be replaced with "UNK" (our "unknown" token), longer sentences will not be used, and all letters will be in the lowercase.
Right now our focus is on building a simple conversational chatbot and later hope to extend its functionalities and use it as a Q/A chatbot for Internity.
