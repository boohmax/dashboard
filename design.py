from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication,
    QFrame, QLabel, QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)
import data_function
import report_model



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        #self.centralwidget.setMinimumSize(900, 500)
        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 100, 500))
        self.menu.setFrameShape(QFrame.NoFrame)
        self.menu.setFrameShadow(QFrame.Raised)
        self.DP = QPushButton('DP', self.menu)
        self.DP.setObjectName(u"DP")
        self.DP.setGeometry(QRect(5, 10, 90, 20))
        self.Model = QPushButton('Model', self.menu)
        self.Model.setObjectName(u"Model")
        self.Model.setGeometry(QRect(5, 40, 90, 20))
        self.Clear = QPushButton('Clear', self.menu)
        self.Clear.setObjectName(u"Clear")
        self.Clear.setGeometry(QRect(5, 70, 90, 20))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(100, 0, 800, 500))
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        
        def makeScrollAreaContents():
            self.scrollAreaWidgetContents = QWidget()
            self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
            self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 800, 500))
            self.scrollAreaWidgetContents.setMinimumSize(100, 2000)
            self.scrollAreaWidgetContentsLayout = QVBoxLayout()
            self.scrollAreaWidgetContentsLayout.addWidget(self.scrollAreaWidgetContents)

        def update_scroll_area():
            for i in reversed(range(self.scrollAreaWidgetContentsLayout.count())): 
                self.scrollAreaWidgetContentsLayout.itemAt(i).widget().deleteLater()
        

        def make_DP_card():
            data = data_function.restructed_data_DP(data_function.load_data_DP())
            card_width = 145
            card_height = 150
            
            count_card = 0
            count_card_row = 0
            card_x = 10
            card_y = 10

            x = 0
            y = 0

            nest_data = data_function.nest_list(data, 5)

            makeScrollAreaContents()

            for x in range(len(nest_data)):
                for y in range(len(nest_data[x])):
                    self.body_info = QFrame(self.scrollAreaWidgetContents)
                    self.body_info.setObjectName(u"body_info")
                    self.body_info.setGeometry(
                        QRect(card_x, card_y, card_width, card_height)
                        )
                    self.body_info.setMinimumSize(QSize(card_width, card_height))
                    self.body_info.setFrameShape(QFrame.Box)
                    self.body_info.setFrameShadow(QFrame.Raised)
                    self.body_info.setLineWidth(1)
                    self.verticalLayout = QVBoxLayout(self.body_info)
                    self.verticalLayout.setObjectName(u"verticalLayout")
                    self.label = QLabel(self.body_info)
                    self.label.setObjectName(u"label")
                    self.label.setAlignment(Qt.AlignCenter)
                    self.label.setText(nest_data[x][y]['DP'])

                    self.verticalLayout.addWidget(self.label)

                    self.D_progress = QLabel(self.body_info)
                    self.D_progress.setObjectName(u"D_progress")
                    self.D_progress.setAlignment(Qt.AlignCenter)

                    if nest_data[x][y].get('DRW_D')\
                        and nest_data[x][y].get('DRW_D_all'):
                        self.D_progress.setText(
                            'D %d/%d' % (nest_data[x][y]['DRW_D'],
                            nest_data[x][y]['DRW_D_all'])
                            )
                        if nest_data[x][y].get('DRW_D')\
                            == nest_data[x][y].get('DRW_D_all'):
                            self.D_progress.setStyleSheet('''
                                background-color: #FFFFFF;
                                ''')
                        else:
                            self.D_progress.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    elif nest_data[x][y].get('DRW_D_all'):
                        self.D_progress.setText(
                            'D 0/%d' % (nest_data[x][y]['DRW_D_all'])
                            )
                        self.D_progress.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    else:
                        self.D_progress.setText('No D')
                        self.D_progress.setStyleSheet('''
                            background-color: #FFFFFF;
                            ''')

                    self.verticalLayout.addWidget(self.D_progress)


                    self.M_progress = QLabel(self.body_info)
                    self.M_progress.setObjectName(u"M_progress")
                    self.M_progress.setAlignment(Qt.AlignCenter)

                    if nest_data[x][y].get('DRW_M')\
                        and nest_data[x][y].get('DRW_M_all'):
                        self.M_progress.setText(
                            'M %d/%d' % (nest_data[x][y]['DRW_M'],
                            nest_data[x][y]['DRW_M_all'])
                            )
                        if nest_data[x][y].get('DRW_M')\
                            == nest_data[x][y].get('DRW_M_all'):
                            self.M_progress.setStyleSheet('''
                                background-color: #FFFFFF;
                                ''')
                        else:
                            self.M_progress.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    elif nest_data[x][y].get('DRW_M_all'):
                        self.M_progress.setText(
                            'M 0/%d' % (nest_data[x][y]['DRW_M_all'])
                            )
                        self.M_progress.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    else:
                        self.M_progress.setText('No M')
                        self.M_progress.setStyleSheet('''
                            background-color: #FFFFFF;
                            ''')

                    self.verticalLayout.addWidget(self.M_progress)


                    self.SA_progress = QLabel(self.body_info)
                    self.SA_progress.setObjectName(u"SA_progress")
                    self.SA_progress.setAlignment(Qt.AlignCenter)

                    if nest_data[x][y].get('DRW_SA')\
                        and nest_data[x][y].get('DRW_SA_all'):                    
                        self.SA_progress.setText(
                            'SA %d/%d' % (nest_data[x][y]['DRW_SA'],
                            nest_data[x][y]['DRW_SA_all'])
                            )
                        if nest_data[x][y].get('DRW_SA')\
                            == nest_data[x][y].get('DRW_SA_all'):
                            self.SA_progress.setStyleSheet('''
                                background-color: #FFFFFF;
                                ''')
                        else:
                            self.SA_progress.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    elif nest_data[x][y].get('DRW_SA_all'):
                        self.SA_progress.setText(
                            'SA 0/%d' % (nest_data[x][y]['DRW_SA_all'])
                            )
                        self.SA_progress.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    else:
                        self.SA_progress.setText('No SA')
                        self.SA_progress.setStyleSheet('''
                                background-color: #FFFFFF;
                                ''')

                    self.verticalLayout.addWidget(self.SA_progress)

                    #Style for DP frame
                    if (nest_data[x][y].get('DRW_D')
                        != nest_data[x][y].get('DRW_D_all')
                        or nest_data[x][y].get('DRW_M')
                        != nest_data[x][y].get('DRW_M_all')
                        or nest_data[x][y].get('DRW_SA')
                        != nest_data[x][y].get('DRW_SA_all')):
                        self.body_info.setStyleSheet('''
                            background-color: #7F7F7F;
                            ''')
                    else:
                        self.body_info.setStyleSheet('''
                            background-color: #FFFFFF;
                            ''')


                    card_x += 155

                card_x = 10
                card_y += 160

            self.scrollAreaWidgetContents\
                .setMinimumSize(100, int(len(data)/5*170))
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.scrollAreaWidgetContents.show()


        def make_model_card():

            data = data_function.load_data_model()
            card_width = 145
            card_height = 150
            
            count_card = 0
            count_card_row = 0
            card_x = 10
            card_y = 10

            x = 0
            y = 0

            nest_data = data_function.nest_list(data, 5)

            makeScrollAreaContents()

            for x in range(len(nest_data)):
                for y in range(len(nest_data[x])):
                    self.body_info = QFrame(self.scrollAreaWidgetContents)
                    self.body_info.setObjectName(u"body_info")
                    self.body_info.setGeometry(
                        QRect(card_x, card_y, card_width, card_height)
                        )
                    self.body_info.setMinimumSize(
                        QSize(card_width, card_height))
                    self.body_info.setFrameShape(QFrame.Box)
                    self.body_info.setFrameShadow(QFrame.Raised)
                    self.body_info.setLineWidth(1)
                    self.verticalLayout = QVBoxLayout(self.body_info)
                    self.verticalLayout.setObjectName(u"verticalLayout")
                    self.label = QLabel(self.body_info)
                    self.label.setObjectName(u"label")
                    self.label.setAlignment(Qt.AlignCenter)
                    self.label.setText(nest_data[x][y]['DP'])

                    self.verticalLayout.addWidget(self.label)

                    self.dp_sent = QLabel(self.body_info)
                    self.dp_sent.setObjectName(u"dp_sent")
                    self.dp_sent.setAlignment(Qt.AlignCenter)

                    if nest_data[x][y].get('Выдано'):
                        self.dp_sent.setText(
                            'Выдано: %s' % (nest_data[x][y]['Выдано'])
                            )
                        if nest_data[x][y].get('Выдано') != 'None':
                            self.dp_sent.setStyleSheet('''
                                background-color: #FFFFFF;
                                ''')
                        else:
                            self.dp_sent.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    
                    self.verticalLayout.addWidget(self.dp_sent)

                    self.dp_model = QLabel(self.body_info)
                    self.dp_model.setObjectName(u"dp_model")
                    self.dp_model.setAlignment(Qt.AlignCenter)

                    if nest_data[x][y].get('Модель'):
                        self.dp_model.setText(
                            'Модель: %s' % (nest_data[x][y]['Модель'])
                            )
                        if nest_data[x][y].get('Модель') != 'None':
                            self.dp_model.setStyleSheet('''
                                background-color: #FFFFFF;
                                ''')
                        else:
                            self.dp_model.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    
                    self.verticalLayout.addWidget(self.dp_model)

                    self.dp_drawing = QLabel(self.body_info)
                    self.dp_drawing.setObjectName(u"dp_drawing")
                    self.dp_drawing.setAlignment(Qt.AlignCenter)

                    if nest_data[x][y].get('чертежи'):
                        self.dp_drawing.setText(
                            'Чертежи: %s' % (nest_data[x][y]['чертежи'])
                            )
                        if nest_data[x][y].get('чертежи') != 'None':
                            self.dp_drawing.setStyleSheet('''
                                background-color: #FFFFFF;
                                ''')
                        else:
                            self.dp_drawing.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    
                    self.verticalLayout.addWidget(self.dp_drawing)

                    self.dp_erection_drawing = QLabel(self.body_info)
                    self.dp_erection_drawing.setObjectName(
                        u"dp_erection_drawing"
                        )
                    self.dp_erection_drawing.setAlignment(Qt.AlignCenter)

                    if nest_data[x][y].get('МС'):
                        self.dp_erection_drawing.setText(
                            'МС: %s' % (nest_data[x][y]['МС'])
                            )
                        if nest_data[x][y].get('МС') != 'None':
                            self.dp_erection_drawing.setStyleSheet('''
                                background-color: #FFFFFF;
                                ''')
                        else:
                            self.dp_erection_drawing.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    
                    self.verticalLayout.addWidget(self.dp_erection_drawing)

                    self.dp_revision = QLabel(self.body_info)
                    self.dp_revision.setObjectName(u"dp_revision")
                    self.dp_revision.setAlignment(Qt.AlignCenter)

                    if nest_data[x][y].get('ревизия'):
                        self.dp_revision.setText(
                            'Ревизия: %s' % (nest_data[x][y]['ревизия'])
                            )
                        if nest_data[x][y].get('ревизия') != 'None':
                            self.dp_revision.setStyleSheet('''
                                background-color: #FFFFFF;
                                ''')
                        else:
                            self.dp_revision.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    
                    self.verticalLayout.addWidget(self.dp_revision)

                    self.dp_date = QLabel(self.body_info)
                    self.dp_date.setObjectName(u"dp_revision")
                    self.dp_date.setAlignment(Qt.AlignCenter)

                    if nest_data[x][y].get('First Issuance Forecast date'):
                        self.dp_date.setText(
                            'Дата: %s' %
                            (nest_data[x][y]['First Issuance Forecast date'])
                            )
                        if nest_data[x][y].get('First Issuance Forecast date')\
                            != 'None':
                            self.dp_date.setStyleSheet('''
                                background-color: #FFFFFF;
                                ''')
                        else:
                            self.dp_date.setStyleSheet('''
                                background-color: #FBF37C;
                                ''')
                    
                    self.verticalLayout.addWidget(self.dp_date)


                    #Style for DP frame
                    if (nest_data[x][y].get('Выдано') == 'None'
                        ):
                        self.body_info.setStyleSheet('''
                            background-color: #7F7F7F;
                            ''')
                    else:
                        self.body_info.setStyleSheet('''
                            background-color: #FFFFFF;
                            ''')

                    card_x += 155

                card_x = 10
                card_y += 160

            self.scrollAreaWidgetContents\
                .setMinimumSize(100, int(len(data)/5*165))
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.scrollAreaWidgetContents.show()


        self.DP.clicked.connect(make_DP_card)
        self.Model.clicked.connect(make_model_card)
        self.Clear.clicked.connect(update_scroll_area)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("DASHBOARD", u"DASHBOARD", None)
            )
        self.DP.setText(QCoreApplication.translate("MainWindow", u"DP", None))
    # retranslateUi

