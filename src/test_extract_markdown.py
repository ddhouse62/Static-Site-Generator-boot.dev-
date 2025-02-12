import unittest
from parse_markdown import (extract_markdown_images, extract_markdown_links)

class  TestExtractImages(unittest.TestCase):
    
    def test_single_image(self):
        test_case = [("an image of a ball", "localhost")]
        self.assertEqual(test_case, extract_markdown_images("Here you can see an image of a red ball ![an image of a ball](localhost)"))

    def test_multiple_images(self):
        test_case = [("an image of a ball", "localhost"), ("an image of a young boy", "localhost/boy"), ("the google logo", "google.com")]
        text_to_text = "Here you can see a boy playing with a red ball, as pictured below: ![an image of a ball](localhost) ![an image of a young boy](localhost/boy)  You can find more about his story by going to google. ![the google logo](google.com)"
        self.assertEqual(test_case, extract_markdown_images(text_to_text))
    
    def test_no_images(self):
        test_case = []
        text = "lorem ipsum dolor est"
        self.assertEqual(test_case, extract_markdown_images(text))


class TestExtractLinks(unittest.TestCase):
    def test_single_link(self):
        test_case = [("google", "google.com")]
        text = "you can search for results at [google](google.com)"
        self.assertEqual(test_case, extract_markdown_links(text))

    def test_multiple_links(self):
        test_case = [("google", "google.com"), ("netflix", "netflix.com"), ("facebook", "facebook.com")]
        text = "Among the most popular sites on the internet are [google](google.com), [netflix](netflix.com), and [facebook](facebook.com)"
        self.assertEqual(test_case, extract_markdown_links(text))

    def test_no_links(self):
        test_case = []
        text = "Among the most popular sites on the internet are google, netflix, and facebook"
        self.assertEqual(test_case, extract_markdown_links(text))
