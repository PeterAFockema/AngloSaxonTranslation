from encoder_rnn import EncoderRNN

def encoderRNN(input_lang, hidden_size, device):
    return EncoderRNN(input_lang.n_words, hidden_size).to(device)
