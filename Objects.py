

import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

import LatentFunctions
import MathsFunctions


class Calculator( QtGui.QWidget ):
    def __init__( self, geo_avail ):
        QtGui.QWidget.__init__( self )
        self.geo_avail = geo_avail 
       
        self.setWindowTitle( "Josh's Calculator" )
        self.layout = QtGui.QGridLayout()
        self.pi_char = u'\u03C0'

        self.setupGeometry()
        self.buildScreen()
        self.buildButtons()

        self.setLayout( self.layout )
        self.show()



    def setupGeometry( self ):
        
        #self.setMinimumWidth( self.geo_avail.width() / 8 )
        self.setMaximumWidth( self.geo_avail.width() / 18 ) 

        #self.setMinimumHeight( self.geo_avail.height() / 4 )
        self.setMaximumHeight( self.geo_avail.height() / 14 )


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

                { 'name' : 'Plus', 'text' : ' + ', 'row' : 3 , 'column' : 4 , },
                { 'name' : 'Subtract', 'text' : ' - ', 'row' : 3 , 'column' : 5 , },
                #
                { 'name' : 'Multiply', 'text' : ' x ', 'row' : 2 , 'column' : 4 , },
                { 'name' : 'Divide', 'text' : ' / ', 'row' : 2 , 'column' : 5 , },
                #
                { 'name' : 'LBracket', 'text' : '(', 'row' : 0 , 'column' : 0 , },
                { 'name' : 'RBracket', 'text' : ')', 'row' : 0 , 'column' : 1 , },
                { 'name' : 'Percentage', 'text' : ' % ', 'row' : 0 , 'column' : 2 , },
                { 'name' : 'Pi', 'text' : self.pi_char, 'row' : 0 , 'column' : 3 , },
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
                { 'name' : 'Equals', 'text' : '=', 'row' : 4 , 'column' : 5 , },
                
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
        
        self.font_weight = 120 

        # This is set here as it is required for Button's backspace function
        # The 0 is simply a placeholder
        self.len_difference = 0

        self.setup()

    def setup( self, input_text=False ):
        self.clear()
        self.setAlignment( QtCore.Qt.AlignCenter )

        formatting = QtGui.QTextCharFormat()
        formatting.setFontWeight( self.font_weight )

        cursor = self.textCursor()
        cursor.setCharFormat( formatting )
        self.setTextCursor( cursor )

        if input_text:
            self.textCursor().insertText( input_text )




class Button( QtGui.QPushButton ):
    def __init__( self, name, text, category, row, column, parent=None ):
        QtGui.QPushButton.__init__( self, text=text, parent=parent )
        self.__name__ = name
        self.gridrow = row
        self.gridcolumn = column
        self.calc_screen = self.parent().screen
        self.category = category

        if self.category != 'control':
            self.clicked.connect( lambda: self.addTextToScreen( self.text() ) )

        elif self.__name__ == 'Answer':
            self.clicked.connect( self.answer )            

        elif self.__name__ == 'Backspace':
            self.clicked.connect( self.backspace )

        elif self.__name__ == 'Clear':
            self.clicked.connect( self.calc_screen.setup )            

        elif self.__name__ == 'History':
            self.clicked.connect( self.openHistory )

        elif self.__name__ == 'Equals':
            self.clicked.connect( self.equals )


    def addTextToScreen( self, text ):
        old_text = self.calc_screen.toPlainText()
        if text in [ 'sin', 'cos', 'tan' ]:
            text += '('

        self.calc_screen.textCursor().insertText( text )

        # This information is used by backspace() to remove the correct number of characters
        self.calc_screen.len_difference = len( self.calc_screen.toPlainText() ) - len( old_text )


    def answer( self ):
        pass

    def backspace( self ):
        if not len( self.calc_screen.toPlainText() ) < 1:
            [ self.calc_screen.textCursor().deletePreviousChar() for x in xrange( self.calc_screen.len_difference ) ]
            
            if not len( self.calc_screen.toPlainText() ) < 1:
                # This code ensures that the correct number of chars are deleted if backspace() is called repeatedly
                exemption_list = [ ' ', 'n', 's' ]
                if self.calc_screen.toPlainText()[ self.calc_screen.textCursor().position() - 1 ] in exemption_list:
                    self.calc_screen.len_difference = 3
                else:
                    self.calc_screen.len_difference = 1

            else:
                # Corrects a bug whereby the font weight gets reset if Screen is empty 
                self.calc_screen.setFontWeight( self.calc_screen.font_weight )

        else:
            pass



    def openHistory( self ):
        pass

    def equals( self ):
        result = MathsFunctions.solveCalculation( self.calc_screen.toPlainText() )
        self.calc_screen.setup( input_text=result )




#class HistoryWindow



