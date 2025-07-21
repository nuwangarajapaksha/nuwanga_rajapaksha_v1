from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.contrib.messages import get_messages


class FooterContactViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('send_message')  # update this if you use a different name
        self.referer = '/'
        self.valid_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.',
        }
        self.invalid_data = {
            'name': '',
            'email': 'invalid_email',
            'message': '',
        }

    def test_valid_contact_form_submission(self):
        response = self.client.post(
            self.url,
            data=self.valid_data,
            HTTP_REFERER=self.referer,
        )

        # Should redirect back
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.referer)

        # Email should be sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('This is a test message.', mail.outbox[0].body)

        # Success message should exist
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Your message has been sent successfully" in str(m) for m in messages))

    def test_invalid_contact_form_submission(self):
        response = self.client.post(
            self.url,
            data=self.invalid_data,
            HTTP_REFERER=self.referer,
        )

        # Should redirect back
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.referer)

        # No email should be sent
        self.assertEqual(len(mail.outbox), 0)

        # Error message should exist
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Please enter the correct details" in str(m) for m in messages))
