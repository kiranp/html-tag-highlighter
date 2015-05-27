#Sample unit test
from django.test import TestCase
class MyFormTestCase(TestCase):
    def testEmptyPost(self):
        response = self.client.post("/", {'inputUrl':''})
        #Does the form load?
        self.assertTemplateUsed(response, 'tags.html')

        print 'Errors:', response.context['form'].errors
        print 'Is Valid',response.context['form'].is_valid()
        self.assertFormError(response, 'form', 'inputUrl', [u'This field is required.'])
