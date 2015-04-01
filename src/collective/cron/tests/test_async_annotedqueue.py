import unittest
from collective.cron.tests import base
from collective.cron import interfaces as i


class AQueueTest(base.IntegrationTestCase):
    def setUp(self):
        base.IntegrationTestCase.setUp(self)
        self.marker = self.layer['crontab_marker']
        self.aqueue = i.IAnnotedQueue(self.marker.queue)
        [self.queue.remove(j) for j in self.queue]

    def tearDown(self):
        base.IntegrationTestCase.tearDown(self)
        [self.queue.remove(j) for j in self.queue]

    def test_pasync_queue_annotations(self):
        self.assertEquals(self.aqueue.annotations, {'plone': ['/plone']})

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

