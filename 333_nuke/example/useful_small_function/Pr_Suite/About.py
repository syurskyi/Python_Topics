import nuke
import nukescripts
import webbrowser

def About():
	class AboutPanel(nukescripts.PythonPanel):
		def __init__(self, about):
			nukescripts.PythonPanel.__init__(self, "About Pr_Suite")
			self.setMinimumSize(311, 311)
			self.logo = nuke.PyScript_Knob("about_pr_suite", "<img src='About_Pr_Suite.png'>", "webbrowser.open('http://www.parimalvfx.com/rnd/pr_suite/')")
			self.addKnob(self.logo)

	show = AboutPanel( "about" )
	show.showModal()