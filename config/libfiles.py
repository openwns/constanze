libname = 'constanze'
srcFiles = [
    'src/ConstanzeModule.cpp',
    'src/ConstanzeComponent.cpp',
    'src/ConstanzePDU.cpp',
    'src/Generator.cpp',
    'src/GeneratorPP.cpp',
    'src/Listener.cpp',
    'src/UdpBinding.cpp',
    'src/UdpListenerBinding.cpp',
    'src/TcpBinding.cpp',
    'src/TcpListenerBinding.cpp',
    'src/HMM.cpp',
    'src/BaumWelch.cpp',
    'src/Measurement.cpp'
]
hppFiles = [
    'src/BaumWelch.hpp',
    'src/Binding.hpp',
    'src/ConstanzeComponent.hpp',
    'src/ConstanzeModule.hpp',
    'src/ConstanzePDU.hpp',
    'src/Generator.hpp',
    'src/GeneratorPP.hpp',
    'src/HMM.hpp',
    'src/Listener.hpp',
    'src/Measurement.hpp',
    'src/TcpBinding.hpp',
    'src/TcpListenerBinding.hpp',
    'src/UdpBinding.hpp',
    'src/UdpListenerBinding.hpp',
]
pyconfigs = [
    'constanze/__init__.py',
    'constanze/distribution/CDFTables.py',
    'constanze/distribution/__init__.py',
    'constanze/evaluation/__init__.py',
    'constanze/evaluation/default.py',
    'constanze/module.py',
    'constanze/node.py',
    'constanze/traffic.py'
]
dependencies = []
Return('libname srcFiles hppFiles pyconfigs dependencies')
