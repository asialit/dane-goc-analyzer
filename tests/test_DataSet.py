import pytest
from src import data_manager


class TestDataSet:

    def test_calculate_pass_rate(self):

        # Arrange
        # Data Set 1
        elem = data_manager.Data('region', 'przystąpiło', 'kobiety', 2010, 2)
        elem2 = data_manager.Data('region', 'przystąpiło', 'mężczyźni', 2010, 2)
        elem3 = data_manager.Data('region', 'zdało', 'kobiety', 2010, 1)
        elem4 = data_manager.Data('region', 'zdało', 'mężczyźni', 2010, 1)
        test_data = [elem, elem2, elem3, elem4]

        test_data_set = data_manager.DataSet(test_data)

        # Data Set 2
        elem1 = data_manager.Data('region', 'przystąpiło', 'kobiety', 2010, 19345)
        elem21 = data_manager.Data('region', 'przystąpiło', 'mężczyźni', 2010, 21234)
        elem31 = data_manager.Data('region', 'zdało', 'kobiety', 2010, 17500)
        elem41 = data_manager.Data('region', 'zdało', 'mężczyźni', 2010, 19653)
        test_data2 = [elem1, elem21, elem31, elem41]

        test_data_set2 = data_manager.DataSet(test_data2)

        # Data Set 3
        elem2 = data_manager.Data('region', 'przystąpiło', 'kobiety', 2010, 19345.0)
        elem22 = data_manager.Data('region', 'przystąpiło', 'mężczyźni', 2010, 21234.0)
        elem32 = data_manager.Data('region', 'zdało', 'kobiety', 2010, 17500.0)
        elem42 = data_manager.Data('region', 'zdało', 'mężczyźni', 2010, 19653.0)
        test_data3 = [elem2, elem22, elem32, elem42]

        test_data_set3 = data_manager.DataSet(test_data3)

        # Act
        result1 = data_manager.calculate_pass_rate(test_data_set, 'region', 2010, 4)
        result2 = data_manager.calculate_pass_rate(test_data_set2, 'region', 2010, 4)
        result3 = data_manager.calculate_pass_rate(test_data_set3, 'region', 2010, 4)

        # Assert
        assert result1 == 50, pytest.fail("Wrong result")
        assert result2 == 91, pytest.fail("Wrong result")
        assert result3 == 91, pytest.fail("Wrong result")

        assert type(result3) == int, pytest.fail("Wrong type")
