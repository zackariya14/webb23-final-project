from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post

class TestPost(APITestCase):

    def setUp(self):
        # Create a post to use in tests
        self.post = Post.objects.create(title="Test Post", content="This is a test post.")

    def test_create_post(self):
        url = reverse('post-list-create')
        data = {'title': 'New Post', 'content': 'New content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.get(id=2).title, 'New Post')

    def test_list_posts(self):
        url = reverse('post-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Post')

    def test_retrieve_post(self):
        url = reverse('post-detail', args=[self.post.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')

    def test_update_post(self):
        url = reverse('post-detail', args=[self.post.id])
        data = {'title': 'Updated Post', 'content': 'Updated content'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')
        self.assertEqual(self.post.content, 'Updated content')

    def test_partial_update_post(self):
        url = reverse('post-detail', args=[self.post.id])
        data = {'title': 'Partially Updated Post'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Partially Updated Post')

    def test_delete_post(self):
        url = reverse('post-detail', args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
