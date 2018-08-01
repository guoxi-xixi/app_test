import allure,pytest
class Test_001:
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="test_001")
    def test_001(self):
        allure.attach('用户名', "xixi")
        allure.attach("密码","123456")
        assert 1
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="test_002")
    def test_002(self):
        assert 0
    def test_003(self):
        assert 1