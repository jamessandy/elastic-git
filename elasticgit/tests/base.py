from unittest import TestCase

from elasticgit.models import Model
from elasticgit.manager import EG


class ModelBaseTest(TestCase):

    def mk_model(self, fields):
        return type('TempModel', (Model,), fields)

    def mk_workspace(self, repo='.test_repo', url='https://localhost',
                     index_name='test-repo-index', setup=False,
                     name='Test Kees', email='kees@example.org'):
        workspace = EG.workspace(repo, es={
            'urls': [url],
        }, index_name=index_name)
        if setup:
            workspace.setup(name, email)
        return workspace