from test_my_dict import Dict
import unittest

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertEqual(isinstance(d, dict),True)
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d['key'], 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertEqual('key' in d, True)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        """期待抛出指定类型的Error，
        比如通过d['empty']访问不存在的key时，我们期待断言会抛出KeyError："""
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        """通过d.empty访问不存在的key时，我们期待抛出AttributeError："""
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

"""当做正常的python脚本运行, $ python mydict_test.py
另一种方法是在命令行通过参数-m unittest直接运行单元测试：
$ python -m unittest mydict_test
这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。"""

if __name__ == '__main__':
    unittest.main()
if __name__ == '__main__':
    unittest.main()
