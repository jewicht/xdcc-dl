"""
LICENSE:
Copyright 2015,2016 Hermann Krumrey

This file is part of toktokkie.

    toktokkie is a program that allows convenient managing of various
    local media collections, mostly focused on video.

    toktokkie is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    toktokkie is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with toktokkie.  If not, see <http://www.gnu.org/licenses/>.
LICENSE
"""

# imports
import os
import unittest
from xdcc_dl.entities.XDCCPack import XDCCPack
from xdcc_dl.entities.Progress import Progress
from xdcc_dl.entities.IrcServer import IrcServer
from xdcc_dl.xdcc.XDCCDownloader import XDCCDownloader


class UnitTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        if os.path.isfile("1_test.txt"):
            os.remove("1_test.txt")
        if os.path.isfile("2_test.txt"):
            os.remove("2_test.txt")
        if os.path.isfile("3_test.txt"):
            os.remove("3_test.txt")

    def test_download_multiple_packs_same_server(self):

        progress = Progress(2)

        downloader = XDCCDownloader("irc.namibsun.net", "random")
        downloader.download([XDCCPack(IrcServer("irc.namibsun.net"), "xdcc_servbot", 2),
                             XDCCPack(IrcServer("irc.namibsun.net"), "xdcc_servbot", 3)], progress)

        self.assertTrue(os.path.isfile("2_test.txt"))
        self.assertTrue(os.path.isfile("3_test.txt"))

        self.assertEqual(progress.get_single_progress_percentage(), 100.0)
        self.assertEqual(progress.get_total_percentage(), 100.0)
