srcFiles = dict()

srcFiles['BASE'] = [
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


srcFiles['TEST'] = [
    ]

Return('srcFiles')
