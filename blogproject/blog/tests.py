from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.

# Tests:
# create user, create a post under this created user, test list-view, test detailed-view, 


class BlogTests(TestCase):
    
    def setUp(self):
        # user creation
        self.user = get_user_model().objects.create_user(
            username = "testuser",
            email = 'test@test.com',
            password = 'secret'
        )
    
        # pist creation
        self.post = Post.objects.create(
            title = 'test-post',
            body = 'test body content',
            author = self.user # created 
        )

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'test-post')
        self.assertEqual(f'{self.post.body}', 'test body content')
        self.assertEqual(f'{self.post.author}', 'testuser') # perhaps, author returns username as object representation in __str__ 
        # otherwise self.post.author.username would have been checked against the username string


    def test_post_list_view(self):
        '''
            testing home page link, its response, some of its content, and the template used 
        '''
        response = self.client.get(reverse('home')) # accessing the url 
        print(response)
        self.assertEqual(response.status_code, 200) # checking if it exists
        self.assertContains(response, 'test-post')
        self.assertTemplateUsed(response, 'home.html')



    def test_post_detail_view(self):
        """
            testing DetailView of the test-post, 
            testing a non-existing post and 404 response return,
            testing DetailView contents,
            testing template used in DetailView
        """
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)

        no_response = self.client.get('/post/1000/')
        self.assertEqual(no_response.status_code, 404)

        self.assertContains(response, 'test body content')
        self.assertTemplateUsed(response, 'post_detail.html')



    # NEW Tests after adding CRUD functionality
    #   def test_get_absolute_url
    #   def test_post_create_view
    #   def test_post_update_view
    #   def test_post_delete_view

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), "/post/1/") # as a post datamember has already been created above

    def test_post_create_view(self):
        """creating a new post using the ConfUrl post_new and checking if its view is funcitoning
        properly """

        response = self.client.post(
            # get the url and then send it a new post object in dict form
            reverse('post_new'), 
            {
                "title" : "test title",
                "body" : "test body",
                "author" : self.user
            }
        )
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 'test title')
        self.assertContains(response, 'test body')
    
    
    def test_post_uodate_view(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {
                "title" : "updated title",
                "body" : "updated text"
            }
        )

        self.assertContains(response, "updated title")
        self.assertEqual(response.status_code, 302) # 302 is a redirect code as we redirect to detailed post view after updation

    def test_post_delete_view(self):
        response = self.client.post(
            reverse("post_delete", args="1")
        )
        self.assertEqual(response.status_code, 302) # 302 is a redirect code as we redirect after deletion

            





