class BaseView:
    def render(self):
        print(" Template render")

class AuthRequiredMixin(BaseView):
    def __init__(self, authed=True):
        self.authed = authed
    def render(self):
        if not self.authed:
            print(" Access denied")
            return
        print(" Auth ok")
        super().render()

class LoggingMixin(AuthRequiredMixin):
    def render(self):
        print(" Log: start")
        super().render()
        print(" Log: end")

class AdminPageView(LoggingMixin):
    def render(self):
        print(" Admin page render start")
        super().render()
        print(" Admin page render end")

AdminPageView(authed=True).render()