#  Copyright (c) Kuba Szczodrzyński 2023-8-22.

from os.path import realpath

Import("env")

platform = env["PIOPLATFORM"]

# from https://github.com/sigrokproject/libserialport/blob/master/Makefile.am
env.Append(
    CPPPATH=[
        realpath("src"),
    ],
)
env.Replace(
    SRC_FILTER=[
        "+<src/serialport.c>",
        "+<src/timing.c>",
    ],
)

if platform == "windows_x86":
    env.Append(
        SRC_FILTER=[
            "+<src/windows.c>",
        ],
        # https://github.com/sigrokproject/libserialport/blob/master/release.props
        CPPDEFINES=[
            "LIBSERIALPORT_MSBUILD",
            "NDEBUG",
        ],
        # https://github.com/sigrokproject/libserialport/blob/master/common.props
        LIBS=[
            "setupapi",
        ],
    )
elif platform.startswith("linux_"):
    env.Append(
        SRC_FILTER=[
            "+<src/linux.c>",
            "+<src/linux_termios.c>",
        ],
    )
else:
    raise ValueError(f"Incompatible platform '{platform}'")
