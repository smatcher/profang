# ProFang productivity assistant

## Bootstrap

- Make sure that all the requisites are installed
- Run bootstrap.bat

## Requisites

- Everything x64         (<https://www.voidtools.com>)
- Python 3 x64           (<https://www.python.org/downloads/>)
- libclang for Python    (py -3 -m pip install clang)
- PySide2                (py -3 -m pip install PySide2)
- Apprise                (py -3 -m pip install apprise)
- Clipboard              (py -3 -m pip install clipboard)

Optional

- Qt Creator             (<https://www.qt.io>)
- Visual Studio Code     (<https://code.visualstudio.com/>)
- pypiwin32              (py -3 -m pip install pypiwin32)

## UI

The ui related code is located in the qt_uis folder. Use _Qt Creator_ to edit the __xxx.ui__ forms, __ui_xxx.py__ files are generated from these forms using uic.

In order to generate py code from ui forms you can either

- Run the "__run uic__" task in visual studio code
- Run "__run_uic.bat__" in the qt_uis folder
