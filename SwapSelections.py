import sublime, sublime_plugin


class SwapSelectionsCommand(sublime_plugin.TextCommand):

	def is_enabled(self):
		return len(self.view.sel()) >= 2

	def run(self, edit):
		sel = self.view.sel()
		
		strings = [self.view.substr(r) for r in sel]
		
		# Rotate the tail to the head. 
		strings.insert(0, strings.pop())
		string_iter = iter(strings)

		for r in sel:
			self.view.replace(edit, r, next(string_iter))
