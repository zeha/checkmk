#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore


checkname = 'carel_sensors'

info = [
    [u'1.0', u'264'], [u'2.0', u'0'], [u'3.0', u'221'], [u'4.0', u'0'],
    [u'5.0', u'0'], [u'6.0', u'0'], [u'7.0', u'0'], [u'8.0', u'0'],
    [u'9.0', u'0'], [u'10.0', u'0'], [u'11.0', u'0'], [u'12.0', u'0'],
    [u'13.0', u'0'], [u'14.0', u'0'], [u'15.0', u'0'], [u'16.0', u'491'],
    [u'17.0', u'0'], [u'18.0', u'497'], [u'19.0', u'0'], [u'20.0', u'220'],
    [u'21.0', u'150'], [u'22.0', u'0'], [u'23.0', u'170'], [u'24.0', u'0'],
    [u'25.0', u'15'], [u'26.0', u'40'], [u'27.0', u'10'], [u'28.0', u'280'],
    [u'29.0', u'160'], [u'30.0', u'70'], [u'31.0', u'200'], [u'32.0', u'70'],
    [u'33.0', u'80'], [u'34.0', u'280'], [u'35.0', u'14'], [u'36.0', u'20'],
    [u'37.0', u'3'], [u'38.0', u'0'], [u'39.0', u'0'], [u'40.0', u'2640'],
    [u'41.0', u'0'], [u'42.0', u'0'], [u'43.0', u'2200'], [u'44.0', u'1700'],
    [u'45.0', u'0'], [u'46.0', u'0'], [u'47.0', u'0'], [u'48.0', u'0'],
    [u'49.0', u'0'], [u'50.0', u'0'], [u'51.0', u'0'], [u'52.0', u'0'],
    [u'53.0', u'0'], [u'54.0', u'0'], [u'55.0', u'0'], [u'56.0', u'0'],
    [u'57.0', u'0'], [u'58.0', u'0'], [u'59.0', u'0'], [u'60.0', u'0'],
    [u'61.0', u'0'], [u'62.0', u'0'], [u'63.0', u'0'], [u'64.0', u'0'],
    [u'65.0', u'0'], [u'66.0', u'0'], [u'67.0', u'0'], [u'68.0', u'0'],
    [u'69.0', u'0'], [u'70.0', u'350'], [u'71.0', u'200'], [u'72.0', u'1000'],
    [u'73.0', u'150'], [u'74.0', u'220'], [u'75.0', u'180'], [u'76.0', u'200'],
    [u'77.0', u'491'], [u'78.0', u'150'], [u'79.0', u'0'], [u'80.0', u'0'],
    [u'81.0', u'263'], [u'82.0', u'0'], [u'83.0', u'0'], [u'84.0', u'0'],
    [u'85.0', u'0'], [u'86.0', u'-50'], [u'87.0', u'50'], [u'88.0', u'-159'],
    [u'89.0', u'750'], [u'90.0', u'850'], [u'91.0', u'498'], [u'92.0', u'0'],
    [u'93.0', u'-500'], [u'94.0', u'0'], [u'95.0', u'0'], [u'96.0', u'0'],
    [u'97.0', u'0'], [u'98.0', u'0'], [u'99.0', u'0'], [u'100.0', u'0'],
    [u'101.0', u'0'], [u'102.0', u'0'], [u'103.0', u'-500'],
    [u'104.0', u'230'], [u'105.0', u'158'], [u'106.0', u'0'], [u'107.0', u'0'],
    [u'108.0', u'0'], [u'109.0', u'0'], [u'110.0', u'0'], [u'111.0', u'0'],
    [u'112.0', u'0'], [u'113.0', u'0'], [u'114.0', u'0'], [u'115.0', u'0'],
    [u'116.0', u'0'], [u'117.0', u'0'], [u'118.0', u'0'], [u'119.0', u'0'],
    [u'120.0', u'0'], [u'121.0', u'0'], [u'122.0', u'0'], [u'123.0', u'0'],
    [u'124.0', u'0'], [u'125.0', u'0'], [u'126.0', u'0'], [u'127.0', u'0'],
    [u'128.0', u'-858993460'], [u'129.0', u'-858993460'],
    [u'130.0', u'-858993460'], [u'131.0', u'-858993460'],
    [u'132.0', u'-858993460'], [u'133.0', u'-858993460'],
    [u'134.0', u'-858993460'], [u'135.0', u'-858993460'],
    [u'136.0', u'-858993460'], [u'137.0', u'-858993460'],
    [u'138.0', u'-858993460'], [u'139.0', u'-858993460'],
    [u'140.0', u'-858993460'], [u'141.0', u'-858993460'],
    [u'142.0', u'-858993460'], [u'143.0', u'-858993460'],
    [u'144.0', u'-858993460'], [u'145.0', u'-858993460'],
    [u'146.0', u'-858993460'], [u'147.0', u'-858993460'],
    [u'148.0', u'-858993460'], [u'149.0', u'-858993460'],
    [u'150.0', u'-858993460'], [u'151.0', u'-858993460'],
    [u'152.0', u'-858993460'], [u'153.0', u'-858993460'],
    [u'154.0', u'-858993460'], [u'155.0', u'-858993460'],
    [u'156.0', u'-858993460'], [u'157.0', u'-858993460'],
    [u'158.0', u'-858993460'], [u'159.0', u'-858993460'],
    [u'160.0', u'-858993460'], [u'161.0', u'-858993460'],
    [u'162.0', u'-858993460'], [u'163.0', u'-858993460'],
    [u'164.0', u'-858993460'], [u'165.0', u'-858993460'],
    [u'166.0', u'-858993460'], [u'167.0', u'-858993460'],
    [u'168.0', u'-858993460'], [u'169.0', u'-858993460'],
    [u'170.0', u'-858993460'], [u'171.0', u'-858993460'],
    [u'172.0', u'-858993460'], [u'173.0', u'-858993460'],
    [u'174.0', u'-858993460'], [u'175.0', u'-858993460'],
    [u'176.0', u'-858993460'], [u'177.0', u'-858993460'],
    [u'178.0', u'-858993460'], [u'179.0', u'-858993460'],
    [u'180.0', u'-858993460'], [u'181.0', u'-858993460'],
    [u'182.0', u'-858993460'], [u'183.0', u'-858993460'],
    [u'184.0', u'-858993460'], [u'185.0', u'-858993460'],
    [u'186.0', u'-858993460'], [u'187.0', u'-858993460'],
    [u'188.0', u'-858993460'], [u'189.0', u'-858993460'],
    [u'190.0', u'-858993460'], [u'191.0', u'-858993460'],
    [u'192.0', u'-858993460'], [u'193.0', u'-858993460'],
    [u'194.0', u'-858993460'], [u'195.0', u'-858993460'],
    [u'196.0', u'-858993460'], [u'197.0', u'-858993460'],
    [u'198.0', u'-858993460'], [u'199.0', u'-858993460'],
    [u'200.0', u'-858993460'], [u'201.0', u'-858993460'],
    [u'202.0', u'-858993460'], [u'203.0', u'-858993460'],
    [u'204.0', u'-858993460'], [u'205.0', u'-858993460'],
    [u'206.0', u'-858993460'], [u'207.0', u'-858993460']
]

