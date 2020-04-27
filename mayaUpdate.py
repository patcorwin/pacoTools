from datetime import datetime

#import sublime
import sublime_plugin


class MayaUpdateBuildTimeCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):
        '''
        Insert at/replace selection with a string of the current utctime
        '''
        pos = self.view.sel()[0]
        
        self.view.replace(edit, pos, str(datetime.utcnow()) )
