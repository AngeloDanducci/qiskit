# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Tests for qiskit/utils"""

from unittest import mock

from qiskit.utils.multiprocessing import local_hardware_info
from qiskit.test import QiskitTestCase


class TestUtil(QiskitTestCase):
    """Tests for qiskit/_util.py"""

    @mock.patch("platform.system", return_value="Linux")
    @mock.patch("psutil.virtual_memory")
    @mock.patch("psutil.cpu_count", return_value=None)
    def test_local_hardware_none_cpu_count(self, cpu_count_mock, vmem_mock, platform_mock):
        """Test cpu count fallback to 1 when true value can't be determined"""
        del cpu_count_mock, vmem_mock, platform_mock  # unused
        result = local_hardware_info()
        self.assertEqual(1, result["cpus"])
