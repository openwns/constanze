###############################################################################
# This file is part of openWNS (open Wireless Network Simulator)
# _____________________________________________________________________________
#
# Copyright (C) 2004-2007
# Chair of Communication Networks (ComNets)
# Kopernikusstr. 16, D-52074 Aachen, Germany
# phone: ++49-241-80-27910,
# fax: ++49-241-80-22242
# email: info@openwns.org
# www: http://www.openwns.org
# _____________________________________________________________________________
#
# openWNS is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License version 2 as published by the
# Free Software Foundation;
#
# openWNS is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openwns.module import Module
import openwns.probebus
import openwns.distribution

class Constanze(Module):
    station = None

    def __init__(self):
        super(Constanze, self).__init__("constanze", "constanze-unstable-1.0")

class Traffic(object):
    iat = None        # average interarrival time [seconds]
    packetSize = None # average packet size [bits]
    offset = None     # startTime [seconds]
    duration = None   # stopTime=startTime+duration [seconds]
    correctFRT = None # use statistically correct ForwardRecurrenceTime if True
    # duration=0.0 means: forever, no stopTime
    logger = None

    def __init__(self, parentLogger = None, **kw):
        self.logger = openwns.logger.Logger("CONST", "Traffic", True, parentLogger)
        #self.logger.level = 2
        attrsetter(self, kw)

# CBR is constant bit rate
# the most simple traffic
# absolutely no burstiness
# produces the best queueing results (delay, loss)
# unfortunately unrealistic in most cases
class CBR(Traffic):
    __plugin__ = "PointProcess" # plugin used in ConstanzeComponent.cpp
    correctFRT = True # use statistically correct ForwardRecurrenceTime if True

    def __init__(self, offset = 0.0, throughput = 1024, packetSize = 1024, duration = 0.0, parentLogger = None):
        throughput = float(throughput) # [bits/s]
        packetSize = float(packetSize) # [bits]
        self.offset = offset
        self.iat = openwns.distribution.Fixed(packetSize / throughput) # arg is mean interarrival time [s]
        self.packetSize = openwns.distribution.Fixed(packetSize)
        self.duration = duration;
        self.logger = openwns.logger.Logger("CONST", "TrafficGeneratorCBR", True, parentLogger)

# CBR0 is constant bit rate. All first packets come at once
class CBR0(Traffic):
    __plugin__ = "PointProcess" # plugin used in ConstanzeComponent.cpp
    correctFRT = False # without FRT. First packet comes at once

    def __init__(self, offset = 0.0, throughput = 1024, packetSize = 1024, duration = 0.0, parentLogger = None):
        throughput = float(throughput) # [bits/s]
        packetSize = float(packetSize) # [bits]
        self.offset = offset
        self.iat = openwns.distribution.Fixed(packetSize / throughput) # arg is mean interarrival time [s]
        self.packetSize = openwns.distribution.Fixed(packetSize)
        self.duration = duration;
        self.logger = openwns.logger.Logger("CONST", "TrafficGeneratorCBR", True, parentLogger)

# Poisson traffic is relatively harmless
# the coefficient of variation is exactly 1.0
# analytical results often only exist for this traffic type
# good for studying short-timescale queueing/delay issues
# in a longer timescale it behaves a bit worse than CBR
class Poisson(Traffic):
    __plugin__ = "PointProcess"
    correctFRT = False # not necessary for Poisson traffic

    def __init__(self, offset = 0.0, throughput = 1024, packetSize = 1024, duration = 0.0, parentLogger = None):
        throughput = float(throughput) # [bits/s]
        packetSize = float(packetSize) # [bits]
        self.offset = offset
        self.iat = openwns.distribution.NegExp(packetSize / throughput) # arg is mean interarrival time [s]
        self.packetSize = openwns.distribution.Fixed(packetSize)
        self.duration = duration;
        self.logger = openwns.logger.Logger("CONST", "TrafficGeneratorPoisson", True, parentLogger)
        #self.logger.level = 2

# ABR is commonly known as Available Bit Rate in ATM
# here we use is as Arbitrarily Adjustable Bit Rate
class ABR(Traffic):
    __plugin__ = "PointProcess"
    correctFRT = True

    def __init__(self, iatDistribution, packetSizeDistribution, offset = 0.0, duration = 0.0, parentLogger = None):
        self.iat = iatDistribution
        self.packetSize = packetSizeDistribution
        self.offset = offset
        self.duration = duration
        self.logger = openwns.logger.Logger("CONST", "TrafficGeneratorABR", True, parentLogger)
        #self.logger.level = 2