discovery = {
    '': [
        ('Cooling Prop. Band', {
            'levels': (60, 70)
        }), ('Cooling Set Point', {
            'levels': (60, 70)
        }), ('Delivery', {
            'levels': (60, 70)
        }), ('Heating Prop. Band', {
            'levels': (60, 70)
        }), ('Heating Set Point', {
            'levels': (60, 70)
        }), ('Room', {
            'levels': (30, 35)
        })
    ]
}

checks = {
    '': [
        (
            'Cooling Prop. Band', {
                'levels': (60, 70)
            }, [(0, u'15.0 \xb0C', [('temp', 15.0, 60, 70, None, None)])]
        ),
        (
            'Cooling Set Point', {
                'levels': (60, 70)
            }, [(0, u'22.0 \xb0C', [('temp', 22.0, 60, 70, None, None)])]
        ),
        (
            'Delivery', {
                'levels': (60, 70)
            }, [(0, u'22.1 \xb0C', [('temp', 22.1, 60, 70, None, None)])]
        ),
        (
            'Heating Prop. Band', {
                'levels': (60, 70)
            }, [(0, u'1.5 \xb0C', [('temp', 1.5, 60, 70, None, None)])]
        ),
        (
            'Heating Set Point', {
                'levels': (60, 70)
            }, [(0, u'17.0 \xb0C', [('temp', 17.0, 60, 70, None, None)])]
        ),
        (
            'Room', {
                'levels': (30, 35)
            }, [(0, u'26.4 \xb0C', [('temp', 26.4, 30, 35, None, None)])]
        )
    ]
}
