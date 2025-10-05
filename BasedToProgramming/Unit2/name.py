from utils.unit_test import TestClass

test_utils = TestClass()

name = "add love to Home"
print(name.upper())
test_utils.assertEqual(name.title(), "Add Love To Home")
test_utils.assertEqual(name.lower(), "add love to home")
test_utils.assertEqual(name.upper(), "ADD LOVE TO HOME")
test_utils.assertEqual("add love to" + " " + "home", "add love to home")
test_utils.assertEqual(" add".lstrip(), "add")
test_utils.assertEqual("add ".rstrip(), "add")
test_utils.assertEqual("add".strip(), "add")

