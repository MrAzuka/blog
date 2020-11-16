from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


# Create your tests here.
class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret')
        self.post = Post.objects.create(
            title='A good title',
            article='Nice body content',
            author=self.user, )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')

        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.article}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')

        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_create_post_view(self):
        res = self.client.post(reverse('post_new'), {
            'title': 'New title', 'author': self.user, 'article': 'Test server'
        })
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Test server', 1)
        self.assertNotContains(res, 'Not a boy')

    def test_update_post_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title', 'article': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    def test_delete_post_view(self):
        response = self.client.post(
            reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)