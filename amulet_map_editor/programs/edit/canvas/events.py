from wx.lib import newevent

CameraMoveEvent, EVT_CAMERA_MOVE = newevent.NewEvent()
CameraRotateEvent, EVT_CAMERA_ROTATE = newevent.NewEvent()
DimensionChangeEvent, EVT_DIMENSION_CHANGE = newevent.NewEvent()

# the active tool changed
ToolChangeEvent, EVT_TOOL_CHANGE = newevent.NewEvent()
PasteEvent, EVT_PASTE = newevent.NewEvent()

UndoEvent, EVT_UNDO = newevent.NewEvent()
RedoEvent, EVT_REDO = newevent.NewEvent()
CreateUndoEvent, EVT_CREATE_UNDO = newevent.NewEvent()
SaveEvent, EVT_SAVE = newevent.NewEvent()
EditCloseEvent, EVT_EDIT_CLOSE = newevent.NewEvent()

# the block highlighted by the cursor changed position.
SelectionPointChangeEvent, EVT_SELECTION_POINT_CHANGE = newevent.NewEvent()

# events fired when the active selection box changes.  TODO: reimplement these
BoxChangeEvent, EVT_BOX_CHANGE = newevent.NewEvent()  # one or more of the box coordinates have changed
BoxPoint1ChangeEvent, EVT_BOX_POINT_1_CHANGE = newevent.NewEvent()  # the first box corner has changed
BoxPoint2ChangeEvent, EVT_BOX_POINT_2_CHANGE = newevent.NewEvent()  # the second box corner has changed
BoxEditToggleEvent, EVT_BOX_EDIT_TOGGLE = newevent.NewEvent()  # the box has switched between edit and static mode