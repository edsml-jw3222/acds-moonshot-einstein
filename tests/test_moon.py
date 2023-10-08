import sys
sys.path.append(".")
import moon_dataset_maker # noqa
import numpy as np # noqa
import cv2 # noqa


class Test_dataset_maker:
    """
    Class for testing the functions within moon_dataset_maker.
    """

    def test_haversine(self):
        output = moon_dataset_maker.haversine(20, 40, 40, 50)
        expected = 659.78139
        assert np.allclose(output, expected, rtol=1e-4)

    def test_index_degree_convert(self):
        output = moon_dataset_maker.index_degree_convert(
            [1000, 1000], 13646, 27291, name="B"
        )
        expected = np.array([41.70233035321706, -176.70220951962185])
        assert np.allclose(output, expected)

    def test_random_pick(self):
        folder, region, _, _ = moon_dataset_maker.random_pick(
            "labels/lunar_crater_database_robbins_train.csv",
            cv2.imread("images/" + "Lunar_B.jpg"),
            n=1,
            output="train",
            name="B",
        )
        expected_shape = 416 * 2
        expected_len = 2
        assert np.isclose(folder[0].shape[0], expected_shape)
        assert np.isclose(len(region[0]), expected_len)
    # Other functions are proven to be able to work in ipynb.
