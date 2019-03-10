from test_data import current_language_order, expected_language_order

def pytest_generate_tests(metafunc):
    argvalues = list(zip(current_language_order, expected_language_order))
    ids = ["first", "second", "third", "fourth"]
    metafunc.parametrize(["current_language","expected_language"], argvalues, scope="function")