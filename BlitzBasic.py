import sublime, sublime_plugin

import os

class BuildbbCommand(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        
        v = self.window.active_view()
        path = v.file_name()
        if not (os.path.exists(path)):
            print("[BlitzBasic] Not a valid .bb file. (%s) " % (path))
            return
        """
            First: We need the Path to blitzcc.exe; Load it from Settings!
        """
        settings = sublime.load_settings('BlitzBasic.sublime-settings')
        blitz_path = settings.get('blitz_path')
        
        """
            The kwargs Dictionary contains the build-parameter:
        for key, value in kwargs.items():
            print("%s == %s" % (key,value))
        """

        """
            We Copy all build parameter in a new Dictionary
        """
        arguments={}
        for i in kwargs:
            arguments[i] = kwargs[i]

        """
            Now we can add the necessary paths from the Settings
        """
        arguments["path"] = blitz_path + "bin\\"
        arguments["env"] = {"blitzpath": blitz_path}

        """
            Just exec it. 
            Maybe run blitzcc in future ourselfes or something
        """
        self.window.run_command("exec", arguments)
