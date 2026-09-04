from test_case import TestCase
from test_result import TestResult
from test_loader import TestLoader
from test_suite import TestSuite
from test_case_test import TestCaseTest
from test_suite_test import TestCaseTest
from test_suite_test import TestSuiteTest
from test_loader_test import TestLoaderTest
from test_runner import TestRunner

class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')

if __name__ == '__main__':
    result = TestResult()

    test = MyTest('test_a')
    test.run(result)

    test = MyTest('test_b')
    test.run(result)

    test = MyTest('test_c')
    test.run(result)

    loader = TestLoader()
    test_case_suite = loader.make_suite(TestCaseTest)
    test_suite_suite = loader.make_suite(TestSuiteTest)
    test_load_suite = loader.make_suite(TestLoaderTest)

    suite = TestSuite()
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_load_suite)

    runner = TestRunner()
    runner.run(suite)

    print(result.summary())