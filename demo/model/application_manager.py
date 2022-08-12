from selene import have, command
from selene.support.shared import browser
from demo.model.components.modal_dialog import ModalDialog
from demo.model.pages.student_registration_page import StudentRegistrationForm


class ApplicationManager:
    def __init__(self):
        self.form = StudentRegistrationForm()
        self.results = ModalDialog()

    def given_student_registration_form_opened(self):
        browser.open('/automation-practice-form')
        (
            browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]')
                .with_(timeout=10)
                .should(have.size_greater_than_or_equal(1))
                .perform(command.js.remove)
        )
        return self


app = ApplicationManager()