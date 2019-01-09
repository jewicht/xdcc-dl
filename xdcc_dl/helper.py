"""LICENSE
Copyright 2016 Hermann Krumrey <hermann@krumreyh.com>

This file is part of xdcc-dl.

xdcc-dl is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

xdcc-dl is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with xdcc-dl.  If not, see <http://www.gnu.org/licenses/>.
LICENSE"""

import sys
import logging
from typing import List
from argparse import Namespace
from xdcc_dl.logging import Logger
from xdcc_dl.entities.XDCCPack import XDCCPack
from xdcc_dl.xdcc.XDCCClient import XDCCCLient


def set_throttle_value(throttle_string: str):
    """
    Sets the throttle value of the XDCC Client globally based on a string in
    the form <Bytes><|k|m|g> (kilo, mega, giga)
    :param throttle_string: The string to parse
    :return: None
    """
    try:
        if throttle_string is not None:
            multiplier = 1
            units = {"k": 1000, "m": 1000000, "g": 1000000000}
            throttle_num = ""
            for i, char in enumerate(throttle_string):
                if char.isdigit():
                    throttle_num += char
                else:
                    if len(throttle_string) - 1 != i:
                        raise KeyError
                    else:
                        multiplier = units[char.lower()]
            limit = multiplier * int(throttle_num)
            XDCCCLient.download_limit = limit
    except KeyError:
        print("Invalid throttle value")
        sys.exit(1)


def set_logging_level(args: Namespace):

    if args.quiet:
        log_level = logging.ERROR
    elif args.verbose:
        log_level = logging.INFO
    elif args.debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.WARNING
    Logger.logging_level = log_level


def prepare_packs(args: Namespace, packs: List[XDCCPack]):

    if args.out is not None:
        if len(packs) == 1:
            packs[0].set_filename(args.out, True)
        else:
            for i, pack in enumerate(packs):
                pack.set_filename(args.out + "-" + str(i).zfill(3), True)
