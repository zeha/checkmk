#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore



checkname = 'openhardwaremonitor'


info = [[u'Index', u'Name', u'Parent', u'SensorType', u'Value'],
        [u'0', u'Temperature', u'/hdd/0', u'Temperature', u'28.000000'],
        [u'0', u'System Fan', u'/lpc/w83627dhgp', u'Fan', u'1506.696411'],
        [u'1', u'CPU Fan', u'/lpc/w83627dhgp', u'Fan', u'2518.656738'],
        [u'1', u'CPU Cores', u'/intelcpu/0', u'Power', u'1.651155'],
        [u'0', u'CPU Core #1', u'/intelcpu/0', u'Temperature', u'28.000000'],
        [u'0', u'Remaining Life', u'/hdd/0', u'Level', u'98.000000'],
        [u'1', u'CPU Core #1', u'/intelcpu/0', u'Clock', u'1297.013062'],
        [u'1', u'CPU Core #1', u'/intelcpu/0', u'Load', u'12.307692'],
        [u'2', u'CPU Core #2', u'/intelcpu/0', u'Clock', u'1297.013062'],
        [u'0', u'Memory', u'/ram', u'Load', u'61.928921'],
        [u'2', u'CPU Graphics', u'/intelcpu/0', u'Power', u'0.040867'],
        [u'1', u'CPU Core #2', u'/intelcpu/0', u'Temperature', u'29.000000'],
        [u'3', u'CPU DRAM', u'/intelcpu/0', u'Power', u'1.188020'],
        [u'2', u'CPU Core #3', u'/intelcpu/0', u'Temperature', u'31.000000'],
        [u'1', u'Host Writes to Controller', u'/hdd/0', u'Data', u'1589.000000'],
        [u'2', u'Host Reads', u'/hdd/0', u'Data', u'1366.000000'],
        [u'4', u'CPU Core #4', u'/intelcpu/0', u'Load', u'6.153846'],
        [u'3', u'CPU Core #3', u'/intelcpu/0', u'Clock', u'1297.013062'],
        [u'3', u'CPU Core #3', u'/intelcpu/0', u'Load', u'18.461536'],
        [u'4', u'CPU Core #4', u'/intelcpu/0', u'Clock', u'1297.013062'],
        [u'1', u'Available Memory', u'/ram', u'Data', u'3.011536'],
        [u'2', u'CPU Core #2', u'/intelcpu/0', u'Load', u'15.384615'],
        [u'0', u'Controller Writes to NAND', u'/hdd/0', u'Data', u'3371.000000'],
        [u'1', u'Write Amplification', u'/hdd/0', u'Factor', u'2.121460'],
        [u'0', u'CPU Total', u'/intelcpu/0', u'Load', u'13.076920'],
        [u'0', u'Bus Speed', u'/intelcpu/0', u'Clock', u'99.770233'],
        [u'0', u'Used Memory', u'/ram', u'Data', u'4.898762'],
        [u'3', u'CPU Core #4', u'/intelcpu/0', u'Temperature', u'27.000000'],
        [u'4', u'CPU Package', u'/intelcpu/0', u'Temperature', u'31.000000'],
        [u'0', u'Used Space', u'/hdd/0', u'Load', u'72.429222']]


discovery = {'': [(u'cpu0 Bus Speed', {}),
                  (u'cpu0 Core #1', {}),
                  (u'cpu0 Core #2', {}),
                  (u'cpu0 Core #3', {}),
                  (u'cpu0 Core #4', {})],
             'fan': [(u'lpcw83627dhgp Fan', {}), (u'lpcw83627dhgp System Fan', {})],
             'power': [(u'cpu0 Cores', {}), (u'cpu0 DRAM', {}), (u'cpu0 Graphics', {})],
             'smart': [(u'hdd0', {})],
             'temperature': [(u'cpu0 Core #1', {}),
                             (u'cpu0 Core #2', {}),
                             (u'cpu0 Core #3', {}),
                             (u'cpu0 Core #4', {}),
                             (u'cpu0 Package', {}),
                             (u'hdd0', {})]}


checks = {'': [(u'cpu0 Bus Speed',
                {},
                [(0, '99.8 MHz', [('clock', 99.770233, None, None, None, None)])]),
               (u'cpu0 Core #1',
                {},
                [(0, '1297.0 MHz', [('clock', 1297.013062, None, None, None, None)])]),
               (u'cpu0 Core #2',
                {},
                [(0, '1297.0 MHz', [('clock', 1297.013062, None, None, None, None)])]),
               (u'cpu0 Core #3',
                {},
                [(0, '1297.0 MHz', [('clock', 1297.013062, None, None, None, None)])]),
               (u'cpu0 Core #4',
                {},
                [(0, '1297.0 MHz', [('clock', 1297.013062, None, None, None, None)])])],
          'fan': [(u'lpcw83627dhgp Fan',
                   {'lower': (None, None), 'upper': (None, None)},
                   [(0, 'Speed: 2518 RPM', [])]),
                  (u'lpcw83627dhgp System Fan',
                   {'lower': (None, None), 'upper': (None, None)},
                   [(0, 'Speed: 1506 RPM', [])])],
          'power': [(u'cpu0 Cores',
                     {},
                     [(0, '1.7 W', [('w', 1.651155, None, None, None, None)])]),
                    (u'cpu0 DRAM',
                     {},
                     [(0, '1.2 W', [('w', 1.18802, None, None, None, None)])]),
                    (u'cpu0 Graphics',
                     {},
                     [(0, '0.0 W', [('w', 0.040867, None, None, None, None)])])],
          'smart': [(u'hdd0',
                     {'remaining_life': (30, 10)},
                     [(0,
                       'Remaining Life 98.0%',
                       [('remaining_life', 98.0, None, None, None, None)])])],
          'temperature': [(u'cpu0 Core #1',
                           {'_default': {'levels': (70, 80)},
                            'cpu': {'levels': (60, 70)},
                            'hdd': {'levels': (40, 50)}},
                           [(0, u'28.0 \xb0C', [('temp', 28.0, 60, 70, None, None)])]),
                          (u'cpu0 Core #2',
                           {'_default': {'levels': (70, 80)},
                            'cpu': {'levels': (60, 70)},
                            'hdd': {'levels': (40, 50)}},
                           [(0, u'29.0 \xb0C', [('temp', 29.0, 60, 70, None, None)])]),
                          (u'cpu0 Core #3',
                           {'_default': {'levels': (70, 80)},
                            'cpu': {'levels': (60, 70)},
                            'hdd': {'levels': (40, 50)}},
                           [(0, u'31.0 \xb0C', [('temp', 31.0, 60, 70, None, None)])]),
                          (u'cpu0 Core #4',
                           {'_default': {'levels': (70, 80)},
                            'cpu': {'levels': (60, 70)},
                            'hdd': {'levels': (40, 50)}},
                           [(0, u'27.0 \xb0C', [('temp', 27.0, 60, 70, None, None)])]),
                          (u'cpu0 Package',
                           {'_default': {'levels': (70, 80)},
                            'cpu': {'levels': (60, 70)},
                            'hdd': {'levels': (40, 50)}},
                           [(0, u'31.0 \xb0C', [('temp', 31.0, 60, 70, None, None)])]),
                          (u'hdd0',
                           {'_default': {'levels': (70, 80)},
                            'cpu': {'levels': (60, 70)},
                            'hdd': {'levels': (40, 50)}},
                           [(0, u'28.0 \xb0C', [('temp', 28.0, 40, 50, None, None)])])]}
