from plonetheme.das.tests.base import ThemedasTestCase as TestCase


class ThemedasTestCase(TestCase):

    def test_das_layers_available(self):
        self.failUnless('das_images' in self.portal.portal_skins)
        self.failUnless('das_styles' in self.portal.portal_skins)
        self.failUnless('das_templates' in self.portal.portal_skins)

    def test_das_skin_installed(self):
        self.skins = self.portal.portal_skins
        theme = self.skins.getDefaultSkin()
        self.failUnless(theme == 'das Theme', 'Default theme is %s' % theme)


def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)
