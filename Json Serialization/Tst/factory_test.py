from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.Logics.report_factory import report_factory

import unittest

class factory_test(unittest.TestCase):

    def test_check_report_factory_create(self):
        manager = settings_manager()
        start = start_factory( manager.settings )
        start.create()
        factory = report_factory()
        key = storage.unit_key()

        report = factory.create( 
                                manager.settings.report_mode, 
                                start.storage.data)

        assert report is not None
        print ( report.create(key) )
 

    def test_check_create_receipts(self):

        items = start_factory.create_receipts()


        assert len(items) > 0     

    def test_check_create_nomenclatures(self):
        items = start_factory.create_nomenclatures()

        assert len(items) > 0 
        

    def test_check_create_units(self):

        items = start_factory.create_units()

        assert len(items) > 0    


    def test_check_create_groups(self):

        items = start_factory.create_groups()

        assert len(items) > 0

    def test_check_factory_create(self):
        manager = settings_manager()
        factory = start_factory( manager.settings )

        result = factory.create()

        if manager.settings.is_first_start == True:
            assert result == True
            assert not factory.storage is None
            assert storage.nomenclature_key() in factory.storage.data
            assert storage.receipt_key() in factory.storage.data
            assert storage.group_key() in factory.storage.data
            assert storage.unit_key() in factory.storage.data
        else:
            assert result == False    


    def test_factory_create(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)
        result = factory.create()

        if manager.settings.is_first_start:
            self.assertTrue(result)
            self.assertIsNotNone(factory.storage)
            self.assertIn(storage.nomenclature_key(), factory.storage.data)
            self.assertIn(storage.receipt_key(), factory.storage.data)
            self.assertIn(storage.group_key(), factory.storage.data)
            self.assertIn(storage.unit_key(), factory.storage.data)
        else:
            self.assertFalse(result)
