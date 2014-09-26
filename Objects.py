
import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

import LatentFunctions
import MathsFunctions




class Calculator( QtGui.QWidget ):
    def __init__( self, geo_avail ):
        QtGui.QWidget.__init__( self )
        self.setWindowTitle( "Josh's Calculator" )


        self.geo_avail = geo_avail       

        self.setupGeometry()
        self.setupLayout()
        self.buildScreen()
        self.buildButtons()

        self.setLayout( self.layout )
        self.show()



    def setupGeometry( self ):
        
        #self.setMinimumWidth( self.geo_avail.width() / 8 )
        self.setMaximumWidth( self.geo_avail.width() / 8 ) 

        #self.setMinimumHeight( self.geo_avail.height() / 4 )
        self.setMaximumHeight( self.geo_avail.height() / 4 )


    def setupLayout( self ):
        self.layout = QtGui.QGridLayout()
        x = [ ( 0 , 0 ), ( 0 , 2 ), ( 0 , 4 ), ( 2 , 4 ) ]

        for i in x:
            y = QtGui.QLabel()
            y.setMinimumWidth( self.geo_avail.width() / 20 )
            y.setMinimumHeight( self.geo_avail.width() / 20 )
            self.layout.addWidget( QtGui.QLabel(), i[ 0 ], i[ 1 ] )


    def buildScreen( self ):
        self.screen = Screen( parent = self )
        self.layout.addWidget( self.screen, 1, 1 )



    def buildButtons( self ):

        self.number_dicts = [

                { 'name' : 'Zero', 'text' : '0', 'row' : 4 , 'column' : 0 , },
                { 'name' : 'Decimal', 'text' : '.', 'row' : 4 , 'column' : 1 , },
                #
                { 'name' : 'One', 'text' : '1', 'row' : 3 , 'column' : 0 , },
                { 'name' : 'Two', 'text' : '2', 'row' : 3 , 'column' : 1 , },
                { 'name' : 'Three', 'text' : '3', 'row' : 3 , 'column' : 2 , },
                #
                { 'name' : 'Four', 'text' : '4', 'row' : 2 , 'column' : 0 , },
                { 'name' : 'Five', 'text' : '5', 'row' : 2 , 'column' : 1 , },
                { 'name' : 'Six', 'text' : '6', 'row' : 2 , 'column' : 2 , },
                #
                { 'name' : 'Seven', 'text' : '7', 'row' : 1 , 'column' : 0 , },
                { 'name' : 'Eight', 'text' : '8', 'row' : 1 , 'column' : 1 , },
                { 'name' : 'Nine', 'text' : '9', 'row' : 1 , 'column' : 2 , },
               
                ]

        self.operation_dicts = [

                { 'name' : 'Equals', 'text' : '=', 'row' : 4 , 'column' : 5 , },
                #
                { 'name' : 'Plus', 'text' : '+', 'row' : 3 , 'column' : 4 , },
                { 'name' : 'Subtract', 'text' : '-', 'row' : 3 , 'column' : 5 , },
                #
                { 'name' : 'Multiply', 'text' : 'x', 'row' : 2 , 'column' : 4 , },
                { 'name' : 'Divide', 'text' : '/', 'row' : 2 , 'column' : 5 , },
                #
                { 'name' : 'LBracket', 'text' : '(', 'row' : 0 , 'column' : 0 , },
                { 'name' : 'RBracket', 'text' : ')', 'row' : 0 , 'column' : 1 , },
                { 'name' : 'Percentage', 'text' : '%', 'row' : 0 , 'column' : 2 , },
                { 'name' : 'Pi', 'text' : 'Pi', 'row' : 0 , 'column' : 3 , },
                { 'name' : 'Exponent', 'text' : '^', 'row' : 0 , 'column' : 4 , },
                #
                { 'name' : 'Sine', 'text' : 'sin', 'row' : 1 , 'column' : 3 , },                            
                { 'name' : 'Cosine', 'text' : 'cos', 'row' : 2 , 'column' : 3 , },
                { 'name' : 'Tangent', 'text' : 'tan', 'row' : 3 , 'column' : 3 , },
               
                ]

        self.control_dicts = [

                { 'name' : 'Answer', 'text' : 'Ans', 'row' : 4 , 'column' : 4 , },
                { 'name' : 'Backspace', 'text' : 'Del', 'row' : 1 , 'column' : 4 , },
                { 'name' : 'Clear', 'text' : 'AC', 'row' : 1 , 'column' : 5 , },
                { 'name' : 'History', 'text' : 'His', 'row' : 0 , 'column' : 5 , },
                
                ]

        self.button_layout = QtGui.QGridLayout()

        for x in self.number_dicts:
            x[ 'parent' ] = self
            x[ 'category' ] = 'number'
            self.button_layout.addWidget( Button( **x ), x[ 'row' ], x[ 'column' ] )

        for x in self.operation_dicts:
            x['parent'] = self
            x[ 'category' ] = 'operation'
            self.button_layout.addWidget( Button( **x ), x[ 'row' ], x[ 'column' ] )

        for x in self.control_dicts:
            x['parent'] = self
            x[ 'category' ] = 'control'
            self.button_layout.addWidget( Button( **x ), x[ 'row' ], x[ 'column' ] )

        self.layout.addLayout( self.button_layout, 3, 1 )


            
class Screen( QtGui.QTextEdit ):
    def __init__( self, parent=None):
        QtGui.QTextEdit.__init__( self, parent=parent )


class Button( QtGui.QPushButton ):
    def __init__( self, name, text, category, row, column, parent=None ):
        QtGui.QPushButton.__init__( self, text=text, parent=parent )
        self.__name__ = name
        self.gridrow = row
        self.gridcolum = column
        self.calc_screen = self.parent().screen
        self.category = category

        if self.category != 'control':
            self.clicked.connect( self.addTextToScreen )

        elif self.__name__ == 'Answer':
            self.clicked.connect( self.answer )            

        elif self.__name__ == 'Backspace':
            self.clicked.connect( self.backspace )

        elif self.__name__ == 'Clear':
            self.clicked.connect( self.calc_screen.clear )            

        elif self.__name__ == 'History':
            self.clicked.connect( self.openHistory )


    def addTextToScreen( self ):
        current_text = self.calc_screen.toPlainText()
        self.calc_screen.setText( current_text + self.text() )
        cursor = self.calc_screen.textCursor()
        cursor.movePosition( QtGui.QTextCursor.EndOfLine )
        self.calc_screen.setTextCursor( cursor )

    def answer( self ):
        pass

    def backspace( self ):
        current_text = self.calc_screen.toPlainText()
        if not len( current_text ) < 1:
            self.calc_screen.setText( self.calc_screen.toPlainText()[ :-1 ] )
        else:
            pass

    def openHistory( self ):
        pass









