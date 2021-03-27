from django.core import mail
from django.test import TestCase


class EmailTest(TestCase):

    def test_send_email(self):
        # Send message.
        mail.send_mail(
            'Enviando', 'Testando oe email.',
            'francisco@gmail.com@example.com', ['raphael@example.com'],
            fail_silently=False,
        )

        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject, 'Enviando')



    def test_send_email_erro(self):
        # Send message.
        mail.send_mail(
            'Enviando', 'Testando oe email.',
            'francisco@gmail.com@example.com', [''],
            fail_silently=False,
        )

        self.assertEqual(len(mail.outbox), 0)

