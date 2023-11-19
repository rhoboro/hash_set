# HashSet: A Python Wrapper for Rust's HashSet Type

This repository contains the content of [Wrapping Rust Types as Python Classes](https://depth-first.com/articles/2020/08/03/wrapping-rust-types-as-python-classes/) written by Richard L. Apodaca.
This is sample code that does FFI between Rust and Python using only libc and also supports Python classes.
Please read the original article and [rapodaca/hash_set](https://github.com/rapodaca/hash_set).

```bash
$ cargo build
# on macOS
$ DYLD_LIBRARY_PATH=target/debug python3 -m unittest -v
test_all (tests.test_hash_set.HashSetTestCase.test_all) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

$ DYLD_LIBRARY_PATH=target/debug python3
>>> from hash_set import HashSet
>>> s = HashSet()
>>> s.contains(0)
False
>>> s.insert(0)
True
>>> s.contains(0)
True
>>> s.insert(0)
False
>>> s.insert(1)
True
>>> s.len()
2
>>> s.collect()
[1, 0]
```
