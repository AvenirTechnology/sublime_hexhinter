import sublime, sublime_plugin

class HexCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        hex = False
        sels = self.view.sel()
        for sel in sels:
            if self.view.substr(sel).find('0x') != -1:
                dec = self.view.substr(sel)
                dec = int(dec, 16) # convert from hex, to int value
                self.view.show_popup(str(dec))
