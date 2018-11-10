import os
import sys
import urllib.request
import json
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QAbstractListModel, Qt, QUrl, QStringListModel
from PySide2.QtGui import QGuiApplication
from PySide2.QtWidgets import QApplication

if __name__ == '__main__':
    # get our data
    url = 'http://country.io/names.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    # Format data
    _list = sorted(data.values())
    
    #Setup the application window

    app = QApplication(sys.argv)
    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    url = QUrl("main.qml")    
    
    # Expose a model to the Qml code
    my_model = QStringListModel()
    my_model.setStringList(_list)
    view.rootContext().setContextProperty('myModel', my_model)
    
    #Load the QML file
    view.setSource(url)        
    
    # Show the window
    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.show()
    
    # Execute and cleanup
    app.exec_()
    del view
    
