import sys

import PySide.QtGui as QtGui

import Objects


if __name__ == '__main__':
    q_app = QtGui.QApplication( sys.argv )
    geo_avail = q_app.desktop().availableGeometry()


    calculator = Objects.Calculator( geo_avail=geo_avail )

    q_app.exec_()
    sys.exit( 0 )