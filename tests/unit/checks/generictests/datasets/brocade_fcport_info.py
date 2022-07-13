#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore

checkname = 'brocade_fcport'

info = [[
    [
        u'1', u'6', u'1', u'1', u'1310134522', u'4177440995', u'1324413930', u'1565457526',
        u'1475618600', u'0', u'0', u'0', u'0', u'', u'port0'
    ],
    [
        u'2', u'6', u'1', u'1', u'3008021003', u'3964905811', u'3109557888', u'589549056',
        u'1475618600', u'0', u'0', u'0', u'0', u'', u'port1'
    ],
    [
        u'3', u'6', u'1', u'1', u'2782145207', u'1772824069', u'1118630179', u'1514486294',
        u'1475618600', u'0', u'0', u'0', u'0', u'', u'port2'
    ],
    [
        u'4', u'6', u'1', u'1', u'3834185164', u'854870244', u'607528486', u'1718780473',
        u'1475618600', u'0', u'0', u'0', u'0', u'', u'port3'
    ],
    [u'5', u'6', u'1', u'1', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port4'],
    [u'6', u'6', u'1', u'1', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port5'],
    [u'7', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port6'],
    [u'8', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port7'],
    [u'9', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port8'],
    [
        u'10', u'6', u'1', u'1', u'3340536595', u'958647746', u'3657835219', u'330709967',
        u'8226777', u'0', u'0', u'0', u'0', u'', u'port9'
    ],
    [
        u'11', u'6', u'1', u'1', u'901915570', u'3576422340', u'83022930', u'309653488', u'8607141',
        u'0', u'0', u'0', u'0', u'', u'port10'
    ],
    [u'12', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port11'],
    [u'13', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port12'],
    [u'14', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port13'],
    [
        u'15', u'6', u'1', u'1', u'2313575', u'1904259', u'194633', u'118130', u'0', u'0', u'0',
        u'10', u'0', u'', u'port14'
    ],
    [u'16', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port15'],
    [
        u'17', u'6', u'1', u'1', u'1994754228', u'2017140248', u'183248159', u'118657339', u'0',
        u'0', u'0', u'2', u'1', u'', u'port16'
    ],
    [
        u'18', u'4', u'2', u'2', u'36802', u'31530', u'2179', u'2018', u'0', u'0', u'0', u'0', u'0',
        u'', u'port17'
    ],
    [
        u'19', u'4', u'2', u'2', u'2783974', u'31530', u'231110', u'2018', u'0', u'0', u'0', u'0',
        u'0', u'', u'port18'
    ],
    [
        u'20', u'6', u'1', u'1', u'73931586', u'64532994', u'4465322', u'3969508', u'71', u'0',
        u'0', u'0', u'0', u'', u'port19'
    ],
    [
        u'21', u'6', u'1', u'1', u'3192010393', u'2004454826', u'2192508727', u'1169747011',
        u'2018496', u'0', u'0', u'24', u'0', u'', u'port20'
    ],
    [
        u'22', u'6', u'1', u'1', u'620671219', u'2141299547', u'1289267355', u'1877851293',
        u'669695', u'0', u'0', u'33', u'0', u'', u'port21'
    ],
    [u'23', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port22'],
    [
        u'24', u'6', u'1', u'1', u'3510202310', u'1784857731', u'1778140500', u'673527753',
        u'15823', u'0', u'0', u'0', u'0', u'', u'port23'
    ],
    [
        u'25', u'6', u'1', u'1', u'3700914499', u'994117016', u'2312658432', u'3028585743',
        u'15717', u'0', u'0', u'0', u'0', u'', u'port24'
    ],
    [
        u'26', u'6', u'1', u'1', u'1362269713', u'3748554767', u'936880806', u'3850931267',
        u'228547', u'0', u'0', u'0', u'0', u'', u'port25'
    ],
    [
        u'27', u'6', u'1', u'1', u'195245792', u'20816', u'16270173', u'1290', u'0', u'0', u'0',
        u'0', u'0', u'', u'port26'
    ],
    [
        u'28', u'6', u'1', u'1', u'1808905154', u'2884029736', u'3666064819', u'4089712868',
        u'4261731', u'0', u'0', u'42906', u'0', u'', u'port27'
    ],
    [u'29', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port28'],
    [u'30', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port29'],
    [u'31', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port30'],
    [u'32', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'', u'port31'],
    [
        u'33', u'6', u'1', u'1', u'5475442', u'1696', u'456256', u'32', u'0', u'0', u'0', u'0',
        u'0', u'', u'port32'
    ],
    [
        u'34', u'6', u'1', u'1', u'3321428066', u'3156624427', u'178039190', u'1644198836',
        u'12684', u'0', u'0', u'0', u'0', u'', u'port33'
    ],
    [
        u'35', u'6', u'1', u'1', u'3667331766', u'769720586', u'4245147266', u'2657068859',
        u'45541', u'0', u'0', u'0', u'0', u'', u'port34'
    ],
    [
        u'36', u'6', u'1', u'1', u'3872978704', u'2336900500', u'300844217', u'289639351',
        u'6502923', u'0', u'0', u'0', u'0', u'', u'port35'
    ],
    [
        u'37', u'6', u'1', u'1', u'609289056', u'946007048', u'1915530030', u'3670690863',
        u'4065058886', u'0', u'0', u'0', u'15', u'', u'port36'
    ],
    [
        u'38', u'6', u'1', u'1', u'476134820', u'3360456335', u'2356132728', u'3493285257',
        u'4065058886', u'0', u'0', u'0', u'1', u'', u'port37'
    ],
    [
        u'39', u'6', u'1', u'1', u'417527049', u'1840377071', u'3140988738', u'3653325568',
        u'3006167201', u'0', u'0', u'0', u'11', u'', u'port38'
    ],
    [
        u'40', u'6', u'1', u'1', u'2198503862', u'2718204125', u'1129084317', u'3528468924',
        u'3006167201', u'0', u'0', u'0', u'0', u'', u'port39'
    ]
],
        [[u'1', u'128'], [u'2', u'128'], [u'3', u'128'], [u'4', u'128'], [u'37', u'128'],
         [u'38', u'128'], [u'39', u'128'], [u'40', u'128']],
        [[u'805306369', u'6', u'100'], [u'805306370', u'24', u'100'], [u'805306371', u'131', u'0'],
         [u'805306372', u'1', u'0'], [u'805306373', u'1', u'0'], [u'805306374', u'1', u'0'],
         [u'1073741824', u'56', u'8000'], [u'1073741825', u'56', u'8000'],
         [u'1073741826', u'56', u'8000'], [u'1073741827', u'56', u'8000'],
         [u'1073741828', u'56', u''], [u'1073741829', u'56', u'8000'],
         [u'1073741830', u'56', u'8000'], [u'1073741831', u'56', u'8000'],
         [u'1073741832', u'56', u'8000'], [u'1073741833', u'56', u'8000'],
         [u'1073741834', u'56', u'8000'], [u'1073741835', u'56', u'8000'],
         [u'1073741836', u'56', u'8000'], [u'1073741837', u'56', u'8000'],
         [u'1073741838', u'56', u'8000'], [u'1073741839', u'56', u'8000'],
         [u'1073741840', u'56', u'4000'], [u'1073741841', u'56', u'8000'],
         [u'1073741842', u'56', u'8000'], [u'1073741843', u'56', u'8000'],
         [u'1073741844', u'56', u'8000'], [u'1073741845', u'56', u'8000'],
         [u'1073741846', u'56', u'8000'], [u'1073741847', u'56', u'8000'],
         [u'1073741848', u'56', u'8000'], [u'1073741849', u'56', u'8000'],
         [u'1073741850', u'56', u'8000'], [u'1073741851', u'56', u'8000'],
         [u'1073741852', u'56', u'8000'], [u'1073741853', u'56', u'8000'],
         [u'1073741854', u'56', u'8000'], [u'1073741855', u'56', u'8000'],
         [u'1073741856', u'56', u'8000'], [u'1073741857', u'56', u'8000'],
         [u'1073741858', u'56', u'8000'], [u'1073741859', u'56', u'8000'],
         [u'1073741860', u'56', u'8000'], [u'1073741861', u'56', u'8000'],
         [u'1073741862', u'56', u'8000'], [u'1073741863', u'56', u'8000']], []]

discovery = {
    '': [(u'00 ISL port0', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'01 ISL port1', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'02 ISL port2', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'03 ISL port3', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'04 port4', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'05 port5', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'09 port9', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'10 port10', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'14 port14', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'16 port16', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'19 port19', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'20 port20', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'21 port21', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'23 port23', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'24 port24', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'25 port25', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'26 port26', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'27 port27', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'32 port32', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'33 port33', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'34 port34', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'35 port35', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'36 ISL port36', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'37 ISL port37', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'38 ISL port38', '{ "phystate": [6], "opstate": [1], "admstate": [1] }'),
         (u'39 ISL port39', '{ "phystate": [6], "opstate": [1], "admstate": [1] }')]
}

checks = {
    '': [(u'00 ISL port0', {
        'admstate': [1],
        'assumed_speed': 2.0,
        'c3discards': (3.0, 20.0),
        'notxcredits': (3.0, 20.0),
        'opstate': [1],
        'phystate': [6],
        'rxcrcs': (3.0, 20.0),
        'rxencinframes': (3.0, 20.0),
        'rxencoutframes': (3.0, 20.0)
    }, [(
        0,
        'ISL speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
        [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
         ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
         ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None, None),
         ('rxencinframes', 0.0, None, None, None, None), ('c3discards', 0.0, None, None, None,
                                                          None),
         ('notxcredits', 0.0, None, None, None, None)])]),
         (u'01 ISL port1', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'ISL speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'02 ISL port2', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'ISL speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'03 ISL port3', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'ISL speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'04 port4', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Assumed speed: 2 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 200000000.0), ('out', 0.0, None, None, 0, 200000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'05 port5', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'09 port9', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'10 port10', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'14 port14', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'16 port16', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 4 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 400000000.0), ('out', 0.0, None, None, 0, 400000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'19 port19', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'20 port20', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'21 port21', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'23 port23', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'24 port24', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'25 port25', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'26 port26', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'27 port27', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'32 port32', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'33 port33', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'34 port34', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'35 port35', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'Speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'36 ISL port36', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'ISL speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'37 ISL port37', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'ISL speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'38 ISL port38', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'ISL speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])]),
         (u'39 ISL port39', {
             'admstate': [1],
             'assumed_speed': 2.0,
             'c3discards': (3.0, 20.0),
             'notxcredits': (3.0, 20.0),
             'opstate': [1],
             'phystate': [6],
             'rxcrcs': (3.0, 20.0),
             'rxencinframes': (3.0, 20.0),
             'rxencoutframes': (3.0, 20.0)
         },
          [(0,
            'ISL speed: 8 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
            [('in', 0.0, None, None, 0, 800000000.0), ('out', 0.0, None, None, 0, 800000000.0),
             ('rxframes', 0.0, None, None, None, None), ('txframes', 0.0, None, None, None, None),
             ('rxcrcs', 0.0, None, None, None, None), ('rxencoutframes', 0.0, None, None, None,
                                                       None),
             ('rxencinframes', 0.0, None, None, None, None),
             ('c3discards', 0.0, None, None, None, None),
             ('notxcredits', 0.0, None, None, None, None)])])]
}
