from django.test import TestCase
from django.urls import reverse

from .models.author import Author
from .models.book import Book
from .models.category import Category


class ProductTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name='جورج',
            last_name='اورول',
            slug='جورج-اورول',
        )
        self.category = Category.objects.create(
            name='تخیلی',
            slug='تخیلی',
        )
        self.book = Book.objects.create(
            title='قلعه حیوانات',
            number_in_stock='3',
            unit_price='30000',
            slug='قلعه-حیوانات',
        )
        self.book.authors.add(self.author)
        self.book.categories.add(self.category)

    def test_string_check(self):
        self.assertEqual(str(self.book), self.book.title)

    def test_book_content(self):
        self.assertEqual(self.book.authors.all().first(), self.author)
        self.assertEqual(self.book.categories.all().first(), self.category)

    def test_product_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    # def test_get_absolute_url_book(self):
    #     self.assertEqual(self.book.get_absolute_url(), f'/book/{self.book.slug}/')

    def test_book_delete_view(self):
        response = self.client.post(
            reverse('book_delete', args=[self.book.id, ]))
        self.assertEqual(response.status_code, 302)
