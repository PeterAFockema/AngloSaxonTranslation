import unittest

from anglosaxon.encoders.encoder_rnn import EncoderRNN

class TestLangs(unittest.TestCase):

    def test_EncoderRNN(self):
        EncoderRNN(input_size=2, hidden_size=1)

if __name__ == '__main__':
    unittest.main()
