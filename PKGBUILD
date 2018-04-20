# Script generated with Bloom
pkgdesc="ROS - franka_example_controllers provides example code for controlling Franka Emika research robots with ros_control"
url='http://wiki.ros.org/franka_example_controllers'

pkgname='ros-kinetic-franka-example-controllers'
pkgver='0.4.0_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('eigen3'
'ros-kinetic-catkin'
'ros-kinetic-controller-interface'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-franka-hw'
'ros-kinetic-geometry-msgs'
'ros-kinetic-hardware-interface'
'ros-kinetic-libfranka'
'ros-kinetic-message-generation'
'ros-kinetic-pluginlib'
'ros-kinetic-realtime-tools'
'ros-kinetic-roscpp'
)

depends=('ros-kinetic-controller-interface'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-franka-control'
'ros-kinetic-franka-description'
'ros-kinetic-franka-hw'
'ros-kinetic-geometry-msgs'
'ros-kinetic-hardware-interface'
'ros-kinetic-libfranka'
'ros-kinetic-message-runtime'
'ros-kinetic-panda-moveit-config'
'ros-kinetic-pluginlib'
'ros-kinetic-realtime-tools'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
)

conflicts=()
replaces=()

_dir=franka_example_controllers
source=()
md5sums=()

prepare() {
    cp -R $startdir/franka_example_controllers $srcdir/franka_example_controllers
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

