INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PY_SERVER py_server)

FIND_PATH(
    PY_SERVER_INCLUDE_DIRS
    NAMES py_server/api.h
    HINTS $ENV{PY_SERVER_DIR}/include
        ${PC_PY_SERVER_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PY_SERVER_LIBRARIES
    NAMES gnuradio-py_server
    HINTS $ENV{PY_SERVER_DIR}/lib
        ${PC_PY_SERVER_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/py_serverTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PY_SERVER DEFAULT_MSG PY_SERVER_LIBRARIES PY_SERVER_INCLUDE_DIRS)
MARK_AS_ADVANCED(PY_SERVER_LIBRARIES PY_SERVER_INCLUDE_DIRS)
