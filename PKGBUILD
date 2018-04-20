# Script generated with Bloom
pkgdesc="ROS - franka_hw provides hardware interfaces for using Franka Emika research robots with ros_control"
url='http://wiki.ros.org/franka_hw'

pkgname='ros-kinetic-franka-hw'
pkgver='0.4.0_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('gtest'
'ros-kinetic-catkin'
'ros-kinetic-controller-interface'
'ros-kinetic-franka-description'
'ros-kinetic-hardware-interface'
'ros-kinetic-joint-limits-interface'
'ros-kinetic-libfranka'
'ros-kinetic-roscpp'
'ros-kinetic-rostest'
)

depends=('ros-kinetic-controller-interface'
'ros-kinetic-hardware-interface'
'ros-kinetic-joint-limits-interface'
'ros-kinetic-libfranka'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=franka_hw
source=()
md5sums=()

prepare() {
    cp -R $startdir/franka_hw $srcdir/franka_hw
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

