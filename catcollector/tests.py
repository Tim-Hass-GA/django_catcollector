import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

####### SAMPLE TESTCASES
# from .models import User

# Create your tests here.
# def create_question(question_text, days):
#     # create a test question and publish date
#     # off set to now (negitive for in the past / positive for in the future)
#     time = timezone.now() + datetime.timedelta(days=days)
#     return Question.objects.create(question_text=question_text, pub_date=time)
#
#
#
# class QuestionIndexViewTests(TestCase):
#         #### TEST QUESTIONS
#     def test_no_question(self):
#         # if no question exists display an error message
#         response = self.client.get(reverse('polls:index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'No polls are available.')
#         self.assertQuerysetEqual(response.context['latest_question_list'], [])
#
#     def test_past_question(self):
#         # question with pub_date in the past shouldn't display on index page
#         create_question(question_text='Past question.', days=-30)
#         response = self.client.get(reverse('polls:index'))
#         self.assertQuerysetEqual(
#             response.context['latest_question_list'],
#             ['<Question: Past question.>']
#         )
#
#     def test_future_question(self):
#         # question with pub_date in the future shouldn't display on index page
#         create_question(question_text='Future question.', days=30)
#         response = self.client.get(reverse('polls:index'))
#         self.assertContains(response, 'No polls are available.')
#         self.assertQuerysetEqual(response.context['latest_question_list'], [])
#
#     def test_future_question_and_past_question(self):
#         # ensure that both past and future questions do not show on index page
#         create_question(question_text='Past question.', days=-30)
#         create_question(question_text='Future question.', days=30)
#         response = self.client.get(reverse('polls:index'))
#         self.assertQuerysetEqual(
#             response.context['latest_question_list'],
#             ['<Question: Past question.>']
#         )
#
#     def test_two_past_questions(self):
#         create_question(question_text='Past question 1.', days=-30)
#         create_question(question_text='Past question 2.', days=-30)
#         response = self.client.get(reverse('polls:index'))
#         self.assertQuerysetEqual(
#             response.context['latest_question_list'],
#             ['<Question: Past question 2.>','<Question: Past question 1.>']
#         )
#
#
#
# class QuestionModelTests(TestCase):
#         #### TEST FOR PUBLISHED RECENTLY DATE
#     def test_was_published_recently_with_future_question(self):
#         # was_published_recently returns False for question whose pub_date is future date
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_question = Question(pub_date=time)
#         self.assertIs(future_question.was_published_recently(), False)
#
#     def test_was_published_recently_with_old_question(self):
#         # was_published_recently returns false for questions whose pub_date is older than 1 day
#         time = timezone.now() - datetime.timedelta(days=1, seconds=1)
#         old_question = Question(pub_date=time)
#         self.assertIs(old_question.was_published_recently(), False)
#
#     def test_was_published_recently_with_recent_question(self):
#         # was_published_recently returns True if question pub_date is within 1 day
#         time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
#         recent_question = Question(pub_date=time)
#         self.assertIs(recent_question.was_published_recently(), True)
#
#
#
# class QuestionDetailsViewTests(TestCase):
#     def test_future_question(self):
#         # detail view of question with pub_date in future
#         # should return 404
#         future_question = create_question(question_text='Future question.', days=5)
#         url = reverse('polls:detail', args=(future_question.id,))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)
#
#     def test_past_question(self):
#         # detail view of a question with a pub_date in the past
#         past_question = create_question(question_text='Past Question.', days=-5)
#         url = reverse('polls:detail', args=(past_question.id,))
#         response = self.client.get(url)
#         self.assertContains(response, past_question.question_text)
