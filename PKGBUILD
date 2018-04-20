# Script generated with Bloom
pkgdesc="ROS - franka_control provides a hardware node to control a Franka Emika research robot"
url='http://wiki.ros.org/franka_control'

pkgname='ros-kinetic-franka-control'
pkgver='0.4.0_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-controller-interface'
'ros-kinetic-controller-manager'
'ros-kinetic-franka-hw'
'ros-kinetic-franka-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-libfranka'
'ros-kinetic-message-generation'
'ros-kinetic-pluginlib'
'ros-kinetic-realtime-tools'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf2-msgs'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-controller-interface'
'ros-kinetic-controller-manager'
'ros-kinetic-franka-description'
'ros-kinetic-franka-hw'
'ros-kinetic-franka-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-joint-state-publisher'
'ros-kinetic-libfranka'
'ros-kinetic-message-runtime'
'ros-kinetic-pluginlib'
'ros-kinetic-realtime-tools'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf2-msgs'
)

conflicts=()
replaces=()

_dir=franka_control
source=()
md5sums=()

prepare() {
    cp -R $startdir/franka_control $srcdir/franka_control
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

