# -*- coding: utf-8 -*-
#
# Klassensammlung für Grafiken und SVG
#

class Graphic:
    def getSVGPrefix( self ):
        """ Return head of SVG file 
        @rtype: str
        @return: header part of SVG XML output
        """
        # FIXME: epydoc gets confused with tags within the source display
        #        use escape chars for <> to fix that
        return '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">'

    def getSVGSuffix( self ):
        """ Return tail of SVG file 
        @rtype: str
        @return: tail part of SVG XML output
        """
        return '</svg>'

    def getSVGContent( self ):
        """ Return content of SVG file. 
        @rtype: str
        @return: content part of SVG XML output
        """
        return ''

    def getSVG( self ):
        """ Return SVG file. The whole file is formed by
        concatenating prefix, content and suffix.
        @rtype: str
        @return: valid SVG XML output
        """
        return self.getSVGPrefix() + self.getSVGContent() + self.getSVGSuffix()

    def getStyle( self ):
        """ Return fixed Style attributes
        @return: attibutes for SVG element tag defining actual style
        @rtype: str
        """

        try:
            stroke, width, fill = self._stroke, self._width, self._fill
        except AttributeError:
            stroke, width, fill = 'black', 2, 'white'
        return f'stroke="{stroke}" stroke-width="{width}" fill="{fill}"'

    def setStyle(self, stroke: str, width: int, fill: str):
        """ Set style attributes
        @param stroke: stroke color
        @type stroke: str
        @param width: stroke width
        @type width: int
        @param fill: fill color
        @type fill: str
        """
        self._stroke = stroke
        self._width = width
        self._fill = fill




class GraphicGroup( Graphic ): # erbt von Graphic
    " Group of graphic elements "
    def __init__( self ):
        self._elements = []

    def getSVGContent( self ):
        ret = ""
        for element in self._elements:
            ret += element.getSVGContent()

        return ret

    def addElement( self, element: Graphic ):
        """ Adds element to group
        @param element: element to add
        @type element: Graphic
        """
        self._elements.append( element )

    def getElements( self ):
        """ Get elements 
        @return: elements in group 
        @rtype: list of Graphic objects
        """
        return self._elements

    def removeElement( self, element ):
        """ Remove element from group
        @param element: element to remove
        @type element: Graphics
        """
        self._elements[:] = [x for x in self._elements if not element == x]


class Circle( Graphic ):
    def __init__( self, center, radius ):
        """ Creates new circle with parameters
        @param center: centre point
        @type center: tuple of int
        @param radius: radius of circle
        @type radius: int
        """
        self.setCenter( center )
        self.setRadius( radius )

    def setCenter( self, center ):
        """ Set centre point
        @param center: centre point
        @type center: tuple of int
        """
        self._center = center

    def setRadius( self, radius ):
        """ Set radius
        @param radius: radius of circle
        @type radius: int
        """
        self._radius = radius

    def getRadius( self ):
        """ Get radius
        @return: radius
        @rtype: int
        """
        return self._radius

    def getCenter( self ):
        """ Get center
        @return: centre point
        @rtype: tuple of int
        """
        return self._center

    def getSVGContent( self ):
        return '<circle cx="%d" cy="%d" r="%d" %s />' \
                %( self.getCenter()[0], self.getCenter()[1],
                   self.getRadius(), self.getStyle() )


class Rectangle( Graphic ):
    def __init__( self, p1, p2, rotation=0 ):
        """ Create new rectangle
        @param p1: upper left corner
        @type p1: ( int, int )
        @param p2: lower right corner
        @type p2: ( int, int )
        @param rotation: rotation angle in degree for rotation around center
        @type rotation: int
        """
        self.setPoints( p1, p2 )
        self.setRotation( rotation )

    def setPoints( self, p1, p2 ):
        """ Set rectangle corners
        @param p1: upper left corner
        @type p1: ( int, int )
        @param p2: lower right corner
        @type p2: ( int, int )
        """
        self._p1 = p1
        self._p2 = p2

    def setRotation( self, rotation ):
        """ Set rotation angle for rotation around center
        @param rotation: rotation angle in degree
        @type rotation: int
        """
        self._rotation = rotation

    def getPoints( self ):
        """ Get corner points 
        @return: coordinates for upper right and lower left corner (ignoring
        any rotation)
        @rtype: ( ( int, int ), (int, int ) )
        """
        return ( self._p1, self._p2 )

    def getRotation( self ):
        """ Get rotation angle
        @return: rotation angle in degree
        @rtype: int
        """
        return self._rotation

    def getSVGContent( self ):
        center = self.getCenter()
        return '<rect x="%d" y="%d" width="%d" height="%d" transform="rotate(%d,%d,%d)" %s />' \
                %( self.getPoints()[0][0], self.getPoints()[0][1],
                        self.getPoints()[1][0] - self.getPoints()[0][0],
                        self.getPoints()[1][1] - self.getPoints()[0][1],
                        self.getRotation(), center[0], center[1], self.getStyle() )

    def getCenter( self ):
        """ Get center of rectangle for rotation
        @return: coordinate for center of rectangle
        @rtype: ( int, int )
        """
        return ( ( self._p1[0] + self._p2[0] ) / 2, ( self._p1[1] + self._p2[1] ) / 2 )


class Line(Graphic):
    def __init__(self, p1: tuple[int, int], p2: tuple[int, int]):
        self.positions = p1, p2

    def getSVGContent(self) -> str:
        (x1, y1), (x2, y2) = self.positions
        # <line x1="0" y1="80" x2="100" y2="20" />
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {self.getStyle()}/>'


class Triangle(Graphic):
    def __init__(self, p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]):
        self.positions = p1, p2, p3

    def getSVGContent(self) -> str:
        # <polygon points="0,100 50,25 50,75" />
        (a1, a2), (b1, b2), (c1, c2) = self.positions
        return f'<polygon points="{a1},{a2} {b1},{b2} {c1},{c2}" {self.getStyle()}/>'



if __name__ == "__main__":
    head = Circle( ( 70, 30 ), 20 )
    body = Rectangle( (40, 50), ( 100, 110 ) )
    body.setRotation( 45 )
    body.setStyle('red', 2, 'blue')
    legs = (Triangle( ( 50, 80 ), ( 50, 150 ), ( 40, 150 ) ),
            Triangle( ( 90, 80 ), ( 90, 150 ), ( 100, 150 ) ) )

    eyes = (Line( ( 55, 25 ), ( 60, 25 ) ),
            Line( ( 80, 25 ), ( 85, 25 ) ) )

    nose = Triangle( ( 70, 30 ), ( 68, 35 ), ( 72, 35 ) )

    arms = (Rectangle( ( 10, 60 ), ( 60, 65 ), 10 ), 
            Rectangle( ( 80, 60 ), ( 130, 65 ), 20 ) )

    gfx = GraphicGroup()
    gfx.addElement( legs[0] )
    gfx.addElement( legs[1] )
    gfx.addElement( arms[0] )
    gfx.addElement( arms[1] )
    gfx.addElement( body )
    gfx.addElement( head )
    gfx.addElement( eyes[0] )
    gfx.addElement( eyes[1] )
    gfx.addElement( nose )

    svgout = open( "output1.svg", "w" )
    svgout.write( gfx.getSVG() )
    svgout.close()

