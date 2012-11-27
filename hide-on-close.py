from gi.repository import GObject, Peas

class HideOnClose(GObject.Object, Peas.Activatable):
    object = GObject.property(type=GObject.GObject)

    def __init__(self):
        super(HideOnClose, self).__init__()

    def do_activate(self):
        self.window = self.object.get_property("window")
        self.handler_id = self.window.connect("delete-event", self.delete_event_cb)

    def do_deactivate(self):
        self.window.show()
        self.window.disconnect(self.handler_id) 

    def delete_event_cb(self, widget, event):
        self.window.hide()
        return True
