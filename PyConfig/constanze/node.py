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

import openwns.node
import openwns.logger
import openwns.qos
from openwns.pyconfig import attrsetter

class Logger(openwns.logger.Logger):
    def __init__(self, name, enabled, parent = None, **kw):
        super(Logger, self).__init__("CONSTANZE", name, enabled, parent, **kw)
        openwns.logger.globalRegistry.addLogger("CONSTANZE", self)

# TODO: pack this into Measurement.py:
class Measurement(object):
    MMPPestimationResultFileName = None
    probeWindow = None
    estimatorNumberOfStates = None # for MMPP parameter estimation
    meanRateList = None
    logger = None

    def __init__(self, **kw):
        attrsetter(self, kw)

# the data sink
class Listener(object):
    domainName = None
    logger = None
    probeWindow = 1.0 # [s], 1.0 is quite slow, 0.01s=10ms is often reasonable, but may generate a lot of samples
    doMMPPestimation = False
    measurement = None # Measurement()

    def __init__(self, _domainName, parentLogger = None, **kw):
        self.domainName = _domainName
        #self.logger = wns.Logger.Logger("CONST", "Listener", True, parentLogger)
        self.logger = Logger("Listener", True, parentLogger)
        measurement = Measurement()
        attrsetter(self, kw)

class UDPBinding(object):
    nameInBindingFactory = "UdpBinding"
    # the UDP service
    udpService = "udp.connectionService"
    # UDP specific parameters
    domainName = None
    destinationDomainName = None
    destinationPort = None
    qosClass = None
    logger = None

    def __init__(self, _domainName, _destinationDomainName, _destionationPort, qosClass = openwns.qos.bestEffortQosClass, parentLogger = None):
        self.domainName = _domainName;
        self.destinationDomainName = _destinationDomainName
        self.destinationPort = _destionationPort
        self.qosClass = qosClass
        #self.logger = wns.Logger.Logger("CONST", "UDPBinding", True, parentLogger)
        self.logger = Logger("UDPBinding", True, parentLogger)

class UDPListenerBinding(object):
    nameInBindingFactory = "UdpListenerBinding"
    # the UDP service
    udpService = "udp.connectionService"
    # UDP specific parameters
    listenPort = None
    logger = None

    def __init__(self, _listenPort, parentLogger = None):
        self.listenPort = _listenPort
        #self.logger = wns.Logger.Logger("CONST", "UDPListenerBinding", True, parentLogger)
        self.logger = Logger("UDPListenerBinding", True, parentLogger)

class TCPBinding(object):
    nameInBindingFactory = "TcpBinding"
    # the TCP service
    tcpService = "tcp.connectionService"
    # TCP specific parameters
    domainName = None
    destinationDomainName = None
    destinationPort = None
    qosClass = None
    logger = None

    def __init__(self, _domainName, _destinationDomainName, _destionationPort, qosClass = openwns.qos.bestEffortQosClass, parentLogger = None):
        self.domainName = _domainName
        self.destinationDomainName = _destinationDomainName
        self.destinationPort = _destionationPort
        self.qosClass = qosClass
        #self.logger = wns.Logger.Logger("CONST", "TCPBinding", True, parentLogger)
        self.logger = Logger("TCPBinding", True, parentLogger)

class TCPListenerBinding(object):
    nameInBindingFactory = "TcpListenerBinding"
    # the TCP service
    tcpService = "tcp.connectionService"
    # TCP specific parameters
    listenPort = None
    logger = None

    def __init__(self, _listenPort, parentLogger = None):
        self.listenPort = _listenPort
        #self.logger = wns.Logger.Logger("CONST", "TCPListenerBinding", True, parentLogger)
        self.logger = Logger("TCPListenerBinding", True, parentLogger)

class BindingStub(object):
    nameInBindingFactory = "BindingStub"
    logger = None
    
    def __init__(self):
        self.logger = Logger("BindingStub", False, None)

class ConstanzeComponent(openwns.node.Component):

    nameInComponentFactory = "Constanze"
    logger = None
    generatorBindings = None
    generators = None # list of generators. A generator is a derived "class Traffic" object, see Constanze.py
    listenerBindings = None
    listeners = None
    __countGenerators__ = 0

    def __init__(self, _node, _name, parentLogger = None):
        super(ConstanzeComponent, self).__init__(_node, _name)

        #self.logger = wns.Logger.Logger("CONST", "ConstanzeComponent", True, parentLogger)
        self.logger = Logger("Constanze", True, parentLogger)
        self.generators = []
        self.generatorBindings = []
        self.listeners = []
        self.listenerBindings = []

    def addTraffic(self, _binding, _generator) :
        self.generatorBindings.append(_binding)
        self.generators.append(_generator)
        indexString = "[" +("%d" % self.__countGenerators__) + "]"
        loggerName = _binding.logger.name.split(".")[-1]
        _binding.logger.name = loggerName + indexString
        loggerName = _generator.logger.name.split(".")[-1]
        _generator.logger.name = loggerName + indexString
        self.__countGenerators__ += 1

    def addListener(self, _binding, _listener) :
        self.listenerBindings.append(_binding)
        self.listeners.append(_listener)


