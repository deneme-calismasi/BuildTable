import functools
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyButton(QPushButton):
    '''
    A special push button.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedWidth(300)
        self.setFixedHeight(30)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showMenu)
        self.dragStartPosition = 0
        self.set_style(False)
        return

    def set_style(self, blink):
        if blink:
            background = "#d3d7cf"
        else:
            background = "#2e3436"
        self.setStyleSheet(f"""
            QPushButton {{
                /* white on red */
                background-color:{background};
                color:#ffffff;
                border-color:#888a85;
                border-style:solid;
                border-width:1px;
                border-radius: 6px;
                font-family:Courier;
                font-size:10pt;
                padding:2px 2px 2px 2px;
            }}
        """)
        self.update()
        return

    def showMenu(self, pos):
        '''
        Show this popup menu when the user clicks with the right mouse button.
        '''
        menu = QMenu()
        menuAction_01 = menu.addAction("action 01")
        menuAction_02 = menu.addAction("action 02")
        menuAction_03 = menu.addAction("action 03")
        menuAction_04 = menu.addAction("action 04")
        menuAction_grab = menu.addAction("grab")
        action = menu.exec_(self.mapToGlobal(pos))
        if action == menuAction_01:
            print("clicked on action 01")
        elif action == menuAction_02:
            print("clicked on action 02")
        elif action == menuAction_03:
            print("clicked on action 03")
        elif action == menuAction_04:
            print("clicked on action 04")
        elif action == menuAction_grab:
            print("clicked on grab")
            # Start animation -> button moves to mouse pointer
            self.animate()
        return

    def animate(self):
        '''
        The button removes itself from the QScrollArea() and flies to the mouse cursor.
        For more details, see the anser of @eyllanesc at
        https://stackoverflow.com/questions/56216698/how-display-a-qpropertyanimation-on-top-of-the-qscrollarea
        '''

        def start():
            startpoint = self.window().mapFromGlobal(self.mapToGlobal(QPoint()))
            endpoint = self.window().mapFromGlobal(
                QCursor.pos() - QPoint(int(self.width() / 2), int(self.height() / 2)))
            self.setParent(self.window())
            anim = QPropertyAnimation(
                self,
                b"pos",
                self,
                duration=500,
                startValue=startpoint,
                endValue=endpoint,
                finished=blink,
            )
            anim.start()
            self.show()
            return

        def blink():
            # Flash the button to catch attention
            self.setText("GRAB ME")
            QTimer.singleShot(10, functools.partial(self.set_style, True))
            QTimer.singleShot(100, functools.partial(self.set_style, False))
            QTimer.singleShot(200, functools.partial(self.set_style, True))
            QTimer.singleShot(300, functools.partial(self.set_style, False))
            QTimer.singleShot(400, functools.partial(self.set_style, True))
            QTimer.singleShot(500, functools.partial(self.set_style, False))
            finish()
            return

        def finish():
            # After two seconds, hide the button
            # (even if user did not grab it)
            QTimer.singleShot(2000, self.hide)
            return

        start()
        return

    def start_drag(self):
        '''
        Start the drag operation.
        '''
        # 1. Start of drag-and-drop operation
        #    => button must disappear
        self.hide()

        # 2. Initiate drag-and-drop
        drag = QDrag(self)
        pixmap = QPixmap("my_pixmap.png")
        pixmap = pixmap.scaledToWidth(100, Qt.SmoothTransformation)
        drag.setPixmap(pixmap)
        mimeData = QMimeData()
        mimeData.setText("Foobar")
        drag.setMimeData(mimeData)
        dropAction = drag.exec(Qt.CopyAction | Qt.MoveAction)
        return

    def mousePressEvent(self, event):
        '''
        Left or Right mouseclick
        '''

        def leftmouse():
            print("left mouse click")
            self.dragStartPosition = event.pos()
            return

        def rightmouse():
            print("right mouse click")
            return

        if event.button() == Qt.LeftButton:
            leftmouse()
            return
        if event.button() == Qt.RightButton:
            rightmouse()
            return
        return

    def mouseMoveEvent(self, event):
        '''
        Mouse move event
        '''
        event.accept()
        if event.buttons() == Qt.NoButton:
            return
        if self.dragStartPosition is None:
            return
        if (event.pos() - self.dragStartPosition).manhattanLength() < QApplication.startDragDistance():
            return
        self.start_drag()
        return


class CustomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 300)
        self.setWindowTitle("ANIMATION & DRAG AND DROP")

        # OUTER FRAME
        # ============
        self.frm = QFrame()
        self.frm.setStyleSheet("""
            QFrame {
                background: #d3d7cf;
                border: none;
            }
        """)
        self.lyt = QHBoxLayout()
        self.frm.setLayout(self.lyt)
        self.setCentralWidget(self.frm)

        # BUTTON FRAME
        # =============
        self.btn_frm = QFrame()
        self.btn_frm.setStyleSheet("""
            QFrame {
                background: #ffffff;
                border: none;
            }
        """)
        self.btn_frm.setFixedWidth(400)
        self.btn_frm.setFixedHeight(200)
        self.btn_lyt = QVBoxLayout()
        self.btn_lyt.setAlignment(Qt.AlignTop)
        self.btn_lyt.setSpacing(5)
        self.btn_frm.setLayout(self.btn_lyt)

        # SCROLL AREA
        # ============
        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("""
            QScrollArea {
                border-style: solid;
                border-width: 1px;
            }
        """)
        self.scrollArea.setWidget(self.btn_frm)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFixedWidth(400)
        self.scrollArea.setFixedHeight(150)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.lyt.addWidget(self.scrollArea)

        # ADD BUTTONS TO BTN_LAYOUT
        # ==========================
        self.btn_lyt.addWidget(MyButton("Foo"))
        self.btn_lyt.addWidget(MyButton("Bar"))
        self.btn_lyt.addWidget(MyButton("Baz"))
        self.btn_lyt.addWidget(MyButton("Qux"))
        self.show()

        self.setAcceptDrops(True)
        return

    def dropEvent(self, event):
        event.acceptProposedAction()
        print("dropEvent at {0!s}".format(event))
        return

    def dragLeaveEvent(self, event):
        event.accept()
        return

    def dragEnterEvent(self, event):
        event.acceptProposedAction()
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Plastique'))
    myGUI = CustomMainWindow()
    sys.exit(app.exec_())
