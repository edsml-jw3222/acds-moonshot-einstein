import os
import doctest
import sys
from pytest import fixture, mark

sys.path.append('..')
import moonshot


def test_folder_exits():
    assert os.path.exists("../images")
    assert os.path.exists("../labels")
    assert os.path.exists("../labels/training")
    assert os.path.exists("../labels/validation")
    assert os.path.exists("../labels/test")
    assert os.path.exists("../images/training")
    assert os.path.exists("../images/validation")
    assert os.path.exists("../images/test")


def test_files_exits():
    assert len(os.listdir("../labels/training")) != 0
    assert len(os.listdir("../labels/validation")) != 0
    assert len(os.listdir("../labels/test")) != 0
    assert len(os.listdir("../images/training")) != 0
    assert len(os.listdir("../images/validation")) != 0
    assert len(os.listdir("../images/test")) != 0


def test_label_file_type():
    for filename in os.listdir("../labels/test"):
        assert filename.endswith('.txt')
    for filename in os.listdir("../labels/training"):
        assert filename.endswith('.txt')
    for filename in os.listdir("../labels/validation"):
        assert filename.endswith('.txt')


def test_image_file_type():
    for filename in os.listdir("../images/test"):
        assert filename.endswith('.png')
    for filename in os.listdir("../images/training"):
        assert filename.endswith('.png')
    for filename in os.listdir("../images/validation"):
        assert filename.endswith('.png')


def test_docstring():
    fail, attempt = doctest.testmod(moonshot)
    assert fail == 0


