import unittest
# Import the function from the package created in Task 4
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    Unit tests for the emotion_detector function.
    """
    
    def test_joy_statement(self):
        """Test for the statement: 'I am glad this happened' -> joy"""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_statement(self):
        """Test for the statement: 'I am really mad about this' -> anger"""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_statement(self):
        """Test for the statement: 'I feel disgusted just hearing about this' -> disgust"""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        
    def test_sadness_statement(self):
        """Test for the statement: 'I am so sad about this' -> sadness"""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        
    def test_fear_statement(self):
        """Test for the statement: 'I am really afraid that this will happen' -> fear"""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()