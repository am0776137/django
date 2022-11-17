from django.test import TestCase

from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    """
        To test the creation and reading of a post in the database
    """

    def setUp(self):
        """
            creating a Post to test later
        """
        Post.objects.create(text="just a test")

    
    def test_text_content(self):
        """
            testing the created post
        """
        # getting the post id
        post = Post.objects.get(id=1)
        
        expected_object_name =  f'{post.text}' # this should evaluate to 'just a text'
        self.assertEqual(expected_object_name, 'just a test') # checking if the db field actually contains the same text


from django.urls import reverse # for generating url from url-name
                                # instead of using the url we use url-name as urls get to change over
                                # the development of the site, whereas, the url-names tend not to change.
                                # This is a way to make our tests future-proof

class HomePageViewTest(TestCase):
    """
        Testing HomePageView for:
            - existance of url/page: HTTP 200 response
            - HomePageView as a working view
            - home.html as working template
    """
    def setUp(self):
        Post.objects.create(text="this is another test")
    
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    

    














