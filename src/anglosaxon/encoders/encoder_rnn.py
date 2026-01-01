import torch
import torch.nn as nn

'''
class EncoderRNN
The Encoder class is to be used as part of a Seq2Seq/ Encoder Decoder network, 
which is a model that consists of two RNNs (Recurrent Neural Networks) called the encoder and decoder.
The encoder reads an input sequence and outputs a single vector.
'''

class EncoderRNN(nn.Module):
    def __init__(self, input_size: int, hidden_size: int, dropout_p: float =0.1):
        super(EncoderRNN, self).__init__()
        self.hidden_size = hidden_size

        self.embedding = nn.Embedding(input_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size, batch_first=True)
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, input: torch.Tensor):
        embedded = self.dropout(self.embedding(input))
        output, hidden = self.gru(embedded)
        return output, hidden