#
# Chris Lumens <clumens@redhat.com>
#
# Copyright 2007 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use, modify,
# copy, or redistribute it subject to the terms and conditions of the GNU
# General Public License v.2.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.  Any Red Hat
# trademarks that are incorporated in the source code or documentation are not
# subject to the GNU General Public License and may only be used or replicated
# with the express permission of Red Hat, Inc. 
#
from pykickstart.version import FC4
from pykickstart.base import KickstartCommand
from pykickstart.options import KSOptionParser

class FC4_MediaCheck(KickstartCommand):
    removedKeywords = KickstartCommand.removedKeywords
    removedAttrs = KickstartCommand.removedAttrs

    def __init__(self, writePriority=0, *args, **kwargs):
        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
        self.op = self._getParser()
        self.mediacheck = kwargs.get("mediacheck", False)

    def __str__(self):
        retval = KickstartCommand.__str__(self)
        if self.mediacheck:
            retval += "mediacheck\n"

        return retval

    def _getParser(self):
        op = KSOptionParser(prog="mediacheck", description="""
                            If given, this will force anaconda to run mediacheck
                            on the installation media. This command requires that
                            installs be attended, so it is disabled by default.
                            """, version=FC4)
        return op

    def parse(self, args):
        self.op.parse_args(args=args, lineno=self.lineno)
        self.mediacheck = True
        return self
